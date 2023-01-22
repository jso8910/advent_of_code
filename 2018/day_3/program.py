from collections import defaultdict


def get_input():
    with open("day_3/input.txt", "r") as f:
        file = f.read().splitlines()

    claims = []
    for line in file:
        top_left = tuple(
            map(int, line.split(" @ ")[1].split(":")[0].split(",")))
        size = tuple(map(int, line.split(": ")[1].split("x")))
        range_x = range(top_left[0], top_left[0] + size[0])
        range_y = range(top_left[1], top_left[1] + size[1])
        claims.append((range_x, range_y))

    return claims


def part_one(claims):
    fabric = defaultdict(int)
    for claim in claims:
        for x in claim[0]:
            for y in claim[1]:
                fabric[(x, y)] += 1

    return sum(1 for x in fabric.values() if x > 1)


def part_two(claims):
    fabric = defaultdict(int)
    for idx, claim in enumerate(claims):
        for x in claim[0]:
            for y in claim[1]:
                fabric[(x, y)] += 1
    for idx, claim in enumerate(claims):
        claim_overlapping = False
        for x in claim[0]:
            for y in claim[1]:
                if fabric[(x, y)] > 1:
                    claim_overlapping = True
        if not claim_overlapping:
            return idx + 1


print(part_one(get_input()))
print(part_two(get_input()))
