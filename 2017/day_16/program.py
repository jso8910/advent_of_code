from collections import deque
from tqdm import tqdm


def get_input():
    with open("day_16/input.txt", "r") as f:
        file = f.read().split(",")

    instructions = []
    for chars in file:
        match chars[0]:
            case "s":
                instructions.append(("spin", int(chars[1:])))
            case "x":
                instructions.append(
                    ("exchange", int(chars[1:].split("/")[0]), int(chars[1:].split("/")[1])))
            case "p":
                instructions.append(
                    ("partner", chars[1:].split("/")[0], chars[1:].split("/")[1]))

    return instructions


def part_one(instructions):
    programs = deque(char for char in "abcdefghijklmnop")
    assert len(programs) == 16
    for instruction in instructions:
        match instruction:
            case ("spin", x):
                programs.rotate(x)
            case ("exchange", a, b):
                programs[a], programs[b] = programs[b], programs[a]
            case ("partner", a, b):
                a_idx = programs.index(a)
                b_idx = programs.index(b)
                programs[a_idx], programs[b_idx] = programs[b_idx], programs[a_idx]

    return "".join(programs)


def part_two(instructions):
    programs = deque(char for char in "abcdefghijklmnop")
    assert len(programs) == 16
    cache = {0: list(programs)}
    i = 1
    while i <= 1_000_000_000:
        for instruction in instructions:
            match instruction:
                case ("spin", x):
                    programs.rotate(x)
                case ("exchange", a, b):
                    programs[a], programs[b] = programs[b], programs[a]
                case ("partner", a, b):
                    a_idx = programs.index(a)
                    b_idx = programs.index(b)
                    programs[a_idx], programs[b_idx] = programs[b_idx], programs[a_idx]
        if list(programs) in cache.values():
            if (1_000_000_000 // i) * i < 1_000_000_000:
                i = max(i, (1_000_000_000 // i) * i)
            cache = {}

        cache[i] = list(programs)
        i += 1

    return "".join(programs)


print(part_one(get_input()))
print(part_two(get_input()))
