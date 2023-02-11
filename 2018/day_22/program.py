from pprint import pprint
from collections import defaultdict
from enum import Enum
import heapq


class ErosionType(Enum):
    ROCKY = 0
    WET = 1
    NARROW = 2


class Tool(Enum):
    TORCH = [ErosionType.ROCKY, ErosionType.NARROW]
    CLIMBING = [ErosionType.ROCKY, ErosionType.WET]
    NEITHER = [ErosionType.WET, ErosionType.NARROW]


def get_input():
    with open("day_22/input.txt", "r") as f:
        depth, target = f.read().splitlines()

    depth = int(depth.split(": ")[1])
    target = tuple(map(int, target.split(": ")[1].split(",")))
    return depth, target


def part_one(depth, target):
    grid = {}

    def get_map_erosion(coord):
        if coord == (0, 0):
            return (depth % 20183)
        elif coord == target:
            return (depth % 20183)
        elif coord[0] == 0:
            return (((coord[1] * 48271) + depth) % 20183)
        elif coord[1] == 0:
            return (((coord[0] * 16807) + depth) % 20183)
        else:
            return (((grid[(coord[0] - 1, coord[1])][0] * grid[(coord[0], coord[1] - 1)][0]) + depth) % 20183)

    danger_score = 0
    for row in range(target[1] + 1):
        for col in range(target[0] + 1):
            erosion = get_map_erosion((col, row))
            danger_score += ErosionType(erosion % 3).value
            grid[(col, row)] = [erosion, ErosionType(erosion % 3)]

    return danger_score


def part_two(depth, target):
    grid = {}

    def get_map_erosion(coord):
        if coord == (0, 0):
            return (depth % 20183)
        elif coord == target:
            return (depth % 20183)
        elif coord[0] == 0:
            return (((coord[1] * 48271) + depth) % 20183)
        elif coord[1] == 0:
            return (((coord[0] * 16807) + depth) % 20183)
        else:
            return (((grid[(coord[0] - 1, coord[1])][0] * grid[(coord[0], coord[1] - 1)][0]) + depth) % 20183)

    for row in range(target[1]*2):
        for col in range(target[0]*2 + 300):
            erosion = get_map_erosion((col, row))
            grid[(col, row)] = [erosion, ErosionType(erosion % 3)]

    num = 0
    queue = [(0, (0, 0), num, Tool.TORCH, False)]
    heapq.heapify(queue)
    visited = set()
    while queue:
        num += 1
        minutes, coords, _, tool, tool_changed = heapq.heappop(queue)
        if coords == target and tool == Tool.TORCH:
            return minutes
        for tool_choice in [Tool.TORCH, Tool.CLIMBING, Tool.NEITHER]:
            if tool_choice != tool and not tool_changed and grid[coords][1] in tool_choice.value and (tool_choice, coords) not in visited:
                num += 1
                heapq.heappush(queue, (minutes + 7, coords, num,
                               tool_choice, True))

        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            new_coords = (coords[0] + dx, coords[1] + dy)
            if new_coords in grid and grid[new_coords][1] in tool.value and (tool, new_coords) not in visited:
                num += 1
                visited.add((tool, new_coords))
                heapq.heappush(
                    queue, (minutes + 1, new_coords, num, tool, False))


print(part_one(*get_input()))
print(part_two(*get_input()))
