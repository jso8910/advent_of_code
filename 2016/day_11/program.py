import re
from copy import deepcopy
from itertools import product


def get_input():
    with open("day_11/input.txt", "r") as f:
        file = f.read().splitlines()

    floors = []
    for line in file:
        generators = [x.group(1) for x in re.finditer("(\w+) generator", line)]
        microchips = [x.group(1) for x in re.finditer(
            "(\w+)-compatible microchip", line)]
        floors.append({"generators": generators,
                      "microchips": microchips, "elevator": False})

    floors[0]["elevator"] = True

    return floors


def find_pair(array, element):
    ret = []
    for i, x in enumerate(array):
        for j, y in enumerate(x["microchips"] + x["generators"]):
            if y == element:
                ret.append(i)

    return tuple(ret)


def get_next_states(floors):
    states = []
    double_move_upstairs_states = []
    single_move_upstairs_states = []
    double_move_downstairs_states = []
    single_move_downstairs_states = []
    idx = sorted(
        range(4), key=lambda i: floors[i]["elevator"], reverse=True)[0]
    floor = floors[idx]
    for dest_floor in range(idx - 1, idx + 2):
        if dest_floor < 0 or dest_floor > 3 or dest_floor == idx:
            continue
        for item1, item2 in product(floor["generators"], floor["microchips"]):
            if item1 != item2:
                continue
            new_floors = deepcopy(floors)
            new_floors[idx]["generators"].remove(item1)
            new_floors[idx]["microchips"].remove(item2)
            new_floors[dest_floor]["generators"].append(item1)
            new_floors[dest_floor]["microchips"].append(item2)
            new_floors[idx]["elevator"] = False
            new_floors[dest_floor]["elevator"] = True
            if all([all([x in new_floors[i]["generators"] or not new_floors[i]["generators"] for x in new_floors[i]["microchips"]]) for i in range(4)]):
                if idx - dest_floor < 0:
                    double_move_upstairs_states.append(
                        (new_floors, {item1, item2}, dest_floor - idx))
                else:
                    double_move_downstairs_states.append(
                        (new_floors, {item1, item2}, dest_floor - idx))
    for dest_floor in range(idx - 1, idx + 2):
        if dest_floor < 0 or dest_floor > 3 or dest_floor == idx:
            continue
        for item1, item2 in product(floor["generators"], floor["generators"]):
            if item1 == item2:
                continue
            new_floors = deepcopy(floors)
            new_floors[idx]["generators"].remove(item1)
            new_floors[idx]["generators"].remove(item2)
            new_floors[dest_floor]["generators"].append(item1)
            new_floors[dest_floor]["generators"].append(item2)
            new_floors[idx]["elevator"] = False
            new_floors[dest_floor]["elevator"] = True
            if all([all([x in new_floors[i]["generators"] or not new_floors[i]["generators"] for x in new_floors[i]["microchips"]]) for i in range(4)]):
                if idx - dest_floor < 0:
                    double_move_upstairs_states.append(
                        (new_floors, {item1, item2}, dest_floor - idx))
                else:
                    double_move_downstairs_states.append(
                        (new_floors, {item1, item2}, dest_floor - idx))
    for dest_floor in range(idx - 1, idx + 2):
        if dest_floor < 0 or dest_floor > 3 or dest_floor == idx:
            continue
        for item1, item2 in product(floor["microchips"], floor["microchips"]):
            if item1 == item2:
                continue
            new_floors = deepcopy(floors)
            new_floors[idx]["microchips"].remove(item1)
            new_floors[idx]["microchips"].remove(item2)
            new_floors[dest_floor]["microchips"].append(item1)
            new_floors[dest_floor]["microchips"].append(item2)
            new_floors[idx]["elevator"] = False
            new_floors[dest_floor]["elevator"] = True
            if all([all([x in new_floors[i]["generators"] or not new_floors[i]["generators"] for x in new_floors[i]["microchips"]]) for i in range(4)]):
                if idx - dest_floor < 0:
                    double_move_upstairs_states.append(
                        (new_floors, {item1, item2}, dest_floor - idx))
                else:
                    double_move_downstairs_states.append(
                        (new_floors, {item1, item2}, dest_floor - idx))
    for dest_floor in range(idx - 1, idx + 2):
        if dest_floor < 0 or dest_floor > 3 or dest_floor == idx:
            continue
        for item in floor["generators"]:
            new_floors = deepcopy(floors)
            new_floors[idx]["generators"].remove(item)
            new_floors[dest_floor]["generators"].append(item)
            new_floors[idx]["elevator"] = False
            new_floors[dest_floor]["elevator"] = True
            if all([all([x in new_floors[i]["generators"] or not new_floors[i]["generators"] for x in new_floors[i]["microchips"]]) for i in range(4)]):
                if idx - dest_floor < 0:
                    single_move_upstairs_states.append(
                        (new_floors, {item}, dest_floor - idx))
                else:
                    single_move_downstairs_states.append(
                        (new_floors, {item}, dest_floor - idx))
    for dest_floor in range(idx - 1, idx + 2):
        if dest_floor < 0 or dest_floor > 3 or dest_floor == idx:
            continue
        for item in floor["microchips"]:
            new_floors = deepcopy(floors)
            new_floors[idx]["microchips"].remove(item)
            new_floors[dest_floor]["microchips"].append(item)
            new_floors[idx]["elevator"] = False
            new_floors[dest_floor]["elevator"] = True
            if all([all([x in new_floors[i]["generators"] or not new_floors[i]["generators"] for x in new_floors[i]["microchips"]]) for i in range(4)]):
                if idx - dest_floor < 0:
                    single_move_upstairs_states.append(
                        (new_floors, (item), dest_floor - idx))
                else:
                    single_move_downstairs_states.append(
                        (new_floors, (item), dest_floor - idx))
    if all(len(floor["generators"] + floor["microchips"]) == 0 for floor in floors[:idx]):
        single_move_downstairs_states = []
        double_move_downstairs_states = []
    states = (double_move_upstairs_states if double_move_upstairs_states else single_move_upstairs_states) + \
        (single_move_downstairs_states if single_move_downstairs_states else double_move_downstairs_states)
    return states


def part_one(floors):
    pairs = {x for i in range(4) for x in floors[i]["microchips"]}
    queue = [(deepcopy(floors), 0, None, 0)]
    visited = [deepcopy(floors)]
    visited_pairs_per_floor = [[sum(x in floors[i]["generators"]
                                    for x in floors[i]["microchips"]) for i in range(4)],
                               [{x for x in floors[i]["microchips"]
                                if x not in floors[i]["generators"]} for i in range(4)],
                               [{x for x in floors[i]["generators"]
                                if x not in floors[i]["microchips"]} for i in range(4)],
                               0]
    visited_pairs_per_floor = [({find_pair(floors, x) for x in pairs}, 0)]
    prev_depth = 0
    node = (deepcopy(floors), 0, None, 0)
    while queue:
        node = queue.pop(0)
        if [floor["generators"] + floor["microchips"] for floor in node[0][0:3]] == [[], [], []]:
            return node[1]

        for new_node, moved_item, dir in get_next_states(node[0]):
            prev_depth = node[1]
            pairs_per_floor = (sorted([find_pair(new_node, x) for x in pairs]), sorted(
                range(4), key=lambda i: new_node[i]["elevator"], reverse=True)[0])
            if dir * -1 == node[2] and moved_item == node[3]:
                continue
            if pairs_per_floor not in visited_pairs_per_floor:
                visited.append(new_node)
                visited_pairs_per_floor.append(pairs_per_floor)
                queue.append((new_node, node[1] + 1, dir, moved_item))


def part_two(floors):
    floors[0]["microchips"].append("elerium")
    floors[0]["generators"].append("elerium")
    floors[0]["microchips"].append("dilithium")
    floors[0]["generators"].append("dilithium")
    pairs = {x for i in range(4) for x in floors[i]["microchips"]}
    queue = [(deepcopy(floors), 0, 0, 0)]
    visited = [deepcopy(floors)]
    visited_pairs_per_floor = [({find_pair(floors, x) for x in pairs}, 0)]
    prev_depth = 0
    node = (deepcopy(floors), 0, 0, 0)
    while queue:
        node = queue.pop(0)
        if [floor["generators"] + floor["microchips"] for floor in node[0][0:3]] == [[], [], []]:
            return node[1]

        for new_node, moved_item, dir in get_next_states(node[0]):
            prev_depth = max([prev_depth, node[1]])
            pairs_per_floor = (sorted([find_pair(new_node, x) for x in pairs]), sorted(
                range(4), key=lambda i: new_node[i]["elevator"], reverse=True)[0])
            if dir * -1 == node[2] and moved_item == node[3]:
                continue
            if pairs_per_floor not in visited_pairs_per_floor:
                visited_pairs_per_floor.append(pairs_per_floor)
                queue.append((new_node, node[1] + 1, dir, moved_item))


print(part_one(get_input()))
print(part_two(get_input()))
