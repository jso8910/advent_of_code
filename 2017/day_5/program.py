def get_input():
    with open("day_5/input.txt", "r") as f:
        return list(map(int, f.read().splitlines()))


def part_one(instructions):
    steps = 0
    i = 0
    while i < len(instructions):
        steps += 1
        jump = instructions[i]
        instructions[i] += 1
        i += jump
    return steps


def part_two(instructions):
    steps = 0
    i = 0
    while i < len(instructions):
        steps += 1
        jump = instructions[i]
        instructions[i] += 1 if jump < 3 else -1
        i += jump
    return steps


print(part_one(get_input()))
print(part_two(get_input()))
