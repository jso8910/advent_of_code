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
    with open("day_19/input.txt", "r") as f:
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
        registers[c] = INSTRUCTION_FUNCS[instruction](a, b, registers)
        registers[ip] += 1

    return registers[0]


def part_two(instructions, ip):
    # Pretty simple. It's just finding factors lol
    res = 0
    for i in range(1, int(10551314) + 1):
        if 10551314 % i == 0:
            res += i
    return res


print(part_one(*get_input()))
print(part_two(*get_input()))
