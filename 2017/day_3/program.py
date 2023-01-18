from collections import defaultdict
from math import sqrt, ceil
from itertools import cycle


def get_input():
    with open("day_3/input.txt", "r") as f:
        return int(f.read())


def part_one(num):
    x, y = 0, 0
    size = 1
    n = 1
    moves = [lambda x, y: (x + 1, y), lambda x, y: (x, y - 1),
             lambda x, y: (x-1, y), lambda x, y: (x, y + 1)]
    move_idx = 0
    while True:
        for _ in range(2):
            move = moves[move_idx]
            for _ in range(size):
                x, y = move(x, y)
                n += 1
                if n == num:
                    return abs(x) + abs(y)
            move_idx += 1
            move_idx %= 4
        size += 1


def part_two(num):
    x, y = 0, 0
    grid = defaultdict(int)
    grid[(0, 0)] = 1
    size = 1
    n = 1
    moves = [lambda x, y: (x + 1, y), lambda x, y: (x, y - 1),
             lambda x, y: (x-1, y), lambda x, y: (x, y + 1)]
    move_idx = 0
    while True:
        for _ in range(2):
            move = moves[move_idx]
            for _ in range(size):
                x, y = move(x, y)
                n = sum(grid[(x + dx, y + dy)]
                        for dx in range(-1, 2) for dy in range(-1, 2))
                grid[(x, y)] = n
                if n >= num:
                    return n
            move_idx += 1
            move_idx %= 4
        size += 1


print(part_one(get_input()))
print(part_two(get_input()))
