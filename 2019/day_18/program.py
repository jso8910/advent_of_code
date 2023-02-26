from sys import maxsize
from collections import defaultdict, deque
from itertools import permutations, combinations, islice
from math import factorial
import heapq


def get_input():
    with open("day_18/input.txt", "r") as f:
        file = f.read().splitlines()

    grid = defaultdict(lambda: "#")
    for idx, line in enumerate(file):
        for ridx, chr in enumerate(line):
            grid[ridx + idx*1j] = chr

    return grid


def bfs(grid, start, end):
    visited = set()
    queue = deque([([g for g in grid if grid[g] == start][0], (), 0)])
    while queue:
        p, required_keys, depth = queue.popleft()
        if grid[p] == end:
            return depth, required_keys

        for dc in [-1, 1, -1j, 1j]:
            nc = p + dc
            n_keys = required_keys
            if grid[nc] == "#":
                continue
            if grid[nc] in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
                n_keys += (grid[nc].lower(),)
            if nc not in visited:
                visited.add(nc)
                queue.append((nc, n_keys, depth + 1))
    return -1, None


def part_one(grid: defaultdict[str]):
    # Include @ because that's the start
    keys = [grid[g] for g in grid if grid[g] in "@abcdefghijklmnopqrstuvwxyz"]
    keys_without_start = [grid[g]
                          for g in grid if grid[g] in "abcdefghijklmnopqrstuvwxyz"]
    path_between_keys = defaultdict(dict)

    for pair1, pair2 in combinations(keys, 2):
        path_between_keys[pair1][pair2] = bfs(
            grid, pair1, pair2)
        path_between_keys[pair2][pair1] = bfs(
            grid, pair2, pair1)

    queue = [(path_between_keys["@"][path][0], "@" + path)
             for path in path_between_keys["@"] if path_between_keys["@"][path][0] > 0 and len(path_between_keys["@"][path][1]) == 0]
    visited = set()
    heapq.heapify(queue)
    mm = 0
    while queue:
        depth, path = heapq.heappop(queue)
        if depth == -1:
            continue
        if mm % 1000 == 0:
            print(mm, len(path), depth)
        mm += 1
        if len(path) == len(keys):
            print(path)
            return depth
        for key in [k for k in keys if k not in path]:
            valid_path = True
            for required_key in path_between_keys[path[-1]][key][1]:
                if required_key not in path:
                    valid_path = False
                    break
            if not valid_path:
                continue
            nd = depth + path_between_keys[path[-1]
                                           ][key][0]
            v = ("".join(sorted(path + key)), nd)
            if v not in visited:
                heapq.heappush(queue,
                               (nd, path + key))
            visited.add(v)


def part_two(grid: defaultdict[str]):
    center = [g for g in grid if grid[g] == "@"][0]
    grid[center] = "#"
    grid[center + 1j] = "#"
    grid[center - 1j] = "#"
    grid[center + 1] = "#"
    grid[center - 1] = "#"
    grid[center + 1 + 1j] = "1"
    grid[center + 1 - 1j] = "2"
    grid[center - 1 + 1j] = "3"
    grid[center - 1 - 1j] = "4"
    # Include 1234 because that's the start
    keys = [grid[g]
            for g in grid if grid[g] in "1234abcdefghijklmnopqrstuvwxyz"]
    keys_without_start = [grid[g]
                          for g in grid if grid[g] in "abcdefghijklmnopqrstuvwxyz"]
    path_between_keys = defaultdict(dict)

    for pair1, pair2 in combinations(keys, 2):
        path_between_keys[pair1][pair2] = bfs(
            grid, pair1, pair2)
        path_between_keys[pair2][pair1] = bfs(
            grid, pair2, pair1)
    queue = []
    for idx in range(1, 5):
        for path in path_between_keys[str(idx)]:
            if path_between_keys[str(idx)][path][0] > 0 and len(path_between_keys[str(idx)][path][1]) == 0:
                queue.append((path_between_keys[str(idx)][path][0], tuple((path_between_keys[str(i)][path][0], str(
                    i) + path) if i == idx else (0, str(i)) for i in range(1, 5))))

    # print(queue, len(queue))
    visited = set()
    heapq.heapify(queue)
    mm = 0
    while queue:
        depth = [0 for _ in range(4)]
        path = ["" for _ in range(4)]
        total_depth, ((depth[0], path[0]), (depth[1], path[1]), (depth[2],
                                                                 path[2]), (depth[3], path[3])) = heapq.heappop(queue)
        if any(d == -1 for d in depth):
            continue
        # if mm % 1000 == 0:
        #     print(mm, len(path[0]), sum(len(p)
        #           for p in path), len(keys), total_depth, depth, path)
        # mm += 1
        if sum(len(p) for p in path) == len(keys):
            return total_depth
        for idx in range(1, 5):
            for key in [k for k in path_between_keys[path[idx - 1][-1]] if k not in path[idx - 1]]:
                if path_between_keys[path[idx - 1][-1]][key][0] == -1:
                    continue

                valid_path = True
                for required_key in path_between_keys[path[idx - 1][-1]][key][1]:
                    if required_key not in "".join(path):
                        valid_path = False
                        break
                if not valid_path:
                    continue

                nd = depth[idx - 1] + path_between_keys[path[idx - 1][-1]
                                                        ][key][0]

                v = ("".join(sorted("".join(path[i]
                     for i in range(4)) + key)), sum(depth) + path_between_keys[path[idx - 1][-1]][key][0])
                if v not in visited:
                    heapq.heappush(queue, (sum(depth) + path_between_keys[path[idx - 1][-1]][key][0], tuple((nd,
                                                                                                            path[idx - 1] + key) if i == idx else (depth[i - 1], path[i - 1]) for i in range(1, 5))))
                    visited.add(v)


# print(part_one(get_input()))
print(part_two(get_input()))
