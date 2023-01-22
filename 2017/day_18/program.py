from collections import defaultdict
"""
If you have stumbled upon this code, it isn't too late to turn back.
You are about to read the most ugly code you will ever read and I can't be held responsible for your (lack) of
sanity after reading this code. I coded it so it worked reasonably efficiently and, while I could make it
more readable, I decided to be lazy and not do that.
"""


def get_input():
    with open("day_18/input.txt", "r") as f:
        file = f.read().splitlines()

    instructions = []
    for line in file:
        match line.split(" "):
            case ["snd", x]:
                if x.lstrip("-").isnumeric():
                    x = int(x)
                instructions.append(("snd", x))
            case ["set", x, y]:
                if y.lstrip("-").isnumeric():
                    y = int(y)
                instructions.append(("set", x, y))
            case ["add", x, y]:
                if y.lstrip("-").isnumeric():
                    y = int(y)
                instructions.append(("add", x, y))
            case ["mul", x, y]:
                if y.lstrip("-").isnumeric():
                    y = int(y)
                instructions.append(("mul", x, y))
            case ["mod", x, y]:
                if y.lstrip("-").isnumeric():
                    y = int(y)
                instructions.append(("mod", x, y))
            case ["rcv", x]:
                if x.lstrip("-").isnumeric():
                    x = int(x)
                instructions.append(("rcv", x))
            case ["jgz", x, y]:
                if x.lstrip("-").isnumeric():
                    x = int(x)
                if y.lstrip("-").isnumeric():
                    y = int(y)
                instructions.append(("jgz", x, y))
    return instructions


def part_one(instructions):
    registers = defaultdict(int)
    sounds = []
    i_pointer = 0
    while i_pointer < len(instructions):
        instruction = instructions[i_pointer]
        match instruction:
            case ("snd", x):
                if isinstance(x, str):
                    x = registers[x]
                sounds.append(x)
                i_pointer += 1
            case ("set", x, y):
                if isinstance(y, str):
                    y = registers[y]
                registers[x] = y
                i_pointer += 1
            case ("add", x, y):
                if isinstance(y, str):
                    y = registers[y]
                registers[x] += y
                i_pointer += 1
            case ("mul", x, y):
                if isinstance(y, str):
                    y = registers[y]
                registers[x] *= y
                i_pointer += 1
            case ("mod", x, y):
                if isinstance(y, str):
                    y = registers[y]
                registers[x] %= y
                i_pointer += 1
            case ("rcv", x):
                if isinstance(x, str):
                    x = registers[x]
                if x != 0:
                    return sounds[-1]
                i_pointer += 1
            case ("jgz", x, y):
                if isinstance(x, str):
                    x = registers[x]
                if isinstance(y, str):
                    y = registers[y]
                if x > 0:
                    i_pointer += y
                else:
                    i_pointer += 1


def part_two(instructions):
    registers_p0 = defaultdict(int)
    registers_p1 = defaultdict(int)
    registers_p1["p"] = 1
    i_pointer_p0 = 0
    i_pointer_p1 = 0
    p0_is_recv = False
    p1_is_recv = False
    p0_queue = []
    p1_queue = []
    p0_is_over = False
    p1_is_over = False
    p1_data_sent = 0
    while not p0_is_over or not p1_is_over:
        if not p0_is_over:
            instruction_0 = instructions[i_pointer_p0]
            match instruction_0:
                case ("snd", x):
                    if isinstance(x, str):
                        x = registers_p0[x]
                    p1_queue.append(x)
                    i_pointer_p0 += 1
                case ("set", x, y):
                    if isinstance(y, str):
                        y = registers_p0[y]
                    registers_p0[x] = y
                    i_pointer_p0 += 1
                case ("add", x, y):
                    if isinstance(y, str):
                        y = registers_p0[y]
                    registers_p0[x] += y
                    i_pointer_p0 += 1
                case ("mul", x, y):
                    if isinstance(y, str):
                        y = registers_p0[y]
                    registers_p0[x] *= y
                    i_pointer_p0 += 1
                case ("mod", x, y):
                    if isinstance(y, str):
                        y = registers_p0[y]
                    registers_p0[x] %= y
                    i_pointer_p0 += 1
                case ("rcv", x):
                    if p0_queue:
                        i_pointer_p0 += 1
                        registers_p0[x] = p0_queue.pop(0)
                        p0_is_recv = False
                    else:
                        p0_is_recv = True
                case ("jgz", x, y):
                    if isinstance(x, str):
                        x = registers_p0[x]
                    if isinstance(y, str):
                        y = registers_p0[y]
                    if x > 0:
                        i_pointer_p0 += y
                    else:
                        i_pointer_p0 += 1

        if not p1_is_over:
            instruction_1 = instructions[i_pointer_p1]
            match instruction_1:
                case ("snd", x):
                    if isinstance(x, str):
                        x = registers_p1[x]
                    p0_queue.append(x)
                    i_pointer_p1 += 1
                    p1_data_sent += 1
                case ("set", x, y):
                    if isinstance(y, str):
                        y = registers_p1[y]
                    registers_p1[x] = y
                    i_pointer_p1 += 1
                case ("add", x, y):
                    if isinstance(y, str):
                        y = registers_p1[y]
                    registers_p1[x] += y
                    i_pointer_p1 += 1
                case ("mul", x, y):
                    if isinstance(y, str):
                        y = registers_p1[y]
                    registers_p1[x] *= y
                    i_pointer_p1 += 1
                case ("mod", x, y):
                    if isinstance(y, str):
                        y = registers_p1[y]
                    registers_p1[x] %= y
                    i_pointer_p1 += 1
                case ("rcv", x):
                    if p1_queue:
                        i_pointer_p1 += 1
                        registers_p1[x] = p1_queue.pop(0)
                        p1_is_recv = False
                    else:
                        p1_is_recv = True
                case ("jgz", x, y):
                    if isinstance(x, str):
                        x = registers_p1[x]
                    if isinstance(y, str):
                        y = registers_p1[y]
                    if x > 0:
                        i_pointer_p1 += y
                    else:
                        i_pointer_p1 += 1

        p0_is_over = i_pointer_p0 >= len(
            instructions) or (p1_is_over and p0_is_recv) or (p0_is_recv and p1_is_recv)
        p1_is_over = i_pointer_p1 >= len(
            instructions) or (p0_is_over and p1_is_recv) or (p0_is_recv and p1_is_recv)
        print(i_pointer_p0, i_pointer_p1, instruction_0,
              instruction_1, registers_p1)

    return p1_data_sent


# print(part_one(get_input()))
print(part_two(get_input()))
