# Boilerplate to get intcode to work
from collections import defaultdict, deque
from os import path
import sys
if __name__ == "__main__" and __package__ is None:  # nopep8
    sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))  # nopep8
from intcode import Intcode


def get_input():
    with open("day_15/input.txt", "r") as f:
        d = defaultdict(int)
        for idx, n in enumerate(f.read().split(",")):
            d[idx] = int(n)
        return d


MOVE_TO_DIR = {
    1: -1j,
    2: 1j,
    3: -1,
    4: 1
}


def map_moves(program, move_sequence: deque, grid, part_one=True, computer=Intcode()):
    # computer = Intcode()
    current_loc = 0
    attempted_move = None
    input_queue = deque([])
    for instruction, output, input_queue, input_requested, pointer, relative_base in computer.run(program, input_queue):
        if input_requested:
            if not move_sequence:
                return current_loc
            attempted_move = move_sequence.popleft()
            # If we know it's blocked it's definitely not good
            if grid[current_loc + MOVE_TO_DIR[attempted_move]] == True:
                return False, None
            input_queue.append(attempted_move)
        if output:
            status = output.pop()
            match status:
                case 0:
                    grid[current_loc + MOVE_TO_DIR[attempted_move]] = True
                case 1:
                    grid[current_loc + MOVE_TO_DIR[attempted_move]] = False
                    current_loc += MOVE_TO_DIR[attempted_move]
                case 2:
                    grid[current_loc + MOVE_TO_DIR[attempted_move]] = 2
                    current_loc += MOVE_TO_DIR[attempted_move]
                    if part_one:
                        # If it's part two, no need to stop there
                        return True
    return current_loc


def part_one(program):
    program_original = program.copy()
    queue = deque([deque([i]) for i in range(1, 5)])
    grid = defaultdict(bool)
    visited = set()
    while queue:
        next_path = queue.popleft()
        res = map_moves(program_original.copy(), next_path.copy(), grid)
        if isinstance(res, tuple):
            continue
        if isinstance(res, complex) or isinstance(res, int):
            if res in visited:
                continue
            visited.add(res)
        if isinstance(res, bool) and res:
            return len(next_path)

        for next_move in range(1, 5):
            new_path = next_path.copy()
            new_path.append(next_move)
            queue.append(new_path)


def part_two(program):
    program_original = program.copy()
    queue = deque([deque([i]) for i in range(1, 5)])
    grid = defaultdict(bool)
    visited = set()
    while queue:
        next_path = queue.popleft()
        res = map_moves(program_original.copy(),
                        next_path.copy(), grid, part_one=False)
        if isinstance(res, tuple):
            continue
        if isinstance(res, complex) or isinstance(res, int):
            if res in visited:
                continue
            visited.add(res)

        for next_move in range(1, 5):
            new_path = next_path.copy()
            new_path.append(next_move)
            queue.append(new_path)

    minutes = 0
    while any(grid[g] == False for g in grid):
        for water in [g for g in grid if grid[g] == 2]:
            for d in [1j, -1j, -1, 1]:
                if grid[water + d] == False:
                    grid[water + d] = 2
        minutes += 1
    return minutes


print(part_one(get_input()))
print(part_two(get_input()))
