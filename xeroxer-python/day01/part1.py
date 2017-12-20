#!/usr/bin/env python
"""Advent of Code 2017: Day 01, Part 1"""

def main():
    """Main function"""
    file = open('input.txt', 'r')
    line = file.readline().rstrip('\n')
    prev = None
    first = None
    total = 0
    for char in line:
        charint = int(char)
        if prev == charint:
            total += charint
        prev = charint
        if first is None:
            first = charint
    if charint == first:
        total += first
    file.close()
    print(total)

if __name__ == '__main__':
    main()
