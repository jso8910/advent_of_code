from copy import deepcopy
from collections import deque


def get_input():
    with open("day_15/input.txt", "r") as f:
        file = f.read().splitlines()

    goblins = []
    elves = []
    grid_blocked_squares = []
    for idx, row in enumerate(file):
        for col_idx, char in enumerate(row):
            if char == "#":
                grid_blocked_squares.append((col_idx, idx))
            elif char == "G":
                goblins.append({"type": "goblin", "loc": (
                    col_idx, idx), "hp": 200, "attack": 3})
            elif char == "E":
                elves.append({"type": "elf", "loc": (
                    col_idx, idx), "hp": 200, "attack": 3})

    return grid_blocked_squares, goblins, elves


def shortest_paths(grid_blocked_squares, start, end, elves, goblins):
    paths = []
    visited = set([start])
    min_len_path = float("inf")
    queue = deque([([start], 0)])
    while queue:
        node = queue.popleft()
        if node[0][-1] == end:
            if node[1] > min_len_path:
                # Don't include the start node
                return [(p[0][1], p[1], end) for p in paths]
            paths.append(node)
            min_len_path = node[1]
            continue

        for dx, dy in [(0, -1), (-1, 0), (1, 0), (0, 1)]:
            new_point = (node[0][-1][0] + dx, node[0][-1][1] + dy)
            if new_point not in visited and new_point not in grid_blocked_squares:
                visited.add(new_point)
                queue.append((node[0] + [new_point], node[1] + 1))

    return [(p[0][1], p[1], end) for p in paths]

# TODO: figure out why the code is so slow lol


def part_one(grid_blocked_squares, goblins, elves):
    num_rounds = 0
    while True:
        for_finished = False
        for making_move in sorted(elves + goblins, key=lambda x: (x["loc"][1], x["loc"][0])):
            if making_move not in elves and making_move not in goblins:
                continue
            blocked_coords = set([g["loc"] for g in goblins if g != making_move] +
                                 [e["loc"]
                                  for e in elves if e != making_move] + grid_blocked_squares)
            targets = goblins if making_move["type"] == "elf" else elves
            if not targets:
                break

            # Find squares in range of targets
            in_range = []
            for point in targets:
                for dx, dy in [(0, -1), (-1, 0), (1, 0), (0, 1)]:
                    new_point = (point["loc"][0] + dx,
                                 point["loc"][1] + dy)
                    if not new_point in blocked_coords:
                        in_range.append(new_point)

            if making_move["loc"] not in in_range:
                # Move stage of turn
                # Find square to move to
                end_point_shortest_path = None
                first_point_shortest_path = None
                shortest_path_adjacent = None
                shortest_path_len = float("inf")
                best_paths = []
                for ir_point in in_range:
                    shortest_raw = shortest_paths(
                        blocked_coords, making_move["loc"], ir_point, elves, goblins)
                    if shortest_raw:
                        best_paths.extend(shortest_raw)
                # First condition - fewest number of moves away
                if best_paths:
                    min_steps = min([x[1] for x in best_paths])
                    best_paths = [x for x in best_paths if x[1] == min_steps]

                    # Second condition - if tie, choose the final tile in reading order
                    best_paths.sort(key=lambda x: (x[2][1], x[2][0]))
                    best_paths = [x for x in best_paths if x[2]
                                  == best_paths[0][2]]

                    # Third condition - if tie, take the first step in reading order
                    best_paths.sort(key=lambda x: (x[0][1], x[0][0]))
                    best_paths = [x for x in best_paths if x[0]
                                  == best_paths[0][0]]
                    # Move to that square
                    making_move["loc"] = best_paths[0][0]

            # Attack
            if making_move["loc"] in in_range:
                enemies_in_range = []
                for enemy in targets:
                    for dx, dy in [(0, -1), (-1, 0), (1, 0), (0, 1)]:
                        new_point = (enemy["loc"][0] + dx,
                                     enemy["loc"][1] + dy)
                        if making_move["loc"] == new_point:
                            enemies_in_range.append(enemy)
                            break
                enemies_in_range = sorted(
                    enemies_in_range, key=lambda e: (e["hp"], e["loc"][1], e["loc"][0]))
                enemies_in_range[0]["hp"] -= making_move["attack"]
                if enemies_in_range[0]["hp"] <= 0:
                    if enemies_in_range[0]["type"] == "goblin":
                        goblins.remove(enemies_in_range[0])
                    else:
                        elves.remove(enemies_in_range[0])
        else:
            for_finished = True
            if len(goblins) == 0 or len(elves) == 0:
                return num_rounds * (sum(g["hp"] for g in goblins) + sum(e["hp"] for e in elves))
            num_rounds += 1
        if not for_finished:
            if len(goblins) == 0 or len(elves) == 0:
                return num_rounds * (sum(g["hp"] for g in goblins) + sum(e["hp"] for e in elves))


def part_two(grid_blocked_squares, goblins, elves):
    goblins_og = deepcopy(goblins)
    elves_og = deepcopy(elves)
    elves_killed = float("inf")
    elf_damage = 0
    while elves_killed:
        elves_killed = False
        elf_damage += 1
        num_rounds = 0
        goblins = deepcopy(goblins_og)
        elves = deepcopy(elves_og)
        for elf in elves:
            elf["attack"] = elf_damage
        while not elves_killed:
            for_finished = False
            for making_move in sorted(elves + goblins, key=lambda x: (x["loc"][1], x["loc"][0])):
                if making_move not in elves and making_move not in goblins:
                    continue
                blocked_coords = set([g["loc"] for g in goblins if g != making_move] +
                                     [e["loc"]
                                     for e in elves if e != making_move] + grid_blocked_squares)
                targets = goblins if making_move["type"] == "elf" else elves
                if not targets:
                    break

                # Find squares in range of targets
                in_range = []
                for point in targets:
                    for dx, dy in [(0, -1), (-1, 0), (1, 0), (0, 1)]:
                        new_point = (point["loc"][0] + dx,
                                     point["loc"][1] + dy)
                        if not new_point in blocked_coords:
                            in_range.append(new_point)

                if making_move["loc"] not in in_range:
                    # Move stage of turn
                    # Find square to move to
                    end_point_shortest_path = None
                    first_point_shortest_path = None
                    shortest_path_adjacent = None
                    shortest_path_len = float("inf")
                    best_paths = []
                    for ir_point in in_range:
                        shortest_raw = shortest_paths(
                            blocked_coords, making_move["loc"], ir_point, elves, goblins)
                        if shortest_raw:
                            best_paths.extend(shortest_raw)
                    # First condition - fewest number of moves away
                    if best_paths:
                        min_steps = min([x[1] for x in best_paths])
                        best_paths = [
                            x for x in best_paths if x[1] == min_steps]

                        # Second condition - if tie, choose the final tile in reading order
                        best_paths.sort(key=lambda x: (x[2][1], x[2][0]))
                        best_paths = [x for x in best_paths if x[2]
                                      == best_paths[0][2]]

                        # Third condition - if tie, take the first step in reading order
                        best_paths.sort(key=lambda x: (x[0][1], x[0][0]))
                        best_paths = [x for x in best_paths if x[0]
                                      == best_paths[0][0]]
                        # Move to that square
                        making_move["loc"] = best_paths[0][0]

                # Attack
                if making_move["loc"] in in_range:
                    enemies_in_range = []
                    for enemy in targets:
                        for dx, dy in [(0, -1), (-1, 0), (1, 0), (0, 1)]:
                            new_point = (enemy["loc"][0] + dx,
                                         enemy["loc"][1] + dy)
                            if making_move["loc"] == new_point:
                                enemies_in_range.append(enemy)
                                break
                    enemies_in_range = sorted(
                        enemies_in_range, key=lambda e: (e["hp"], e["loc"][1], e["loc"][0]))
                    enemies_in_range[0]["hp"] -= making_move["attack"]
                    if enemies_in_range[0]["hp"] <= 0:
                        if enemies_in_range[0]["type"] == "goblin":
                            goblins.remove(enemies_in_range[0])
                        else:
                            elves_killed = True
                            elves.remove(enemies_in_range[0])
            else:
                for_finished = True
                if len(goblins) == 0 or len(elves) == 0:
                    if len(elves) == len(elves_og):
                        return num_rounds * (sum(g["hp"] for g in goblins) + sum(e["hp"] for e in elves))
                num_rounds += 1
            if not for_finished:
                if len(elves) == len(elves_og):
                    return num_rounds * (sum(g["hp"] for g in goblins) + sum(e["hp"] for e in elves))
    return num_rounds * (sum(g["hp"] for g in goblins) + sum(e["hp"] for e in elves))


print(part_one(*get_input()))
print(part_two(*get_input()))
