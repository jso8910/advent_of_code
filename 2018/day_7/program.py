import sys
from collections import defaultdict


def get_input():
    with open("day_7/input.txt", "r") as f:
        file = f.read().splitlines()

    requirements = {letter: set() for letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"}
    # requirements = {letter: set() for letter in "ABCDEF"}
    for line in file:
        requirements[line.split(" ")[-3]].add(line.split(" ")[1])

    return requirements


def part_one(requirements):
    order = ""
    while len(order) != len(requirements):
        to_do = sorted(
            [r for r in requirements if requirements[r] == set() and r not in order])[0]
        order += to_do
        for r in [r for r in requirements if r not in order]:
            requirements[r] -= set(to_do)

    return order


def part_two(requirements):
    order = ""
    elves_time = [0 for _ in range(5)]
    elves_working_on = ["" for _ in range(5)]
    time = 0
    while len(order) != len(requirements):
        for idx, elf_time, elf_working_on in zip(range(5), elves_time, elves_working_on):
            if elf_time > 0:
                elves_time[idx] -= 1
            else:
                order += elf_working_on
                elves_time[idx] -= 1
                for r in [r for r in requirements if r not in order]:
                    requirements[r] -= set(elf_working_on)
        for idx, elf_time, elf_working_on in zip(range(5), elves_time, elves_working_on):
            if elf_time < 0:
                to_do = sorted(
                    [r for r in requirements if requirements[r] == set() and r not in order and r not in elves_working_on])
                if to_do:
                    to_do = to_do[0]
                    elves_working_on[idx] = to_do
                    elves_time[idx] = 60 + ord(to_do) - ord("A")
                else:
                    elves_working_on[idx] = ""
        time += 1

    return time - 1


print(part_one(get_input()))
print(part_two(get_input()))
