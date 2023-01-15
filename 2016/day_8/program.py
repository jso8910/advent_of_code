from copy import deepcopy
from collections import deque


def get_input():
    with open("day_8/input.txt", "r") as f:
        file = f.read().splitlines()

    instructions = []
    for line in file:
        instruction = {}
        match line.replace("=", " ").split(" "):
            case ["rect", dims]:
                instruction["type"] = "rect"
                instruction["x"] = int(dims.split('x')[0])
                instruction["y"] = int(dims.split('x')[1])
            case ["rotate", "row", "y", row, "by", amount]:
                instruction["type"] = "rotate_row"
                instruction["row"] = int(row)
                instruction["amount"] = int(amount)
            case ["rotate", "column", "x", col, "by", amount]:
                instruction["type"] = "rotate_col"
                instruction["col"] = int(col)
                instruction["amount"] = int(amount)
        instructions.append(instruction)

    return instructions


def transpose(lst):
    return list(map(deque, zip(*lst)))


def part_one(instructions):
    grid = [deque([0 for _ in range(50)]) for _ in range(6)]
    for instruction in instructions:
        match instruction:
            case {"type": "rect", "x": x, "y": y}:
                for row in range(y):
                    for col in range(x):
                        grid[row][col] = 1
            case {"type": "rotate_row", "row": row, "amount": amount}:
                old_grid = deepcopy(grid)
                grid[row].rotate(amount)
            case {"type": "rotate_col", "col": col, "amount": amount}:
                grid_by_cols = transpose(grid)
                grid_by_cols[col].rotate(amount)
                grid = transpose(grid_by_cols)
    return sum(sum(row) for row in grid)


def part_two(instructions):
    grid = [deque([0 for _ in range(50)]) for _ in range(6)]
    for instruction in instructions:
        match instruction:
            case {"type": "rect", "x": x, "y": y}:
                for row in range(y):
                    for col in range(x):
                        grid[row][col] = 1
            case {"type": "rotate_row", "row": row, "amount": amount}:
                old_grid = deepcopy(grid)
                grid[row].rotate(amount)
            case {"type": "rotate_col", "col": col, "amount": amount}:
                grid_by_cols = transpose(grid)
                grid_by_cols[col].rotate(amount)
                grid = transpose(grid_by_cols)
    for row in grid:
        for char in row:
            if char == 1:
                print("#", end="")
            else:
                print(" ", end="")
        print()


print(part_one(get_input()))
part_two(get_input())
