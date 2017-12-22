#!/usr/bin/env python
"""Advent of Code 2017: Day 02, Part 1"""

def main():
    """Main function"""
    checksum = 0
    file = open('input.txt', 'r')
    for line in file:
        numbers = line.split()
        numbers.sort(key=int)
        checksum += int(numbers[-1]) - int(numbers[0])
    print(checksum)

if __name__ == '__main__':
    main()
