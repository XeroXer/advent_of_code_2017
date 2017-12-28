#!/usr/bin/env python
"""Advent of Code 2017: Day 05, Part 2"""

def main():
    """Main function"""
    file = open('input.txt', 'r')
    lines = [int(line.strip()) for line in file]
    pos = 0
    steps = 0
    while True:
        try:
            val = lines[pos]
            if lines[pos] >= 3:
                lines[pos] -= 1
            else:
                lines[pos] += 1
            pos += val
            steps += 1
        except IndexError:
            break
    print(steps)

if __name__ == '__main__':
    main()
