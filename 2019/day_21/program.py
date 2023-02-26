# Boilerplate to get intcode to work
from collections import defaultdict, deque
from os import path
import sys
if __name__ == "__main__" and __package__ is None:  # nopep8
    sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))  # nopep8
from intcode import Intcode


def get_input():
    with open("day_21/input.txt", "r") as f:
        d = defaultdict(int)
        for idx, n in enumerate(f.read().split(",")):
            d[idx] = int(n)
        return d


def part_one(program):
    computer = Intcode()
    current_loc = 0
    current_dir = -1j
    s = ""
    input_queue = deque([ord(c)
                        for c in "\n".join([
                            "NOT A T",
                            "NOT B J",
                            "OR T J",
                            "NOT C T",
                            "OR T J",
                            "AND D J",
                            "WALK"
                        ]) + "\n"])
    for instruction, output, input_queue, input_requested, pointer, relative_base in computer.run(program, input_queue):
        if output:
            p = output.pop()
            if p > 255:
                return p
            s += chr(p)


def part_two(program):
    computer = Intcode()
    current_loc = 0
    current_dir = -1j
    s = ""
    input_queue = deque([ord(c)
                        for c in "\n".join([
                            "NOT A T",
                            "NOT B J",
                            "OR T J",
                            "NOT C T",
                            "OR T J",
                            "AND D J",
                            "NOT H T",
                            "NOT T T",
                            "OR E T",
                            "AND T J",
                            "RUN"
                        ]) + "\n"])
    for instruction, output, input_queue, input_requested, pointer, relative_base in computer.run(program, input_queue):
        if output:
            p = output.pop()
            if p > 255:
                return p
            s += chr(p)


print(part_one(get_input()))
print(part_two(get_input()))
