"""
This is an interesting one. Had to implement a custom mult x y z (z = x*y) instruction.
Changed lines 5-10 of the input from:
cpy b c
inc a
dec c
jnz c -2
dec d
jnz d -5
To:
mul b d a
cpy 0 c
cpy 0 d
jnz 0 0
jnz 0 0
jnz 0 0

Essentially just set a = b * d then a bunch of no-ops (and setting c and d to 0 as they need to be).
"""


def get_input():
    with open("day_23/input_modified.txt", "r") as f:
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

    return instructions


def part_one(instructions):
    registers = {x: 0 for x in "abcd"}
    registers["a"] = 7
    instruction_pointer = 0
    while instruction_pointer < len(instructions):
        try:
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
                case ("tgl", x):
                    if isinstance(x, str):
                        x = registers[x]
                    old_in = instructions[instruction_pointer + x]
                    if len(old_in) == 3 and old_in[0] == "jnz":
                        instructions[instruction_pointer +
                                     x] = ("cpy", *old_in[1:])
                    elif len(old_in) == 3:
                        instructions[instruction_pointer +
                                     x] = ("jnz", *old_in[1:])
                    if len(old_in) == 2 and old_in[0] == "inc":
                        instructions[instruction_pointer +
                                     x] = ("dec", *old_in[1:])
                    elif len(old_in) == 2:
                        instructions[instruction_pointer +
                                     x] = ("inc", *old_in[1:])
                    instruction_pointer += 1
                case ("mul", x, y, z):
                    if isinstance(x, str):
                        x = registers[x]
                    if isinstance(y, str):
                        y = registers[y]
                    registers[z] = x * y
                    instruction_pointer += 1
        except:
            # tgl has created an invalid instruction, no problem :P
            instruction_pointer += 1

    return registers["a"]


def part_two(instructions):
    registers = {x: 0 for x in "abcd"}
    registers["a"] = 12
    instruction_pointer = 0
    while instruction_pointer < len(instructions):
        try:
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
                case ("tgl", x):
                    if isinstance(x, str):
                        x = registers[x]
                    old_in = instructions[instruction_pointer + x]
                    if len(old_in) == 3 and old_in[0] == "jnz":
                        instructions[instruction_pointer +
                                     x] = ("cpy", *old_in[1:])
                    elif len(old_in) == 3:
                        instructions[instruction_pointer +
                                     x] = ("jnz", *old_in[1:])
                    if len(old_in) == 2 and old_in[0] == "inc":
                        instructions[instruction_pointer +
                                     x] = ("dec", *old_in[1:])
                    elif len(old_in) == 2:
                        instructions[instruction_pointer +
                                     x] = ("inc", *old_in[1:])
                    instruction_pointer += 1
                case ("mul", x, y, z):
                    if isinstance(x, str):
                        x = registers[x]
                    if isinstance(y, str):
                        y = registers[y]
                    registers[z] = x * y
                    instruction_pointer += 1
        except:
            # tgl has created an invalid instruction, no problem :P
            instruction_pointer += 1

    return registers["a"]


print(part_one(get_input()))
print(part_two(get_input()))
