from time import sleep
import curses

# Boilerplate to get intcode to work
from collections import defaultdict, deque
from os import path
import sys
if __name__ == "__main__" and __package__ is None:  # nopep8
    sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))  # nopep8
from intcode import Intcode


def get_input():
    with open("day_13/input.txt", "r") as f:
        d = defaultdict(int)
        for idx, n in enumerate(f.read().split(",")):
            d[idx] = int(n)
        return d


def part_one(program):
    computer = Intcode()
    current_loc = 0
    current_dir = -1j
    grid = defaultdict(int)
    input_queue = deque([])
    for instruction, output, input_queue, input_requested, pointer, relative_base in computer.run(program, input_queue):
        if len(output) == 3:
            tile = output.pop()
            y = output.pop()
            x = output.pop()
            grid[(x, y)] = tile

    # s = [[" " for _ in range(int(max(g[0] for g in grid) + 1))]
    #      for _ in range(int(max(p[1] for p in grid) + 1))]
    # for g in grid:
    #     s[int(g[1])][int(g[0])] = "█" if grid[g] else " "
    # print("\n".join(["".join(p) for p in s]))
    return list(grid.values()).count(2)


def sign(n):
    if n > 0:
        return 1
    elif n < 0:
        return -1
    else:
        return 0


def part_two(program, out=False, framerate=200):
    # 2 quarters... for free?
    program[0] = 2

    if out:
        stdscr = curses.initscr()
        curses.noecho()
        curses.curs_set(0)
        stdscr.clear()
    computer = Intcode()
    current_loc = 0
    current_dir = -1j
    input_queue = deque([])
    grid = defaultdict(int)
    high_score = 0
    ball_pos = (0, 0)
    paddle_pos = (0, 0)
    paddle_y = set()
    for instruction, output, input_queue, input_requested, pointer, relative_base in computer.run(program, input_queue):
        if len(output) == 3:
            tile = output.pop()
            y = output.pop()
            x = output.pop()
            if tile == 3:
                paddle_pos = (x, y)
            elif tile == 4:
                ball_pos = (x, y)
            if (x, y) == (-1, 0):
                high_score = tile
            grid[(x, y)] = tile
        if input_requested:
            # Basically just keep the ball under the paddle
            input_queue.append(sign(ball_pos[0] - paddle_pos[0]))
            if out:
                s = [[" " for _ in range(int(max(g[0] for g in grid) + 1))]
                     for _ in range(int(max(p[1] for p in grid) + 1))]
                for g in grid:
                    s[int(g[1])][int(g[0])] = "█" if grid[g] else " "
                stdscr.clear()
                for idx, a in enumerate(["".join(p) for p in s]):
                    stdscr.addstr(idx, 0, a)
                stdscr.addstr(len(["".join(p) for p in s]), 0, "\n")
                stdscr.addstr(len(["".join(p) for p in s]) +
                              1, 0, str("YOUR SCORE:").center(len(s[0])))
                stdscr.addstr(len(["".join(p) for p in s]) +
                              2, 0, str(high_score).center(len(s[0])))
                stdscr.refresh()
                sleep(1/framerate)

    if out:
        s = [[" " for _ in range(int(max(g[0] for g in grid) + 1))]
             for _ in range(int(max(p[1] for p in grid) + 1))]
        for g in grid:
            s[int(g[1])][int(g[0])] = "█" if grid[g] else " "
        stdscr.clear()
        for idx, a in enumerate(["".join(p) for p in s]):
            stdscr.addstr(idx, 0, a)
        stdscr.addstr(len(["".join(p) for p in s]), 0, "\n")
        stdscr.addstr(len(["".join(p) for p in s]) +
                      1, 0, str("YOUR SCORE:").center(len(s[0])))
        stdscr.addstr(len(["".join(p) for p in s]) +
                      2, 0, str(high_score).center(len(s[0])))
        stdscr.refresh()
        sleep(1)
        curses.nocbreak()
        stdscr.keypad(False)
        curses.echo()
        curses.endwin()
    return high_score


print(part_one(get_input()))
# I built an output. Change out to True and update the framerate as you want!
print(part_two(get_input(), out=True, framerate=500))
