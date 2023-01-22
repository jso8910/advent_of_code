from collections import defaultdict
from math import ceil


def get_input():
    with open("day_22/input.txt", "r") as f:
        file = f.read().splitlines()

    grid = defaultdict(bool)

    # -(1+1j) because we are 0 indexing
    starting_point = ceil(len(file[0]) / 2) - 1 + ceil(len(file) / 2) * 1j - 1j
    for row_idx, row in enumerate(file):
        for col_idx, char in enumerate(row):
            grid[col_idx + row_idx*1j] = char == "#"

    return grid, starting_point


def clockwise(dir):
    match dir:
        case -1j:
            return 1
        case 1:
            return 1j
        case 1j:
            return -1
        case -1:
            return -1j


def counter_clockwise(dir):
    match dir:
        case -1j:
            return -1
        case -1:
            return 1j
        case 1j:
            return 1
        case 1:
            return -1j


def reverse(dir):
    return dir*-1


def part_one(grid, starting_point):
    dir = -1j
    num_infected = 0
    point = starting_point
    for i in range(10_000):
        # print(clockwise(point), counter_clockwise(point))
        dir = clockwise(dir) if grid[point] else counter_clockwise(dir)
        if not grid[point]:
            num_infected += 1
        grid[point] = not grid[point]
        point += dir

    return num_infected


def part_two(grid, starting_point):
    dir = -1j
    num_infected = 0
    point = starting_point
    for key in grid:
        grid[key] = 2 if grid[key] else 0

    # 0 = clean
    # 1 = weakened
    # 2 = infected
    # 3 = flagged
    for i in range(10_000_000):
        match grid[point]:
            case 0:
                dir = counter_clockwise(dir)
            case 1:
                dir = dir
            case 2:
                dir = clockwise(dir)
            case 3:
                dir = reverse(dir)
        grid[point] += 1
        grid[point] %= 4
        if grid[point] == 2:
            num_infected += 1
        point += dir

    return num_infected


print(part_one(*get_input()))
print(part_two(*get_input()))
