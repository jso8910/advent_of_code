from collections import Counter


def get_input():
    with open("day_01/input.txt") as f:
        file = f.readlines()
        x = []
        y = []
        for line in file:
            x.append(int(line.split()[0]))
            y.append(int(line.split()[1]))
        return x, y


def part_one(inp):
    x = sorted(inp[0])
    y = sorted(inp[1])
    return sum(abs(a[1] - a[0]) for a in zip(x, y))


def part_two(inp):
    c = Counter(inp[1])
    score = 0
    for i in inp[0]:
        score += c[i] * i
    return score


print(part_one(get_input()))
print(part_two(get_input()))
