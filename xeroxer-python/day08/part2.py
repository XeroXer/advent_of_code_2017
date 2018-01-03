#!/usr/bin/env python
"""Advent of Code 2017: Day 08, Part 2"""

import re

def main():
    """Main function"""
    with open('input.txt') as file:
        registers = dict()
        max_value = 0
        for line in file:
            rmatch = re.match(
                r"(\w+)\s(inc|dec)\s(-*\d+)\sif\s(\w+)\s(<|>|<=|>=|==|!=)\s(-*\d+)",
                line.strip()
            )
            if rmatch:
                rmatch_groups = rmatch.groups()

                compare_register = registers.get(rmatch_groups[3], 0)
                compare_value = int(rmatch_groups[5])
                if not eval("%s %s %d" % (compare_register, rmatch_groups[4], compare_value)):
                    continue

                register_value = registers.get(rmatch_groups[0], 0)
                if rmatch_groups[1] == "inc":
                    registers[rmatch_groups[0]] = register_value + int(rmatch_groups[2])
                else:
                    registers[rmatch_groups[0]] = register_value - int(rmatch_groups[2])
                if max_value < registers[rmatch_groups[0]]:
                    max_value = registers[rmatch_groups[0]]
        print(max_value)

if __name__ == '__main__':
    main()
