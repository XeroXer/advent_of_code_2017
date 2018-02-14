#!/usr/bin/env python
"""Advent of Code 2017: Day 23, Part 1"""

import re

def handle_instructions(instructions):
    """Handle input instructions"""
    num_mul = 0
    values = {}
    for code in range(ord('a'), ord('h') + 1):
        values[chr(code)] = 0
    i = 0
    while i < len(instructions):
        if isinstance(instructions[i][2], int):
            workint = instructions[i][2]
        else:
            workint = values[instructions[i][2]]

        if instructions[i][0] == 'set':
            values[instructions[i][1]] = workint
        elif instructions[i][0] == 'sub':
            values[instructions[i][1]] -= workint
        elif instructions[i][0] == 'mul':
            values[instructions[i][1]] *= workint
            num_mul += 1
        else:
            if isinstance(instructions[i][1], int):
                instructint = instructions[i][1]
            else:
                instructint = values[instructions[i][1]]

            if instructint != 0:
                i += workint
                continue
        i += 1
    print(num_mul)

def main():
    """Main function"""
    with open('input.txt') as file:
        instructions = []
        for line in file:
            instruction = line.split()
            rmatch = re.match(
                r"[a-h]+",
                instruction[2]
            )
            if not rmatch:
                instruction[2] = int(instruction[2])
            if instruction[0] == 'jnz':
                rmatch2 = re.match(
                    r"[a-h]+",
                    instruction[1]
                )
                if not rmatch2:
                    instruction[1] = int(instruction[1])
            instructions.append(instruction)
        handle_instructions(instructions)

if __name__ == '__main__':
    main()
