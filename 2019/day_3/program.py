from collections import defaultdict


def get_input():
    with open("day_3/input.txt", "r") as f:
        file = f.read().splitlines()

    wires = []
    dirs = {
        "U": -1j,
        "D": 1j,
        "L": -1,
        "R": 1
    }
    for wire in file:
        wires.append([])
        for thing in wire.split(","):
            wires[-1].append((dirs[thing[0]], int(thing[1:])))

    return wires


def manhattan(a: int, b=0):
    return abs(a.real - b.real) + abs(a.imag - b.imag)


def part_one(wires):
    wire_1 = defaultdict(bool)
    wire_2 = defaultdict(bool)
    current_point = 0
    for thing in wires[0]:
        for i in range(thing[1]):
            current_point += thing[0]
            wire_1[current_point] = True
    current_point = 0
    for thing in wires[1]:
        for i in range(thing[1]):
            current_point += thing[0]
            wire_2[current_point] = True

    min_dist = float("inf")
    for point in wire_1:
        if wire_1[point] and wire_2[point]:
            min_dist = min(manhattan(point), min_dist)

    return int(min_dist)


def part_two(wires):
    wire_1 = defaultdict(int)
    wire_2 = defaultdict(int)
    current_point = 0
    num_steps = 0
    for thing in wires[0]:
        for i in range(thing[1]):
            num_steps += 1
            current_point += thing[0]
            wire_1[current_point] = num_steps
    current_point = 0
    num_steps = 0
    for thing in wires[1]:
        for i in range(thing[1]):
            num_steps += 1
            current_point += thing[0]
            wire_2[current_point] = num_steps

    min_steps = float("inf")
    for point in wire_1:
        if wire_1[point] and wire_2[point]:
            min_steps = min(wire_1[point] + wire_2[point], min_steps)

    return int(min_steps)


print(part_one(get_input()))
print(part_two(get_input()))
