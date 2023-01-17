from collections import defaultdict


def get_input():
    with open("day_18/input.txt", "r") as f:
        file = f.read()

    grid = defaultdict(bool)
    for x, char in enumerate(file):
        grid[x] = char == "^"

    return grid, len(file)


def part_one(grid, len_row):
    for i in range(1, 40):
        for idx in range(len_row):
            is_trap = False
            to_comp = [grid[(i - 1)*1j + idx - 1], grid[(i - 1)
                                                        * 1j + idx], grid[(i - 1)*1j + idx + 1]]
            if to_comp in [[True, True, False], [False, True, True], [True, False, False], [False, False, True]]:
                is_trap = True

            grid[idx + i*1j] = is_trap

    return sum(not v for coords, v in grid.items() if 0 <= coords.real < len_row)


def part_two(grid, len_row):
    for i in range(1, 400_000):
        for idx in range(len_row):
            is_trap = False
            to_comp = [grid[(i - 1)*1j + idx - 1], grid[(i - 1)
                                                        * 1j + idx], grid[(i - 1)*1j + idx + 1]]
            if to_comp in [[True, True, False], [False, True, True], [True, False, False], [False, False, True]]:
                is_trap = True

            grid[idx + i*1j] = is_trap

    return sum(not v for coords, v in grid.items() if 0 <= coords.real < len_row)


print(part_one(*get_input()))
print(part_two(*get_input()))
