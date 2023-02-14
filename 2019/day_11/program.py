from collections import defaultdict

# Boilerplate to get intcode to work
from os import path
import sys
if __name__ == "__main__" and __package__ is None:  # nopep8
    sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))  # nopep8
from intcode import Intcode


def get_input():
    with open("day_11/input.txt", "r") as f:
        d = defaultdict(int)
        for idx, n in enumerate(f.read().split(",")):
            d[idx] = int(n)
        return d


def turn(dir, right):
    if right:
        return dir * 1j
    else:
        return dir * -1j


def part_one(program):
    computer = Intcode()
    current_loc = 0
    current_dir = -1j
    grid = defaultdict(bool)
    painted = set()
    input_queue = [0]
    for instruction, output, input_queue in computer.run(program, input_queue):
        if len(output) == 2:
            new_dir = output.pop()
            new_color = output.pop()
            grid[current_loc] = new_color == 1
            painted.add(current_loc)
            current_dir = turn(current_dir, right=new_dir == 1)
            current_loc += current_dir
            input_queue.append(int(grid[current_loc]))

    return len(painted)


def part_two(program):
    computer = Intcode()
    current_loc = 0
    current_dir = -1j
    grid = defaultdict(bool)
    grid[0] = True
    input_queue = [1]
    for instruction, output, input_queue in computer.run(program, input_queue):
        if len(output) == 2:
            new_dir = output.pop()
            new_color = output.pop()
            grid[current_loc] = new_color == 1
            current_dir = turn(current_dir, right=new_dir == 1)
            current_loc += current_dir
            input_queue.append(int(grid[current_loc]))

    s = [[" " for _ in range(int(max(g.real for g in grid) + 1))]
         for _ in range(int(max(p.imag for p in grid) + 1))]
    for g in grid:
        s[int(g.imag)][int(g.real)] = "█" if grid[g] else " "

    return "\n".join(["".join(p) for p in s])


print(part_one(get_input()))
print(part_two(get_input()))
