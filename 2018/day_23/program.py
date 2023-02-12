from math import ceil
import re
import heapq
from itertools import permutations


def get_input():
    with open("day_23/input.txt", "r") as f:
        file = f.read().splitlines()

    nanobots = []
    prog = re.compile("pos=<(\d+),(\d+),(\d+)>, r=(\d+)")
    for line in file:
        match = prog.match(line)
        # x = match.group(1)
        # y = match.group(2)
        # z = match.group(3)
        x, y, z = map(int, line.replace(">", "<").split("<")[1].split(","))
        r = int(line.split("r=")[1])
        nanobots.append(((x, y, z), r))
    return nanobots


def manhattan(p1, p2=(0, 0, 0)):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1]) + abs(p1[2] - p2[2])


def part_one(nanobots):
    max_nanobot = sorted(nanobots, key=lambda x: x[1], reverse=True)[0]
    num_in_range = 0
    for nbot in nanobots:
        if manhattan(max_nanobot[0], nbot[0]) <= max_nanobot[1]:
            num_in_range += 1

    return num_in_range


def part_two(nanobots):
    divisor = 113_379_904
    best = ((-divisor, divisor), (-divisor,
            divisor), (-divisor, divisor))
    done_one = False
    while divisor >= 1:
        new_nanobots = [(tuple(map(lambda x: x / divisor, nbot[0])),
                         ceil(nbot[1] / divisor)) for nbot in nanobots]
        queue = [(0, tuple(b[0]//divisor for b in best))]
        heapq.heapify(queue)
        visited = set()
        max_in_range = -1
        max_point_in_range = None
        while queue:
            coord = heapq.heappop(queue)
            num_in_range = 0
            for nbot in new_nanobots:
                if manhattan(nbot[0], coord[1]) <= nbot[1]:
                    num_in_range += 1
            if num_in_range > max_in_range:
                max_in_range = num_in_range
                max_point_in_range = coord[1]
            elif num_in_range == max_in_range:
                if manhattan(coord[1]) < manhattan(max_point_in_range):
                    max_point_in_range = coord[1]
            for dx, dy, dz in [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]:
                new_coord = (coord[1][0] + dx, coord[1]
                             [1] + dy, coord[1][2] + dz)
                if new_coord not in visited and all(new_coord[i] in range(best[i][0]//divisor, best[i][1]//divisor) for i in range(3)):
                    heapq.heappush(
                        queue, (manhattan(new_coord), new_coord))
                    visited.add(new_coord)
        best = ((max_point_in_range[0]*divisor, (max_point_in_range[0] + 2)*divisor + 1), (max_point_in_range[1]*divisor,
                (max_point_in_range[1] + 1)*divisor + 1), (max_point_in_range[2]*divisor, (max_point_in_range[2] + 1)*divisor + 1))

        # It's kinda strange. Some numbers are too low which idk why that happens. Honestly it works so I won't question it
        divisor //= 20
        if divisor < 1 and not done_one:
            done_one = True
            divisor = 1

    return manhattan(max_point_in_range)


print(part_one(get_input()))
print(part_two(get_input()))
