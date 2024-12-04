def get_input():
    with open("day_3/input.txt", "r") as f:
        file = f.read().splitlines()

    grid = []
    for line in file:
        grid.append([])
        for chr in line:
            grid[-1].append(chr == "#")

    return grid


def part_one(grid):
    num_trees = 0
    x_pos = 0
    for line in grid:
        if line[x_pos]:
            num_trees += 1
        x_pos += 3
        x_pos %= len(line)

    return num_trees


def part_two(grid):
    slope_product = 1
    for dx, dy in [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]:
        num_trees = 0
        x_pos = 0
        for line in grid[::dy]:
            if line[x_pos]:
                num_trees += 1
            x_pos += dx
            x_pos %= len(line)
        slope_product *= num_trees

    return slope_product


print(part_one(get_input()))
print(part_two(get_input()))
