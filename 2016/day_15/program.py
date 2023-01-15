import re


def get_input():
    with open("day_15/input.txt", "r") as f:
        file = f.read().splitlines()

    discs = {}
    prog = re.compile(
        r"Disc #(\d+) has (\d+) positions; at time=0, it is at position (\d+).")
    for line in file:
        m = prog.match(line)
        discs[int(m.group(1))] = (int(m.group(2)), int(m.group(3)))

    return discs


def part_one(discs):
    i = 0
    while True:
        if all((discs[k][1] + i + k) % discs[k][0] == 0 for k in discs):
            return i
        i += 1


def part_two(discs):
    discs[max(discs.keys()) + 1] = (11, 0)
    i = 0
    while True:
        if all((discs[k][1] + i + k) % discs[k][0] == 0 for k in discs):
            return i
        i += 1


print(part_one(get_input()))
print(part_two(get_input()))
