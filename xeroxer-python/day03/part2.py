#!/usr/bin/env python
"""Advent of Code 2017: Day 03, Part 2"""

INPUT = 289326
GRID = {"0_0": 1}

def get_cell_value(xpos, ypos):
    """Calculate cell value"""
    grid_sum = 0
    for i in range((xpos - 1), (xpos + 2)):
        for j in range((ypos - 1), (ypos + 2)):
            if "%d_%d" % (i, j) in GRID.keys():
                grid_sum += GRID["%d_%d" % (i, j)]
    return grid_sum

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
        GRID["%d_%d" % (x_pos, y_pos)] = get_cell_value(x_pos, y_pos)
        if GRID["%d_%d" % (x_pos, y_pos)] > INPUT:
            print(GRID["%d_%d" % (x_pos, y_pos)])
            break
        steps += 1
        if steps >= turn_after:
            steps = 0
            direction -= 1
            if direction < 0:
                direction = 3
            if direction in (1, 3):
                turn_after += 1
        i += 1

if __name__ == '__main__':
    main()
