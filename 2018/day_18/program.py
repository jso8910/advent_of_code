from pprint import pprint
from copy import deepcopy
from enum import Enum
from collections import defaultdict, Counter


class Acre(Enum):
    OPEN = "."
    TREES = "|"
    LUMBERYARD = "#"

    @classmethod
    def _missing_(cls, value):
        return cls.OPEN

    def __repr__(self):
        return self.value

    def __str__(self):
        return self.value


def get_input():
    with open("day_18/input.txt", "r") as f:
        file = f.read().splitlines()

    grid = defaultdict(lambda: Acre.OPEN)
    for ridx, row in enumerate(file):
        for cidx, chr in enumerate(row):
            grid[cidx + ridx*1j] = Acre(chr)

    return grid


def part_one(grid):
    for minute in range(10):
        new_grid = deepcopy(grid)
        for coord, val in list(grid.items()):
            if max(coord.imag, coord.real) > 50:
                continue
            neighbors = []
            for d in [1, -1, 1j, -1j, 1+1j, 1-1j, -1+1j, -1-1j]:
                neighbors.append(grid[coord + d])
            neighbor_c = Counter(neighbors)
            if val == Acre.OPEN and neighbor_c[Acre.TREES] >= 3:
                new_grid[coord] = Acre.TREES
            elif val == Acre.TREES and neighbor_c[Acre.LUMBERYARD] >= 3:
                new_grid[coord] = Acre.LUMBERYARD
            elif val == Acre.LUMBERYARD and not (neighbor_c[Acre.TREES] >= 1 and neighbor_c[Acre.LUMBERYARD] >= 1):
                new_grid[coord] = Acre.OPEN
        grid = new_grid

    c = Counter(grid.values())
    return c[Acre.LUMBERYARD] * c[Acre.TREES]


def part_two(grid):
    cache = {str(grid): 0}
    minute = 1
    while minute <= 1_000_000_000:
        new_grid = deepcopy(grid)
        for coord, val in list(grid.items()):
            if max(coord.imag, coord.real) > 50:
                continue
            neighbors = []
            for d in [1, -1, 1j, -1j, 1+1j, 1-1j, -1+1j, -1-1j]:
                neighbors.append(grid[coord + d])
            neighbor_c = Counter(neighbors)
            if val == Acre.OPEN and neighbor_c[Acre.TREES] >= 3:
                new_grid[coord] = Acre.TREES
            elif val == Acre.TREES and neighbor_c[Acre.LUMBERYARD] >= 3:
                new_grid[coord] = Acre.LUMBERYARD
            elif val == Acre.LUMBERYARD and not (neighbor_c[Acre.TREES] >= 1 and neighbor_c[Acre.LUMBERYARD] >= 1):
                new_grid[coord] = Acre.OPEN
        grid = new_grid
        c = Counter(grid.values())
        resource = c[Acre.LUMBERYARD] * c[Acre.TREES]
        if str(grid) in cache:
            cycle_start = cache[str(grid)]
            cycle_end = minute
            period = cycle_end - cycle_start
            cycle_containing = 1_000_000_000 - cycle_start
            num_minutes = cycle_start + cycle_containing % period
            for key, value in cache.items():
                if value == num_minutes:
                    c = Counter(key)
                    return c[Acre.LUMBERYARD.value] * c[Acre.TREES.value]

        cache[str(grid)] = minute
        minute += 1
    c = Counter(grid.values())
    return c[Acre.LUMBERYARD] * c[Acre.TREES]


print(part_one(get_input()))
print(part_two(get_input()))
