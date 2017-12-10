from functools import reduce

class ListNode(object):
    def __init__(self, val, pos):
        self.pos = pos
        self.val = val
        self.next = None
        self.prev = None

    def move(self, num):
        if num == 0:
            return self
        curr = self
        while num < 0:
            curr = curr.prev
            num += 1
        while num > 0:
            curr = curr.next
            num -= 1
        return curr

    def find_start(self):
        curr = self
        while True:
            if curr.pos == 0:
                break
            curr = curr.next
        return curr

    def __str__(self):
        return f'{self.pos}:{self.val}'

def reverse(start, length, total_length):
    if length <= 1:
        return start

    # save this reference so we can connect up the start
    start_pos = start.pos
    before_start = start.prev
    curr = start
    while length > 0:
        _next = curr.next
        _prev = curr.prev
        # print(curr, _next, _prev)
        # save it so we can connect the end
        curr.prev = _next
        after_end = _next
        curr.next = _prev
        last = curr
        curr = _next
        length -= 1

    if last != before_start:
        # last should be at the start
        last.prev = before_start
        before_start.next = last
    if start != after_end:
        # first should be at the end
        start.next = after_end
        after_end.prev = start

    # fix positions (UUGH)
    end_pos = last.pos
    pos = start_pos
    curr = last
    while pos != end_pos: #could lap around
        curr.pos = pos
        curr = curr.next
        pos = (pos + 1) % total_length
    start.pos = end_pos

    # return new start position
    return last


def print_chain(node):
    curr = node.find_start()
    _list = [str(curr.val)]
    curr = curr.next
    while curr.pos != 0:
        _list.append(str(curr.val))
        curr = curr.next

    print(",".join(_list))



def knot_round(start, lengths, skip_size):
    current_pos = start

    for length in lengths:
        # 1. Reverse order of selected elements
        current_pos = reverse(current_pos, length, total_length)

        # 2. Move current position forward
        current_pos = current_pos.move(skip_size + length)

        # 3. Increase skip size.
        skip_size = (skip_size + 1) % total_length
    return current_pos, skip_size

total_length = 256
# Make a doubly linked list
start = ListNode(0, 0)
p = 1
curr = start
for val in range(1,total_length):
    node = ListNode(val, p)
    node.prev = curr
    curr.next = node
    curr = node
    p += 1
# Link up the ends.
curr.next = start
start.prev = curr

raw_input = input()

# # Solve 10a
# lengths = [int(i) for i in raw_input.split(",")]
# curr, _ = knot_round(start, lengths)
# print(start.val * start.next.val)

byte_lengths = [ord(i) for i in raw_input.strip()]
suffix = [17, 31, 73, 47, 23]
byte_lengths.extend(suffix)
# print(byte_lengths)
skip_size = 0
curr = start
for _ in range(64):
    curr, skip_size = knot_round(curr, byte_lengths, skip_size)

# Compute dense hash
start = curr.find_start()
values = []
curr = start
for _ in range(total_length):
    values.append(curr.val)
    curr = curr.next

# print(values)
# Perform xor
hx = ""
for i in range(0, 256, 16):
    xored_byte = reduce(lambda p,c: p ^ c, values[i:i+16], 0)
    h = hex(xored_byte)[2:]
    if len(h) == 1:
        h = '0' + h
    hx += h

print(hx)

# print_chain(start)