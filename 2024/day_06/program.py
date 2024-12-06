from itertools import product


def get_input():
    with open("day_06/input.txt") as f:
        return [[c for c in line] for line in f.read().splitlines()]


def part_one(grid):
    positions_visited = set()
    guard_position = (0, 0)
    for i, row in enumerate(grid):
        if "^" in row:
            guard_position = (i, row.index("^"))
            break
    # Up
    direction = (-1, 0)
    while 0 <= guard_position[0] < len(grid) and 0 <= guard_position[1] < len(grid[0]):
        positions_visited.add(guard_position)
        new_pos = (guard_position[0] + direction[0], guard_position[1] + direction[1])
        if not 0 <= new_pos[0] < len(grid) or not 0 <= new_pos[1] < len(grid[0]):
            break
        if grid[new_pos[0]][new_pos[1]] == "#":
            # Rotate right
            direction = (direction[1], -direction[0])
        else:
            guard_position = new_pos

    return len(positions_visited), positions_visited


def part_two(grid, original_path):
    num_possible = 0
    guard_position = (0, 0)
    for i, row in enumerate(grid):
        if "^" in row:
            guard_position = (i, row.index("^"))
            break
    starting_pos = guard_position
    for i, j in original_path:
        if (i, j) == starting_pos:
            continue
        guard_position = starting_pos
        previous_positions_and_dir = set()
        # Up
        direction = (-1, 0)
        while 0 <= guard_position[0] < len(grid) and 0 <= guard_position[1] < len(grid[0]):
            if (guard_position, direction) in previous_positions_and_dir:
                num_possible += 1
                break
            previous_positions_and_dir.add((guard_position, direction))
            new_pos = (guard_position[0] + direction[0], guard_position[1] + direction[1])
            if not 0 <= new_pos[0] < len(grid) or not 0 <= new_pos[1] < len(grid[0]):
                break
            if grid[new_pos[0]][new_pos[1]] == "#" or new_pos == (i, j):
                # Rotate right
                direction = (direction[1], -direction[0])
            else:
                guard_position = new_pos

    return num_possible


num_positions_visited, original_path = part_one(get_input())
print(num_positions_visited)
print(part_two(get_input(), original_path))
