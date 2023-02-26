# Boilerplate to get intcode to work
from itertools import count
from collections import defaultdict, deque
from os import path
import sys
if __name__ == "__main__" and __package__ is None:  # nopep8
    sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))  # nopep8
from intcode import Intcode


def get_input():
    with open("day_19/input.txt", "r") as f:
        d = defaultdict(int)
        for idx, n in enumerate(f.read().split(",")):
            d[idx] = int(n)
        return d


def part_one(program):
    program_orig = program.copy()
    computer = Intcode()
    input_queue = deque([])
    grid = defaultdict(bool)
    for idx in range(50):
        for cidx in range(50):
            program = program_orig.copy()
            for instruction, output, input_queue, input_requested, pointer, relative_base in computer.run(program, input_queue):
                if input_requested:
                    input_queue.append(cidx)
                    input_queue.append(idx)
                if output:
                    grid[(cidx, idx)] = bool(output.pop())
                    break

    s = [[" " for _ in range(int(max(g[0] for g in grid) + 1))]
         for _ in range(int(max(p[1] for p in grid) + 1))]
    for g in grid:
        s[int(g[1])][int(g[0])] = "#" if grid[g] else " "
    print("\n".join(["".join(p) for p in s]))
    return sum(grid.values())


def part_two(program):
    program_orig = program.copy()
    computer = Intcode()
    input_queue = deque([])
    grid = defaultdict(bool)
    # idx = 0
    # cidx = 0
    prev_beam_start = 0
    for idx in count():
        beam_start_set = False
        continue_row = False
        found_beam = False
        for cidx in count(start=prev_beam_start):
            prev_beam_start = prev_beam_start
            program = program_orig.copy()
            for instruction, output, input_queue, input_requested, pointer, relative_base in computer.run(program, input_queue):
                if input_requested:
                    input_queue.append(cidx)
                    input_queue.append(idx)
                if output:
                    grid[(cidx, idx)] = bool(output.pop())
                    continue_row = grid[(cidx, idx)]
                    if grid[(cidx, idx)] and not beam_start_set:
                        prev_beam_start = cidx
                        beam_start_set = True
                        found_beam = True
                    break
            if not continue_row and found_beam:
                print(idx, cidx)
                break
            if not continue_row and cidx > 10*idx:
                break

        if idx > 120:
            current_row = idx
            min_current_row = min(
                g[0] for g in grid if grid[g] and g[1] == current_row)
            max_current_row = max(
                g[0] for g in grid if grid[g] and g[1] == current_row)
            row_hundred_ago = idx - 99
            min_row_hundred_ago = min(
                g[0] for g in grid if grid[g] and g[1] == row_hundred_ago)
            max_row_hundred_ago = max(
                g[0] for g in grid if grid[g] and g[1] == row_hundred_ago)
            shared_max = min(max_current_row, max_row_hundred_ago)
            shared_min = max(min_current_row, min_row_hundred_ago)
            if shared_max - shared_min >= 99:
                return shared_min * 10000 + row_hundred_ago


print(part_one(get_input()))
print(part_two(get_input()))
