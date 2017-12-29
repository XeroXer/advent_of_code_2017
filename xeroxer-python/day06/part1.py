#!/usr/bin/env python
"""Advent of Code 2017: Day 06, Part 1"""

def main():
    """Main function"""
    file = open('input.txt', 'r')
    line = [int(x) for x in file.readline().rstrip('\n').split()]
    max_len = (len(line) - 1)
    previous = []
    steps = 0
    str_line = "_".join([str(x) for x in line])
    while str_line not in previous:
        previous.append(str_line)
        max_value = max(line)
        curr_index = line.index(max_value)
        line[curr_index] = 0
        while max_value > 0:
            curr_index += 1
            if curr_index > max_len:
                curr_index = 0
            line[curr_index] += 1
            max_value -= 1
        steps += 1
        str_line = "_".join([str(x) for x in line])
    print(steps)

if __name__ == '__main__':
    main()
