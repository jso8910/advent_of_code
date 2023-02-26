# This one I'm proud of. Was fun to finally get right and very rewarding because I thought it would be impossible

# Boilerplate to get intcode to work
from collections import defaultdict, deque
from os import path
import sys
if __name__ == "__main__" and __package__ is None:  # nopep8
    sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))  # nopep8
from intcode import Intcode


def get_input():
    with open("day_17/input.txt", "r") as f:
        d = defaultdict(int)
        for idx, n in enumerate(f.read().split(",")):
            d[idx] = int(n)
        return d


def part_one(program):
    computer = Intcode()
    input_queue = deque([])
    grid = defaultdict(lambda: ".")
    idx = 0
    cidx = 0
    for instruction, output, input_queue, input_requested, pointer, relative_base in computer.run(program, input_queue):
        if output:
            thing = chr(output.pop())
            if thing == "\n":
                cidx = 0
                idx += 1
            else:
                grid[(cidx, idx)] = thing
                cidx += 1

    intersections = 0
    for point in list(grid):
        if grid[point] != "#":
            continue
        num_scaffold = 0
        for dy, dx in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            num_scaffold += grid[(point[0] + dx, point[1] + dy)] == "#"
        if num_scaffold >= 3:
            intersections += point[0] * point[1]
    # s = [[" " for _ in range(int(max(g[0] for g in grid) + 1))]
    #      for _ in range(int(max(p[1] for p in grid) + 1))]
    # for g in grid:
    #     s[int(g[1])][int(g[0])] = grid[g]
    # print("\n".join(["".join(p) for p in s]))
    return intersections


def part_two(program):
    original = program.copy()
    computer = Intcode()
    input_queue = deque([])
    grid = defaultdict(lambda: ".")
    idx = 0
    cidx = 0
    for instruction, output, input_queue, input_requested, pointer, relative_base in computer.run(program, input_queue):
        if output:
            thing = chr(output.pop())
            if thing == "\n":
                cidx = 0
                idx += 1
            else:
                grid[(cidx, idx)] = thing
                cidx += 1

    intersections = []
    for point in list(grid):
        if grid[point] != "#":
            continue
        num_scaffold = 0
        for dy, dx in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            num_scaffold += grid[(point[0] + dx, point[1] + dy)] == "#"
        if num_scaffold >= 3:
            intersections.append(point)
    queue = deque([([g], "", (0, -1)) for g in grid if grid[g] in "<>v^"])
    visited = set()
    scaffolding = set(g for g in grid if grid[g] in "#<>v^")
    # BFS to find optimal path. Done by assuming you should never turn
    # In reality it's probably just one possible path I think
    while queue:
        path, s, dir = queue.popleft()
        if set(path) == scaffolding:
            best = s
        n_p = (path[-1][0] + dir[0], path[-1][1] + dir[1])
        match dir:
            case (1, 0):
                new_possible_dirs = [("R", (0, 1)), ("L", (0, -1))]
            case (-1, 0):
                new_possible_dirs = [("L", (0, 1)), ("R", (0, -1))]
            case (0, -1):
                new_possible_dirs = [("R", (1, 0)), ("L", (-1, 0))]
            case (0, 1):
                new_possible_dirs = [("L", (1, 0)), ("R", (-1, 0))]
        for ds, d in new_possible_dirs + [("", dir)]:
            if (path[-1][0] + d[0], path[-1][1] + d[1]) in scaffolding:
                ns = s + ds
                ndir = d
                new_points = [(path[-1][0], path[-1][1])]
                n = 0
                while True:
                    new_points.append((new_points[-1][0] + d[0],
                                       new_points[-1][1] + d[1]))
                    if new_points[-1] not in scaffolding:
                        new_points.pop()
                        break
                    n += 1
                ns += str(len(new_points[1:]))
                queue.append((path + new_points[1:], ns, d))
    path_str = best
    func_1_start = 0
    to_break = False
    # Split into substrings. Painful code lmfao
    for func_1_end in range(2, 22):
        if to_break:
            break
        for func_2_start in range(func_1_end, func_1_end + 20):
            if to_break:
                break
            for func_2_end in range(func_2_start + 2, func_2_start + 20 + 2):
                if to_break:
                    break
                for func_3_start in range(func_2_end, func_2_end + 20):
                    if to_break:
                        break
                    for func_3_end in range(func_3_start + 2, func_3_start + 20 + 2):
                        if to_break:
                            break
                        func_1 = path_str[:func_1_end]
                        func_2 = path_str[func_2_start:func_2_end]
                        func_3 = path_str[func_3_start:func_3_end]
                        path_cpy = str(path_str)
                        removal_order = ""
                        while True:
                            if path_cpy.startswith(func_1):
                                path_cpy = path_cpy.removeprefix(func_1)
                                removal_order += "A"
                            elif path_cpy.startswith(func_2):
                                path_cpy = path_cpy.removeprefix(func_2)
                                removal_order += "B"
                            elif path_cpy.startswith(func_3):
                                path_cpy = path_cpy.removeprefix(func_3)
                                removal_order += "C"
                            elif len(path_cpy) == 0:
                                to_break = True
                                break
                            else:
                                break

    func_1_list = []
    temp = ""
    for char in func_1:
        if char in "LR":
            if temp:
                func_1_list.append(temp)
                temp = ""
            func_1_list.append(char)
        else:
            temp += char
    if temp:
        func_1_list.append(temp)
    func_2_list = []
    temp = ""
    for char in func_2:
        if char in "LR":
            if temp:
                func_2_list.append(temp)
                temp = ""
            func_2_list.append(char)
        else:
            temp += char
    if temp:
        func_2_list.append(temp)
    func_3_list = []
    temp = ""
    for char in func_3:
        if char in "LR":
            if temp:
                func_3_list.append(temp)
                temp = ""
            func_3_list.append(char)
        else:
            temp += char
    if temp:
        func_3_list.append(temp)

    program = original.copy()
    program[0] = 2
    computer = Intcode()
    input_queue = deque([
        *[ord(c) for c in ",".join(removal_order) + "\n"],
        *[ord(c) for c in ",".join(func_1_list) + "\n"],
        *[ord(c) for c in ",".join(func_2_list) + "\n"],
        *[ord(c) for c in ",".join(func_3_list) + "\n"],
        *[ord(c) for c in "n" + "\n"]
    ])
    for instruction, output, input_queue, input_requested, pointer, relative_base in computer.run(program, input_queue):
        if output:
            thing = output.pop()
            # If it isn't ascii
            if thing > 255:
                return thing
            thing = chr(thing)
            if thing == "\n":
                cidx = 0
                idx += 1
            else:
                grid[(cidx, idx)] = thing
                cidx += 1


print(part_one(get_input()))
print(part_two(get_input()))
