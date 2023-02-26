# Boilerplate to get intcode to work
from collections import defaultdict, deque
from os import path
import sys
if __name__ == "__main__" and __package__ is None:  # nopep8
    sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))  # nopep8
from intcode import Intcode


def get_input():
    with open("day_23/input.txt", "r") as f:
        d = defaultdict(int)
        for idx, n in enumerate(f.read().split(",")):
            d[idx] = int(n)
        return d


def part_one(program):
    computers = [(Intcode().run(program.copy(), input_queue=deque([i])))
                 for i in range(50)]
    inbox = defaultdict(deque)
    while True:
        for idx, computer in enumerate(computers):
            instruction, output, input_queue, input_requested, pointer, relative_base = next(
                computer)
            if len(output) == 3:
                y = output.pop()
                x = output.pop()
                address = output.pop()
                if address == 255:
                    return y
                inbox[address].append((x, y))

            if input_requested:
                if inbox[idx]:
                    x, y = inbox[idx].popleft()
                    input_queue.append(x)
                    input_queue.append(y)
                else:
                    input_queue.append(-1)


def part_two(program):
    computers = [(Intcode().run(program.copy(), input_queue=deque([i])))
                 for i in range(50)]
    inbox = defaultdict(deque)
    computers_attempting_input = set()
    nat_y_sent = []
    nat_send = None
    while True:
        for idx, computer in enumerate(computers):
            instruction, output, input_queue, input_requested, pointer, relative_base = next(
                computer)
            if len(output) == 3:
                y = output.pop()
                x = output.pop()
                address = output.pop()
                if address == 255:
                    nat_send = (x, y)
                    # print("AAAA", nat_send)
                    # return y
                inbox[address].append((x, y))

            if input_requested:
                if inbox[idx]:
                    x, y = inbox[idx].popleft()
                    input_queue.append(x)
                    input_queue.append(y)
                    computers_attempting_input = set()
                    # print("A", idx)
                else:
                    input_queue.append(-1)
                    if not any(inbox[i] for i in inbox if i != 255):
                        computers_attempting_input.add(idx)
                        if len(computers_attempting_input) == 50 and nat_send:
                            nat_y_sent.append(nat_send[1])
                            if len(nat_y_sent) >= 2 and nat_y_sent[-1] == nat_y_sent[-2]:
                                return nat_y_sent[-1]
                            inbox[0].append(nat_send)
                            nat_send = None
                            computers_attempting_input = set()


print(part_one(get_input()))
print(part_two(get_input()))
