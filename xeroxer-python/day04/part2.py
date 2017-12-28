#!/usr/bin/env python
"""Advent of Code 2017: Day 04, Part 2"""

def main():
    """Main function"""
    valid_num = 0
    file = open('input.txt', 'r')
    for line in file:
        words = line.split()
        seen = set()
        dups = False
        for word in words:
            word_list = list(word)
            word_list.sort()
            word_list = str(word_list)
            if word_list in seen:
                dups = True
                break
            else:
                seen.add(word_list)
        if not dups:
            valid_num += 1
    print(valid_num)

if __name__ == '__main__':
    main()
