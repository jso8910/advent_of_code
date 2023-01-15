from collections import defaultdict


def get_input():
    with open("day_13/input.txt", "r") as f:
        return int(f.read())


counts = bytes(bin(x).count("1") for x in range(2**16))


def is_valid_location(x, y, favorite_number):
    return counts[x*x + 3*x + 2*x*y + y + y*y + favorite_number] % 2 == 0


def part_one(favorite_number):
    # BFS
    queue = [(1, 1, 0)]
    visited = set()
    while queue:
        x, y, depth = queue.pop()
        if (x, y) == (31, 39):
            return depth

        for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            new_x, new_y = x + dx, y + dy
            if new_x >= 0 and new_y >= 0 and is_valid_location(new_x, new_y, favorite_number) and (new_x, new_y) not in visited:
                queue.insert(0, (new_x, new_y, depth + 1))
                visited.add((new_x, new_y))


def part_two(favorite_number):
    # BFS
    queue = [(1, 1, 0)]
    visited = set()
    while queue:
        x, y, depth = queue.pop()
        if depth == 50:
            return len(visited)

        for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            new_x, new_y = x + dx, y + dy
            if new_x >= 0 and new_y >= 0 and is_valid_location(new_x, new_y, favorite_number) and (new_x, new_y) not in visited:
                queue.insert(0, (new_x, new_y, depth + 1))
                visited.add((new_x, new_y))


print(part_one(get_input()))
print(part_two(get_input()))
