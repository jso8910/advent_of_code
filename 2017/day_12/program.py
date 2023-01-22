from collections import deque


def get_input():
    with open("day_12/input.txt", "r") as f:
        file = f.read().splitlines()

    pipes = {}
    for line in file:
        key = int(line.split(" <-> ")[0])
        values = [int(x) for x in line.split(" <-> ")[1].split(", ")]
        pipes[key] = values

    return pipes


def part_one(pipes):
    current_key = 0
    connected = [current_key]
    queue = deque([current_key])
    while queue:
        current_thing = queue.popleft()
        for key in pipes[current_thing]:
            if key not in connected:
                connected.append(key)
                queue.append(key)

    return len(connected)


def part_two(pipes):
    num_groups = 0
    current_key = 0
    visited = [current_key]
    queue = deque([current_key])
    while current_key != None:
        while queue:
            current_thing = queue.popleft()
            for key in pipes[current_thing]:
                if key not in visited:
                    queue.append(key)
                    visited.append(key)
        num_groups += 1
        current_key = min([key for key in pipes.keys()
                          if key not in visited], default=None)
        queue = deque([current_key])

    return num_groups


print(part_one(get_input()))
print(part_two(get_input()))
