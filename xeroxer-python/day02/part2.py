#!/usr/bin/env python
"""Advent of Code 2017: Day 02, Part 2"""

def main():
    """Main function"""
    checksum = 0
    file = open('input.txt', 'r')
    for line in file:
        numbers = line.split()
        numbers.sort(key=int, reverse=True)
        numbers = [int(x) for x in numbers]
        for num1 in numbers:
            for num2 in numbers:
                if num1 != num2 and (num1 % num2) == 0:
                    checksum += int(num1 / num2)
                    break
            else:
                continue
            break
    print(checksum)

if __name__ == '__main__':
    main()
