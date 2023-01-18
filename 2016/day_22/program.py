import re
from copy import deepcopy
from itertools import permutations


def get_input():
    with open("day_22/input.txt", "r") as f:
        file = f.read().splitlines()[2:]

    # /dev/grid/node-xX-yY     SIZET   USEDT    AVAILT   PERCENT%
    prog = re.compile(
        r"/dev/grid/node-x(\d+)-y(\d+)\s+(\d+)T\s+(\d+)T\s+(\d+)T\s+(\d+)%")
    disks = {}
    for line in file:
        match = prog.match(line)
        if match:
            x, y, size, used, avail, percent = match.groups()
            disks[(int(x), int(y))] = [
                int(size), int(used), int(avail), int(percent)]

    return disks


def dx(a, b):
    return abs(a[0] - b[0])


def dy(a, b):
    return abs(a[1] - b[1])


def part_one(disks):
    count = 0
    for perm in permutations(disks.items(), 2):
        disk1, disk2 = perm
        assert disk1[0] != disk2[0]
        if disk1[1][1] != 0 and disk1[1][1] <= disk2[1][2]:
            count += 1

    return count


def part_two(disks):
    empty_spot = (
        [coords for coords, thing in disks.items() if thing[1] == 0][0], 0, deepcopy(disks))
    goal = (max(x for x, y in disks.keys()) - 1, 0)
    queue = [empty_spot]
    visited = [empty_spot]
    len_path = 0
    while queue:
        current = queue.pop(0)
        if current[0] == goal:
            # print(current[1])
            len_path = current[1]
            disks = current[2]
            break
        for x, y in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            new = (current[0][0] + x, current[0][1] + y)
            if new in disks and disks[new][1] <= disks[current[0]][0] and new not in visited:
                # print(x, y)
                visited.append(new)
                new_grid = deepcopy(current[2])
                new_grid[current[0]][1] += new_grid[new][1]
                new_grid[current[0]][2] -= new_grid[new][1]
                new_grid[new][1] = 0
                new_grid[new][2] = new_grid[new][0]
                queue.append((new, current[1] + 1, new_grid))

    # print(len_path)
    target_data = (max(x for x, y in disks.keys()), 0)
    current = (
        (max(x for x, y in disks.keys()) - 1, 0), 0, deepcopy(disks), target_data, [])
    goal = (0, 0)
    queue = [current]
    visited = [current]
    while queue:
        queue = sorted(queue, key=lambda x: x[3][0] + 10*x[3][1])
        current = queue.pop(0)
        if current[3] == goal:
            len_path += current[1]
            break
        for x, y in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            new = (current[0][0] + x, current[0][1] + y)
            # With the optimal path, you shouldn't revisit more than twice or thrice.
            if new in disks and disks[new][1] <= disks[current[0]][0] and current[4].count(new) < 3:
                if dx(new, current[3]) > 1 or dy(new, current[3]) > 1:
                    continue
                visited.append(new)
                new_grid = deepcopy(current[2])
                new_grid[current[0]][1] += new_grid[new][1]
                new_grid[current[0]][2] -= new_grid[new][1]
                new_grid[new][1] = 0
                new_grid[new][2] = new_grid[new][0]
                if new == current[3]:
                    if current[0][0] > current[3][0] or current[0][1] > current[3][1]:
                        continue
                    queue.append(
                        (new, current[1] + 1, new_grid, current[0], current[4] + [new]))
                else:
                    queue.append(
                        (new, current[1] + 1, new_grid, current[3], current[4] + [new]))

    return len_path


print(part_one(get_input()))
print(part_two(get_input()))
