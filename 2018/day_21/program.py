INSTRUCTION_FUNCS = {
    "addr": lambda a, b, registers: registers[a] + registers[b],
    "addi": lambda a, b, registers: registers[a] + b,
    "mulr": lambda a, b, registers: registers[a] * registers[b],
    "muli": lambda a, b, registers: registers[a] * b,
    "banr": lambda a, b, registers: registers[a] & registers[b],
    "bani": lambda a, b, registers: registers[a] & b,
    "borr": lambda a, b, registers: registers[a] | registers[b],
    "bori": lambda a, b, registers: registers[a] | b,
    "setr": lambda a, _, registers: registers[a],
    "seti": lambda a, _, registers: a,
    "gtir": lambda a, b, registers: 1 if a > registers[b] else 0,
    "gtri": lambda a, b, registers: 1 if registers[a] > b else 0,
    "gtrr": lambda a, b, registers: 1 if registers[a] > registers[b] else 0,
    "eqir": lambda a, b, registers: 1 if a == registers[b] else 0,
    "eqri": lambda a, b, registers: 1 if registers[a] == b else 0,
    "eqrr": lambda a, b, registers: 1 if registers[a] == registers[b] else 0,
}


def get_input():
    with open("day_21/input.txt", "r") as f:
        file = f.read().splitlines()

    instructions = []
    for line in file:
        match line.split(" "):
            case ["#ip", a]:
                ip = int(a)
            case [instruction, a, b, c]:
                instructions.append((instruction, int(a), int(b), int(c)))
    return instructions, ip


def part_one(instructions, ip):
    registers = {key: 0 for key in range(15)}
    while registers[ip] < len(instructions):
        instruction, a, b, c = instructions[registers[ip]]
        if registers[ip] == 28:
            # 0 is never modified :P
            return registers[4]
        registers[c] = INSTRUCTION_FUNCS[instruction](a, b, registers)
        registers[ip] += 1


def part_two(instructions, ip):
    registers = {key: 0 for key in range(15)}
    found_values = []
    cycle = False
    while registers[ip] < len(instructions):
        instruction, a, b, c = instructions[registers[ip]]
        if registers[ip] == 28:
            if registers[4] in found_values and not cycle:
                # found_values = found_values[next(i for i in reversed(range(len(found_values))) if found_values[i] == registers[4]):] + [registers[4]]
                return found_values[-1]
                cycle = True
            elif registers[4] in found_values and cycle:
                print(len(found_values))
                return min(found_values)
                # return found_values[-1], registers[4]
            else:
                found_values.append(registers[4])
        registers[c] = INSTRUCTION_FUNCS[instruction](a, b, registers)
        registers[ip] += 1


print(part_one(*get_input()))
print(part_two(*get_input()))