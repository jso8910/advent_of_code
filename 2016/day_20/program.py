import collections
import sys
from itertools import islice


def get_input():
    with open("day_20/input.txt", "r") as f:
        file = f.read().splitlines()
    return [tuple(map(int, line.split("-"))) for line in file]


def part_one(ranges):
    ranges = sorted(ranges, key=lambda x: x[0])
    # print(ranges)
    iter = ranges.__iter__()
    current_range = next(iter)
    num = 0
    while num < 2**32:
        if num > current_range[1]:
            next_range = next(iter)
            if num < next_range[0]:
                return num
            else:
                current_range = next_range
                num = current_range[1]
        num += 1


def part_two(ranges):
    ranges = sorted(ranges, key=lambda x: x[0])
    iter = ranges.__iter__()
    current_range = next(iter)
    num = 0
    count = 0
    index = 0
    while num < 2**32:
        current_range = ranges[index]
        if num >= current_range[0]:
            if num <= current_range[1]:
                num = current_range[1] + 1
                continue
            index += 1
        else:
            count += 1
            num += 1

    return count


print(part_one(get_input()))
print(part_two(get_input()))
