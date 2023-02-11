from copy import deepcopy
from ast import literal_eval


def get_input():
    with open("day_16/input.txt", "r") as f:
        # print(len(f.read().split("\n\n\n\n")))
        thing = f.read().split("\n\n\n\n")
        samples, program = thing[0].split(
            "\n\n"), thing[1].splitlines()

    samples_list = []
    for sample in samples:
        sample = sample.splitlines()
        samples_list.append({
            "before": literal_eval(sample[0].split("Before: ")[1]),
            "instruction": list(map(int, sample[1].split(" "))),
            "after": literal_eval(sample[2].split("After: ")[1])
        })

    instructions = []
    for instruction in program:
        instructions.append(map(int, instruction.split(" ")))

    return samples_list, instructions


INSTRUCTIONS = {
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


def part_one(samples_list, instructions):
    num_more_three_instruction = 0
    for sample in samples_list:
        num_correct = 0
        _, a, b, c = sample["instruction"]
        for instruction in INSTRUCTIONS.values():
            registers = deepcopy(sample["before"])
            registers[c] = instruction(a, b, registers)
            if registers == sample["after"]:
                num_correct += 1
                if num_correct >= 3:
                    num_more_three_instruction += 1
                    break
    return num_more_three_instruction


def part_two(samples_list, instructions):
    INSTRUCTION_LOOKUP = {}
    INSTRUCTION_POSSIBILITIES = {
        key: set(INSTRUCTIONS.keys()) for key in range(16)}
    for instruction in range(16):
        for sample in samples_list:
            i, a, b, c = sample["instruction"]
            for name, instruction in INSTRUCTIONS.items():
                registers = deepcopy(sample["before"])
                registers[c] = instruction(a, b, registers)
                if registers != sample["after"]:
                    if name in INSTRUCTION_POSSIBILITIES[i]:
                        INSTRUCTION_POSSIBILITIES[i].remove(name)

    while any(map(lambda x: len(x) > 1, INSTRUCTION_POSSIBILITIES.values())):
        for instruction in INSTRUCTION_POSSIBILITIES:
            if len(INSTRUCTION_POSSIBILITIES[instruction]) == 1:
                INSTRUCTION_LOOKUP[instruction] = list(
                    INSTRUCTION_POSSIBILITIES[instruction])[0]
                for remaining in INSTRUCTION_POSSIBILITIES:
                    if len(INSTRUCTION_POSSIBILITIES[remaining]) != 1:
                        INSTRUCTION_POSSIBILITIES[remaining].discard(list(
                            INSTRUCTION_POSSIBILITIES[instruction])[0])
                        if len(INSTRUCTION_POSSIBILITIES[remaining]) == 1:
                            INSTRUCTION_LOOKUP[remaining] = list(
                                INSTRUCTION_POSSIBILITIES[remaining])[0]

    registers = [0, 0, 0, 0]
    for instruction in instructions:
        i, a, b, c = instruction
        registers[c] = INSTRUCTIONS[INSTRUCTION_LOOKUP[i]](a, b, registers)

    return registers[0]


print(part_one(*get_input()))
print(part_two(*get_input()))
