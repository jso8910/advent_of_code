from itertools import product
import re
from pprint import pprint
from collections import defaultdict, deque


def get_input():
    with open("day_20/input.txt", "r") as f:
        return f.read()


def get_grid(regex, current_coords=[0], grid=defaultdict(set)):
    idx = 0
    before_branch = current_coords.copy()
    current_coords = list(set(current_coords))
    # print(regex)
    while idx < len(regex):
        char = regex[idx]
        match char:
            case "N":
                for i in range(len(current_coords)):
                    grid[current_coords[i]].add(1j)
                    current_coords[i] += 1j
                    grid[current_coords[i]].add(-1j)
            case "E":
                for i in range(len(current_coords)):
                    grid[current_coords[i]].add(1)
                    current_coords[i] += 1
                    grid[current_coords[i]].add(-1)
            case "S":
                for i in range(len(current_coords)):
                    grid[current_coords[i]].add(-1j)
                    current_coords[i] -= 1j
                    grid[current_coords[i]].add(1j)
            case "W":
                for i in range(len(current_coords)):
                    grid[current_coords[i]].add(-1)
                    current_coords[i] -= 1
                    grid[current_coords[i]].add(1)
            case "(":
                paren_level = 0
                for nidx, nchr in enumerate(regex[idx:]):
                    if nchr == "(":
                        paren_level += 1
                    elif nchr == ")":
                        paren_level -= 1
                        if paren_level == 0:
                            current_coords = (get_grid(regex[idx + 1:nidx + idx],
                                                       current_coords=current_coords.copy(), grid=grid))

                            idx = nidx + idx
                            break
            case "|":
                current_coords.extend(get_grid(regex[idx + 1:],
                                               current_coords=before_branch.copy(), grid=grid))
                break
        idx += 1
    return current_coords


def part_one(regex):
    grid = defaultdict(set)
    get_grid(regex, grid=grid)
    queue = deque([(0, 0)])
    visited = set()
    max_dist = -1
    while queue:
        node = queue.popleft()
        for dir in grid[node[0]]:
            if node[0] + dir not in visited:
                visited.add(node[0] + dir)
                max_dist = max(node[1] + 1, max_dist)
                queue.append((node[0] + dir, node[1] + 1))

    return max_dist


def part_two(regex):
    grid = defaultdict(set)
    get_grid(regex, grid=grid)
    queue = deque([(0, 0)])
    dist = {}
    visited = set()
    while queue:
        node = queue.popleft()
        dist[node[0]] = node[1]
        for dir in grid[node[0]]:
            if node[0] + dir not in visited:
                visited.add(node[0] + dir)
                queue.append((node[0] + dir, node[1] + 1))

    return sum(1 for key, val in dist.items() if val >= 1000)


print(part_one(get_input()))
print(part_two(get_input()))
