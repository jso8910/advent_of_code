from collections import defaultdict, deque

# Boilerplate to get intcode to work
from os import path
import sys
if __name__ == "__main__" and __package__ is None:  # nopep8
    sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))  # nopep8
from intcode import Intcode


def get_input():
    with open("day_9/input.txt", "r") as f:
        d = defaultdict(int)
        for idx, n in enumerate(f.read().split(",")):
            d[idx] = int(n)
        return d


def part_one(instructions):
    pointer = 0
    output = []
    input_queue = deque([1])
    relative_base = 0
    computer = Intcode()
    for instruction, output, input_queue, input_requested, pointer, relative_base in computer.run(instructions, input_queue):
        continue
    return output.pop()


def part_two(instructions):
    pointer = 0
    output = []
    input_queue = deque([2])
    relative_base = 0
    computer = Intcode()
    for instruction, output, input_queue, input_requested, pointer, relative_base in computer.run(instructions, input_queue):
        continue
    return output.pop()


print(part_one(get_input()))
print(part_two(get_input()))
