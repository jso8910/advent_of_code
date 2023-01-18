# Do Warshall to create a weighted graph and then simple permutations check (or djikstra, whatever).
# Should be super easy, literally 0 challenge
from collections import defaultdict, deque
from itertools import permutations
import math


def get_input():
    with open("day_24/input.txt", "r") as f:
        file = f.read().splitlines()

    grid = defaultdict(bool)
    required_nodes = set()
    for y, line in enumerate(file):
        for x, char in enumerate(line):
            if char == ".":
                grid[x + y*1j] = True
            elif char == "#":
                grid[x + y*1j] = False
            else:
                grid[x + y*1j] = True
                if int(char) == 0:
                    start = x + y*1j
                else:
                    required_nodes.add(x + y*1j)

    return grid, required_nodes, start


def bfs(grid, start, end):
    queue = deque([(start, 0)])
    visited = set()
    d = False
    while queue:
        node, dist = queue.popleft()
        # if dist % 10 == 0 and not d:
        # print(dist, len(visited), len(queue), len(set(queue)))
        # print(node, dist, len(visited))
        # d = True
        if dist % 10 != 0:
            d = False
        if node == end:
            return dist
        for neighbor in [node + 1, node - 1, node + 1j, node - 1j]:
            if neighbor in grid and grid[neighbor] and neighbor not in visited:
                queue.append((neighbor, dist + 1))
                visited.add(neighbor)


def part_one(grid, required_nodes, start):
    new_graph = {node_start: {node_end: bfs(grid, node_start, node_end)
                              for node_end in required_nodes | set([start])} for node_start in required_nodes | set([start])}

    min_dist = math.inf
    for perm in permutations(key for key in new_graph.keys() if key != start):
        dist = 0
        perm = (start, *perm)
        for node in zip(perm, perm[1:]):
            dist += new_graph[node[0]][node[1]]

        min_dist = min(min_dist, dist)

    return min_dist


def part_two(grid, required_nodes, start):
    new_graph = {node_start: {node_end: bfs(grid, node_start, node_end)
                              for node_end in required_nodes | set([start])} for node_start in required_nodes | set([start])}

    min_dist = math.inf
    for perm in permutations(key for key in new_graph.keys() if key != start):
        dist = 0
        perm = (start, *perm, start)
        for node in zip(perm, perm[1:]):
            dist += new_graph[node[0]][node[1]]

        min_dist = min(min_dist, dist)

    return min_dist


print(part_one(*get_input()))
print(part_two(*get_input()))
