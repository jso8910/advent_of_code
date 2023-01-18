import collections
import re


def get_input():
    with open("day_7/input.txt", "r") as f:
        file = f.read().splitlines()

    programs = {}
    for line in file:
        program_name = line.split(" ")[0]
        program_weight = int(line.split(" ")[1].strip("()"))
        if " -> " in line:
            program_children = line.split(" -> ")[1].split(", ")
        else:
            program_children = []

        programs[program_name] = {
            "weight": program_weight, "children": program_children}

    return programs


def part_one(programs):
    not_child = list(programs)
    for program in programs:
        for child in programs[program]["children"]:
            if child in programs:
                del not_child[not_child.index(child)]

    return not_child[0]


def get_weight(programs, program):
    tower = [programs[program]["weight"]]
    for child in programs[program]["children"]:
        tower.append(get_weight(programs, child))

    return sum(tower)


def part_two(programs, first_program):
    weights = []
    if not programs[first_program]["children"]:
        return 0
    for child in programs[first_program]["children"]:
        weights.append((child, get_weight(programs, child)))

    for idx, weight in enumerate(weights):
        if [w[1] for w in weights].count(weight[1]) == 1 and len(weights) != 1:
            unbalanced_side = part_two(programs, first_program=weight[0])
            if unbalanced_side != 0:
                return unbalanced_side
            else:
                return programs[weight[0]]["weight"] + weights[idx - 1][1] - weight[1]
    return ([x for x in [part_two(programs, first_program=program) for program in programs[first_program]["children"]] if x != 0] + [0])[0]


print(part_one(get_input()))
print(part_two(get_input(), first_program=part_one(get_input())))
