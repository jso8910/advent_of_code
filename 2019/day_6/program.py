from collections import deque, defaultdict


def get_input():
    with open("day_6/input.txt", "r") as f:
        file = f.read().splitlines()

    direct_orbits = defaultdict(set)
    for line in file:
        direct_orbits[line.split(")")[0]].add(line.split(")")[1])

    return direct_orbits


def part_one(direct_orbits):
    queue = deque([("COM", 0)])
    num_orbits = 0
    while queue:
        node, path_len = queue.popleft()
        num_orbits += path_len
        for neighbor in direct_orbits[node]:
            queue.append((neighbor, path_len + 1))
    return num_orbits


def part_two(direct_orbits):
    queue = deque([("YOU", 0)])
    visited = set()
    while queue:
        node, path_len = queue.popleft()
        if node == "SAN":
            return path_len - 2
        for neighbor in direct_orbits[node] | set(n for n in [o for o in direct_orbits] if node in direct_orbits[n]):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path_len + 1))


print(part_one(get_input()))
print(part_two(get_input()))
