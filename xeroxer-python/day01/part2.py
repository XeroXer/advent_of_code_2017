#!/usr/bin/env python
"""Advent of Code 2017: Day 01, Part 2"""

def main():
    """Main function"""
    file = open('input.txt', 'r')
    line = file.readline().rstrip('\n')
    length = len(line)
    steps = int(length / 2)
    total = 0
    for i in range(len(line)):
        i = int(i)
        j = int(i + steps)
        if j >= length:
            j -= length
        if line[i] == line[j]:
            total += int(line[i])
    file.close()
    print(total)

if __name__ == '__main__':
    main()
