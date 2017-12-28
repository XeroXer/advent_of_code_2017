#!/usr/bin/env python
"""Advent of Code 2017: Day 03, Part 1"""

INPUT = 289326

def main():
    """Main function"""
    x_pos = 0
    y_pos = 0
    direction = 1
    turn_after = 1
    steps = 0
    i = 1
    while i < INPUT:
        if direction == 0:
            y_pos += 1
        elif direction == 1:
            x_pos += 1
        elif direction == 2:
            y_pos -= 1
        else:
            x_pos -= 1
        steps += 1
        if steps >= turn_after:
            steps = 0
            direction -= 1
            if direction < 0:
                direction = 3
            if direction in (1, 3):
                turn_after += 1
        i += 1
    print(abs(x_pos) + abs(y_pos))

if __name__ == '__main__':
    main()
