import re


def get_input():
    with open("day_03/input.txt", "r") as f:
        return f.read()


def part_one(inp):
    total = 0
    for match in re.finditer(r"mul\((\d+),(\d+)\)", inp):
        total += int(match.group(1)) * int(match.group(2))
    return total


def part_two(inp):
    total = 0
    enabled = True
    for match in re.finditer(r"mul\((\d+),(\d+)\)|(do(?:n't)?\(\))", inp):
        if match.group(3) == "don't()":
            enabled = False
        elif match.group(3) == "do()":
            enabled = True
        elif enabled:
            total += int(match.group(1)) * int(match.group(2))
    return total


print(part_one(get_input()))
print(part_two(get_input()))
