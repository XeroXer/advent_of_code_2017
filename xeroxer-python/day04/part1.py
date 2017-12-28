#!/usr/bin/env python
"""Advent of Code 2017: Day 04, Part 1"""

def main():
    """Main function"""
    valid_num = 0
    file = open('input.txt', 'r')
    for line in file:
        words = line.split()
        seen = set()
        dups = set(x for x in words if x in seen or seen.add(x))
        if not dups:
            valid_num += 1
    print(valid_num)

if __name__ == '__main__':
    main()
