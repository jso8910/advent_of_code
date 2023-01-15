def get_input():
    with open("day_12/input.txt", "r") as f:
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

    return instructions


def part_one(instructions):
    registers = {x: 0 for x in "abcd"}
    instruction_pointer = 0
    while instruction_pointer < len(instructions):
        match instructions[instruction_pointer]:
            case ("cpy", x, y):
                if isinstance(x, str):
                    x = registers[x]
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
                if x != 0:
                    instruction_pointer += y
                else:
                    instruction_pointer += 1

    return registers["a"]


def part_two(instructions):
    registers = {x: 0 for x in "abcd"}
    registers["c"] = 1
    instruction_pointer = 0
    while instruction_pointer < len(instructions):
        match instructions[instruction_pointer]:
            case ("cpy", x, y):
                if isinstance(x, str):
                    x = registers[x]
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
                if x != 0:
                    instruction_pointer += y
                else:
                    instruction_pointer += 1

    return registers["a"]


print(part_one(get_input()))
print(part_two(get_input()))
