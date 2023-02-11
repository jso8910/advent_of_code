from collections import deque
from collections import defaultdict
# This solution is so slow and bad but it works? Not proud at all.
# I am sorry for this code it takes like 5 minutes for each part and makes me want to die oh god
# forgive me for i have sinned don't read this code it isnt too late


def get_input():
    with open("day_17/input.txt", "r") as f:
        file = f.read().splitlines()

    grid = defaultdict(str)
    for line in file:
        constant, r = line.split(", ")
        if constant.split("=")[0] == "x":
            x = int(constant.split("=")[1])
            for y in range(int(r.split("=")[1].split("..")[0]), int(r.split("=")[1].split("..")[1]) + 1):
                grid[(x, y)] = "#"
        else:
            y = int(constant.split("=")[1])
            for x in range(int(r.split("=")[1].split("..")[0]), int(r.split("=")[1].split("..")[1]) + 1):
                grid[(x, y)] = "#"

    return grid


def part_one(grid):
    min_y = min(y for x, y in grid)
    max_y = max(y for x, y in grid)
    min_x = min(x for x, y in grid) - 1
    max_x = max(x for x, y in grid) + 1
    water_grid = defaultdict(lambda: True)
    queue = deque([(500, 0)])
    node = (500, 0)
    visited = set()
    settled = set()
    prev = -2
    prev2 = -3
    prev3 = -4
    while queue:
        node = queue.popleft()
        # If same thing occurs 3 times in a row because im lazy to figure this out
        if sum(1 for v in visited | settled if min_y <= v[1] <= max_y) == prev3:
            break
        prev3 = prev2
        prev2 = prev
        prev = sum(1 for v in visited | settled if min_y <= v[1] <= max_y)
        for node in visited | set([node]):
            row_full = True
            for wall_left_x in range(node[0], min_x - 1, -1):
                if grid[(wall_left_x, node[1])] == "#":
                    break
            else:
                row_full = False
            for wall_right_x in range(node[0], max_x + 1):
                if not row_full:
                    break
                if grid[(wall_right_x, node[1])] == "#":
                    break
            else:
                row_full = False
            for x in range(wall_left_x + 1, wall_right_x):
                if not row_full:
                    break
                if (x, node[1]) not in visited:
                    row_full = False
                    break
            if row_full:
                for x in range(wall_left_x + 1, wall_right_x):
                    visited.remove((x, node[1]))
                    settled.add((x, node[1]))
            if (node[0], node[1] + 1) not in settled and not grid[(node[0], node[1] + 1)]:
                queue.append((node[0], node[1] + 1))
                visited.add((node[0], node[1] + 1))
                # if node[1] + 1 > max_y:
                #     break
            else:
                if (node[0] + 1, node[1]) not in settled and not grid[(node[0] + 1, node[1])]:
                    queue.append((node[0] + 1, node[1]))
                    visited.add((node[0] + 1, node[1]))
                if (node[0] - 1, node[1]) not in settled and not grid[(node[0] - 1, node[1])]:
                    queue.append((node[0] - 1, node[1]))
                    visited.add((node[0] - 1, node[1]))
        # print(sum(1 for v in visited | settled if min_y <= v[1] <= max_y))
    return sum(1 for v in visited | settled if min_y <= v[1] <= max_y)


def part_two(grid):
    min_y = min(y for x, y in grid)
    max_y = max(y for x, y in grid)
    min_x = min(x for x, y in grid) - 1
    max_x = max(x for x, y in grid) + 1
    water_grid = defaultdict(lambda: True)
    queue = deque([(500, 0)])
    node = (500, 0)
    visited = set()
    settled = set()
    prev = -2
    prev2 = -3
    prev3 = -4
    while queue:
        node = queue.popleft()
        # If same thing occurs 3 times in a row because im lazy to figure this out
        if sum(1 for v in visited | settled if min_y <= v[1] <= max_y) == prev3:
            break
        prev3 = prev2
        prev2 = prev
        prev = sum(1 for v in visited | settled if min_y <= v[1] <= max_y)
        for node in visited | set([node]):
            row_full = True
            for wall_left_x in range(node[0], min_x - 1, -1):
                if grid[(wall_left_x, node[1])] == "#":
                    break
            else:
                row_full = False
            if grid[(wall_left_x, node[1])] != "#":
                row_full = False
            for wall_right_x in range(node[0], max_x + 1):
                if not row_full:
                    break
                if grid[(wall_right_x, node[1])] == "#":
                    break
            else:
                row_full = False
            if grid[(wall_right_x, node[1])] != "#":
                row_full = False
            for x in range(wall_left_x + 1, wall_right_x):
                if not row_full:
                    break
                if (x, node[1]) not in visited:
                    row_full = False
                    break
            if row_full:
                for x in range(wall_left_x + 1, wall_right_x):
                    # if x <= min_x + 1 or x >= max_x - 1:
                    #     continue
                    visited.remove((x, node[1]))
                    settled.add((x, node[1]))
            if (node[0], node[1] + 1) not in settled and not grid[(node[0], node[1] + 1)]:
                queue.append((node[0], node[1] + 1))
                visited.add((node[0], node[1] + 1))
                # if node[1] + 1 > max_y:
                #     break
            else:
                if (node[0] + 1, node[1]) not in settled and not grid[(node[0] + 1, node[1])]:
                    queue.append((node[0] + 1, node[1]))
                    visited.add((node[0] + 1, node[1]))
                if (node[0] - 1, node[1]) not in settled and not grid[(node[0] - 1, node[1])]:
                    queue.append((node[0] - 1, node[1]))
                    visited.add((node[0] - 1, node[1]))
        # print(sum(1 for v in visited | settled if min_y <= v[1] <= max_y))
    # return sum(1 for v in visited | settled if min_y <= v[1] <= max_y)
    for node in visited | set():
        row_full = True
        for wall_left_x in range(node[0], min_x - 1, -1):
            if grid[(wall_left_x, node[1])] == "#":
                break
        if grid[(wall_left_x, node[1])] != "#":
            row_full = False
        for wall_right_x in range(node[0], max_x + 1):
            if grid[(wall_right_x, node[1])] == "#":
                break
        if grid[(wall_right_x, node[1])] != "#":
            row_full = False
        for x in range(wall_left_x + 1, wall_right_x):
            if not row_full:
                break
            if (x, node[1]) not in visited:
                row_full = False
                break
        if row_full:
            for x in range(wall_left_x + 1, wall_right_x):
                visited.remove((x, node[1]))
                settled.add((x, node[1]))

    # for y in range(min_y, max_y + 1):
    #     for x in range(min_x, max_x + 1):
    #         if grid[(x, y)] == "#":
    #             print("#", end="")
    #         elif (x, y) in settled:
    #             print("~", end="")
    #         elif (x, y) in visited:
    #             print("|", end="")
    #         else:
    #             print(" ", end="")
    #     print()
    return sum(1 for v in settled if min_y <= v[1] <= max_y)


# print(part_one(get_input()))
print(part_two(get_input()))
