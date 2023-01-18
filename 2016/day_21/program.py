from itertools import permutations
import re
from collections import deque
from itertools import islice


def get_input():
    with open("day_21/input.txt", "r") as f:
        file = f.read().splitlines()

    instructions = []
    for line in file:
        match line.split(" "):
            case ["swap", "position", x, "with", "position", y]:
                instructions.append(("swap_pos", int(x), int(y)))
            case ["swap", "letter", x, "with", "letter", y]:
                instructions.append(("swap_let", x, y))
            case ["rotate", dir, x, "steps" | "step"]:
                instructions.append(("rotate_steps", dir, int(x)))
            case ["rotate", "based", "on", "position", "of", "letter", x]:
                instructions.append(("rotate_pos", x))
            case ["reverse", "positions", x, "through", y]:
                instructions.append(("reverse", int(x), int(y)))
            case ["move", "position", x, "to", "position", y]:
                instructions.append(("move", int(x), int(y)))

    return instructions


def part_one(instructions, pwd="abcdefgh"):
    password = deque(pwd)
    for instruction in instructions:
        match instruction:
            case ("swap_pos", x, y):
                password[x], password[y] = password[y], password[x]
            case ("swap_let", x, y):
                # NOTE: Why doesn't the following commented line work?
                # password[password.index(x)], password[password.index(
                #     y)] = password[password.index(y)], password[password.index(x)]
                password = deque("".join(password).replace(x, "X").replace(
                    y, "Y").replace("X", y).replace("Y", x))
            case ("rotate_steps", "left", x):
                password.rotate(-x)
            case ("rotate_steps", "right", x):
                password.rotate(x)
            case ("rotate_pos", x):
                to_rot = password.index(x) + 1
                if to_rot - 1 >= 4:
                    to_rot += 1
                password.rotate(to_rot)
            case ("reverse", x, y):
                rev = reversed([d for d in islice(password, x, y + 1)])
                for i, let in enumerate(rev):
                    password[x + i] = let
            case ("move", x, y):
                password.rotate(-x)
                let = password.popleft()
                password.rotate(x)
                password.insert(y, let)
    return "".join(password)


def part_two(instructions):
    for new_password in permutations("fbgdceah"):
        if part_one(instructions, pwd=new_password) == "fbgdceah":
            return "".join(new_password)


print(part_one(get_input()))
print(part_two(get_input()))
