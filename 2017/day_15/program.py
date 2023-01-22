def get_input():
    with open("day_15/input.txt", "r") as f:
        return map(lambda line: int(line.split(" ")[-1]), f.read().splitlines())


def generator(N, C, M=1):
    while True:
        N = (N * C) % 2147483647
        if N % M == 0:
            yield N & 0xffff


def part_one(a, b):
    gen_a = generator(a, 16807)
    gen_b = generator(b, 48271)
    count = 0
    for i in range(40_000_000):
        if next(gen_a) == next(gen_b):
            count += 1
    return count


def part_two(a, b):
    gen_a = generator(a, 16807, M=4)
    gen_b = generator(b, 48271, M=8)
    count = 0
    for i in range(5_000_000):
        if next(gen_a) == next(gen_b):
            count += 1
    return count


print(part_one(*get_input()))
print(part_two(*get_input()))
