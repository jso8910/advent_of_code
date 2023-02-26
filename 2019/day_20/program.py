from collections import defaultdict, deque


def get_input():
    with open("day_20/input.txt", "r") as f:
        file = f.read().splitlines()

    portals = []
    grid = defaultdict(str)
    for idx, row in enumerate(file):
        for cidx, chr in enumerate(row):
            # if chr != " ":
            grid[(cidx, idx)] = chr
            if chr in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
                portals.append((chr, (cidx, idx)))

    portal_pairs = defaultdict(list)
    for portal in portals:
        portal_chr, coord = portal
        for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            if grid[(coord[0] + dx, coord[1] + dy)] in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" and grid[(coord[0] - dx, coord[1] - dy)] == ".":
                chr1 = portal_chr
                chr2 = grid[(coord[0] + dx, coord[1] + dy)]
                # The portal name is reversed, fix it
                if dx < 0 or dy < 0:
                    chr1, chr2 = chr2, chr1

                x_min_max = coord[0] <= 1 or coord[0] >= max(
                    c[0] for c in grid) - 2
                y_min_max = coord[1] <= 1 or coord[1] >= max(
                    c[1] for c in grid) - 2
                if x_min_max or y_min_max:
                    outer = True
                else:
                    outer = False

                portal_pairs[chr1 + chr2].append({
                    "coord_in": coord,
                    "dir_in": (dx, dy),
                    "outer": outer
                })

    return grid, portal_pairs


def part_one(grid, portal_pairs):
    start = (portal_pairs["AA"][0]["coord_in"][0] - portal_pairs["AA"][0]["dir_in"][0],
             portal_pairs["AA"][0]["coord_in"][1] - portal_pairs["AA"][0]["dir_in"][1])
    end = (portal_pairs["ZZ"][0]["coord_in"][0] - portal_pairs["ZZ"][0]["dir_in"][0],
           portal_pairs["ZZ"][0]["coord_in"][1] - portal_pairs["ZZ"][0]["dir_in"][1])
    queue = deque([(start, 0, [start])])
    visited = set()
    while queue:
        point, depth, path = queue.popleft()
        if point == end:
            return depth
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            n_point = (point[0] + dx, point[1] + dy)
            if grid[n_point] == "#":
                continue
            elif grid[n_point] in " ":
                continue
            elif grid[n_point] in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
                # It's a portal
                chr1 = grid[n_point]
                chr2 = grid[(n_point[0] + dx, n_point[1] + dy)]
                # The portal name is reversed, fix it
                if dx < 0 or dy < 0:
                    chr1, chr2 = chr2, chr1
                portal = portal_pairs[chr1 + chr2]
                p_out = None
                for p in portal:
                    if p["coord_in"] != (n_point[0], n_point[1]):
                        p_out = p
                        break
                if p_out:
                    n_point = (
                        p_out["coord_in"][0] -
                        p_out["dir_in"][0],
                        p_out["coord_in"][1] -
                        p_out["dir_in"][1]
                    )
                else:
                    continue
            if n_point not in visited:
                queue.append((n_point, depth + 1, path + [n_point]))
                visited.add(n_point)


def part_two(grid, portal_pairs):
    start = (portal_pairs["AA"][0]["coord_in"][0] - portal_pairs["AA"][0]["dir_in"][0],
             portal_pairs["AA"][0]["coord_in"][1] - portal_pairs["AA"][0]["dir_in"][1], 0)
    end = (portal_pairs["ZZ"][0]["coord_in"][0] - portal_pairs["ZZ"][0]["dir_in"][0],
           portal_pairs["ZZ"][0]["coord_in"][1] - portal_pairs["ZZ"][0]["dir_in"][1], 0)
    queue = deque([(start, 0, [start])])
    visited = set()
    while queue:
        point, depth, path = queue.popleft()
        if point[2] > 100:
            continue
        if point == end:
            return depth
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            n_point = (point[0] + dx, point[1] + dy, point[2])
            if grid[n_point[:2]] == "#":
                continue
            elif grid[n_point[:2]] in " ":
                continue
            elif grid[n_point[:2]] in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
                # It's a portal
                chr1 = grid[n_point[:2]]
                chr2 = grid[(n_point[0] + dx, n_point[1] + dy)]
                # The portal name is reversed, fix it
                if dx < 0 or dy < 0:
                    chr1, chr2 = chr2, chr1
                portal = portal_pairs[chr1 + chr2]
                p_out = None
                p_in = None
                for p in portal:
                    if p["coord_in"] != (n_point[0], n_point[1]):
                        p_out = p
                        # break
                    if p["coord_in"] == (n_point[0], n_point[1]):
                        p_in = p
                if p_out:
                    if p_in["outer"] and point[2] <= 0:
                        continue
                    else:
                        new_layer = point[2]
                        if p_in["outer"]:
                            new_layer -= 1
                        else:
                            new_layer += 1
                    n_point = (
                        p_out["coord_in"][0] -
                        p_out["dir_in"][0],
                        p_out["coord_in"][1] -
                        p_out["dir_in"][1],
                        new_layer
                    )
                else:
                    chr1 = None
                    continue
            if n_point not in visited:
                queue.append(
                    (n_point, depth + 1, path + [n_point]))
                chr1 = None
                visited.add(n_point)


print(part_one(*get_input()))
print(part_two(*get_input()))
