#!/usr/bin/env python
"""Advent of Code 2017: Day 07, Part 1"""

def main():
    """Main function"""
    with open('input.txt') as file:
        parents = set()
        children = set()
        for line in file:
            if " -> " in line:
                row = line.strip().split(" -> ")
                parents.add(row[0].split()[0])
                for child in row[1].split(", "):
                    children.add(child)
        print(parents - children)

if __name__ == '__main__':
    main()
