from collections import deque


def get_input():
    with open("day_17/input.txt", "r") as f:
        return int(f.read())


def part_one(steps):
    buffer = deque([0])
    for i in range(1, 2017 + 1):
        buffer.rotate(-steps - 1)
        buffer.appendleft(i)

    return buffer[buffer.index(2017) + 1]


def part_two(steps):
    buffer = deque([0])
    for i in range(1, 50_000_000 + 1):
        if i % 10_000 == 0:
            print(i)
        buffer.rotate(-steps - 1)
        buffer.appendleft(i)

    return buffer[buffer.index(0) + 1]


print(part_one(get_input()))
print(part_two(get_input()))
