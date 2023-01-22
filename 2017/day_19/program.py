from collections import defaultdict


def get_input():
    with open("day_19/input.txt", "r") as f:
        file = f.read().splitlines()

    grid = defaultdict(bool)
    for row, line in enumerate(file):
        for col, char in enumerate(line):
            grid[col + row*1j] = char if char != " " else False

    return grid


def rotate_right(dir):
    match dir:
        case -1j:
            return 1
        case 1:
            return 1j
        case 1j:
            return -1
        case -1:
            return -1j


def rotate_left(dir):
    match dir:
        case -1j:
            return -1
        case -1:
            return 1j
        case 1j:
            return 1
        case 1:
            return -1j


def part_one(grid):
    start = [char for key, char in grid.items() if key.imag == 0].index("|")
    loc = start
    current_dir = 1j
    letters = ""
    while True:
        if grid[loc] != "+":
            if not grid[loc]:
                break
            if grid[loc] not in ["|", "-"]:
                letters += grid[loc]
            loc = loc + current_dir
        else:
            if grid[loc + current_dir]:
                loc = loc + current_dir
            else:
                current_dir = rotate_right(
                    current_dir) if grid[loc + rotate_right(current_dir)] else rotate_left(current_dir)
                loc = loc + current_dir

    return letters


def part_two(grid):
    start = [char for key, char in grid.items() if key.imag == 0].index("|")
    loc = start
    current_dir = 1j
    steps = 0
    while True:
        if grid[loc] != "+":
            if not grid[loc]:
                break
            loc = loc + current_dir
        else:
            if grid[loc + current_dir]:
                loc = loc + current_dir
            else:
                current_dir = rotate_right(
                    current_dir) if grid[loc + rotate_right(current_dir)] else rotate_left(current_dir)
                loc = loc + current_dir
        steps += 1

    return steps


print(part_one(get_input()))
print(part_two(get_input()))
