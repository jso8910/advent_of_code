from copy import deepcopy


def get_input():
    with open("day_25/input.txt", "r") as f:
        file = f.read().splitlines()

    instructions = []
    for line in file:
        match line.split():
            case ["cpy", x, y]:
                if x not in "abcd":
                    x = int(x)
                if y not in "abcd":
                    y = int(y)
                instructions.append(("cpy", x, y))
            case ["inc", x]:
                instructions.append(("inc", x))
            case ["dec", x]:
                instructions.append(("dec", x))
            case ["jnz", x, y]:
                if x not in "abcd":
                    x = int(x)
                if y not in "abcd":
                    y = int(y)
                instructions.append(("jnz", x, y))
            case ["tgl", x]:
                if x not in "abcd":
                    x = int(x)
                instructions.append(("tgl", x))
            case ["mul", x, y, z]:
                if x not in "abcd":
                    x = int(x)
                if y not in "abcd":
                    y = int(y)
                instructions.append(("mul", x, y, z))
            case ["out", x]:
                if x not in "abcd":
                    x = int(x)
                instructions.append(("out", x))

    return instructions


def part_one(instructions):
    i = 0
    while True:
        i += 1
        registers = {x: 0 for x in "abcd"}
        registers["a"] = i
        instruction_pointer = 0
        outputs = []
        while instruction_pointer < len(instructions):
            match instructions[instruction_pointer]:
                case ("cpy", x, y):
                    if isinstance(x, str):
                        x = registers[x]
                    registers[y]
                    registers[y] = x
                    instruction_pointer += 1
                case ("inc", x):
                    registers[x] += 1
                    instruction_pointer += 1
                case ("dec", x):
                    registers[x] -= 1
                    instruction_pointer += 1
                case ("jnz", x, y):
                    if isinstance(x, str):
                        x = registers[x]
                    if isinstance(y, str):
                        y = registers[y]
                    if x != 0:
                        instruction_pointer += y
                    else:
                        instruction_pointer += 1
                case ("out", x):
                    if isinstance(x, str):
                        x = registers[x]
                    outputs.append(x)
                    if x > 1:
                        break
                    if len(outputs) > 12:
                        if set(outputs) == set([0, 1]) and outputs[0:12] == [0, 1] * 6:
                            return i
                        else:
                            break
                    instruction_pointer += 1


print(part_one(get_input()))
