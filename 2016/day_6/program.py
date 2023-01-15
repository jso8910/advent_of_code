def get_input():
    with open("day_6/input.txt", "r") as f:
        return [[c for c in l] for l in f.read().splitlines()]


def part_one(message):
    columns = list(zip(*message))
    return "".join([max(c, key=c.count) for c in columns])


def part_two(message):
    columns = list(zip(*message))
    return "".join([min(c, key=c.count) for c in columns])


print(part_one(get_input()))
print(part_two(get_input()))
