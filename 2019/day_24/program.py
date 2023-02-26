from collections import defaultdict


def get_input():
    with open("day_24/input.txt", "r") as f:
        file = f.read().splitlines()

    grid = {}
    for ridx, line in enumerate(file):
        for cidx, chr in enumerate(line):
            grid[cidx + ridx * 1j] = chr == "#"

    return grid


def part_one(grid):
    states = set()
    while True:
        score = 0
        for pos in grid:
            exponent = int(pos.real) + int(pos.imag) * \
                int(max(p.real for p in grid) + 1)
            score += grid[pos] * 2**exponent
        if score in states:
            return score
        states.add(score)
        new_grid = {}
        for pos in grid:
            num_bugs = 0
            for dc in [-1, 1, -1j, 1j]:
                if pos + dc not in grid:
                    continue
                num_bugs += grid[pos + dc]
            if grid[pos] and num_bugs == 1:
                new_grid[pos] = True
            elif grid[pos] and num_bugs != 1:
                new_grid[pos] = False
            elif not grid[pos] and num_bugs in (1, 2):
                new_grid[pos] = True
            elif not grid[pos] and num_bugs not in (1, 2):
                new_grid[pos] = False
        grid = new_grid.copy()


def part_two(grid):
    LEFT_EDGE = [0, 1j, 2j, 3j, 4j]
    RIGHT_EDGE = [4, 4+1j, 4+2j, 4+3j, 4+4j]
    TOP_EDGE = [0, 1, 2, 3, 4]
    BOTTOM_EDGE = [4j, 1+4j, 2+4j, 3+4j, 4+4j]
    DIR_TO_EDGE = {
        -1: RIGHT_EDGE,
        1: LEFT_EDGE,
        -1j: BOTTOM_EDGE,
        1j: TOP_EDGE
    }
    empty_grid = {g: False for g in grid}
    grid_levels = defaultdict(lambda: empty_grid)
    grid_levels[0] = grid
    for i in range(200):
        new_grid_levels = defaultdict(lambda: empty_grid)
        for level in range(min(grid_levels) - 1, max(grid_levels) + 2):
            new_grid = {}
            for pos in grid_levels[level]:
                num_bugs = 0
                if pos == 2 + 2j:
                    continue
                for dc in [-1, 1, -1j, 1j]:
                    if pos + dc == 2 + 2j:
                        num_bugs += sum(grid_levels[level + 1][c]
                                        for c in DIR_TO_EDGE[dc])
                    elif (pos + dc).real == 5:
                        num_bugs += grid_levels[level - 1][3 + 2j]
                    elif (pos + dc).real == -1:
                        num_bugs += grid_levels[level - 1][1 + 2j]
                    elif (pos + dc).imag == 5:
                        num_bugs += grid_levels[level - 1][2 + 3j]
                    elif (pos + dc).imag == -1:
                        num_bugs += grid_levels[level - 1][2 + 1j]
                    else:
                        num_bugs += grid_levels[level][pos + dc]
                if grid_levels[level][pos] and num_bugs == 1:
                    new_grid[pos] = True
                elif grid_levels[level][pos] and num_bugs != 1:
                    new_grid[pos] = False
                elif not grid_levels[level][pos] and num_bugs in (1, 2):
                    new_grid[pos] = True
                elif not grid_levels[level][pos] and num_bugs not in (1, 2):
                    new_grid[pos] = False
            new_grid_levels[level] = new_grid.copy()
        grid_levels = new_grid_levels.copy()

    ret = 0
    for l in grid_levels:
        ret += sum(grid_levels[l].values())

    return ret


print(part_one(get_input()))
print(part_two(get_input()))
