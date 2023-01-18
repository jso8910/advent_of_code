from itertools import permutations


def get_input():
    with open("day_2/input.txt", "r") as f:
        return list(map(lambda x: list(map(int, x.split())), f.read().splitlines()))


def part_one(number_grid):
    checksum = 0
    for row in number_grid:
        checksum += max(row) - min(row)
    return checksum


def part_two(number_grid):
    checksum = 0
    for row in number_grid:
        for perm in permutations(row, 2):
            if perm[0] % perm[1] == 0:
                checksum += perm[0] // perm[1]
                break
    return checksum


print(part_one(get_input()))
print(part_two(get_input()))
