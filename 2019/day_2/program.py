def get_input():
    with open("day_2/input.txt", "r") as f:
        return list(map(int, f.read().split(",")))


def part_one(instructions):
    instructions[1] = 12
    instructions[2] = 2
    pointer = 0
    while pointer < len(instructions):
        instruction = instructions[pointer]
        match instruction:
            case 1:
                instructions[instructions[pointer + 3]] = instructions[instructions[pointer + 1]
                                                                       ] + instructions[instructions[pointer + 2]]
                pointer += 3
            case 2:
                instructions[instructions[pointer + 3]] = instructions[instructions[pointer + 1]
                                                                       ] * instructions[instructions[pointer + 2]]
                pointer += 3
            case 99:
                break
        pointer += 1
    return instructions[0]


def part_two(instructions):
    original_instructions = instructions.copy()
    for noun in range(100):
        for verb in range(100):
            instructions = original_instructions.copy()
            instructions[1] = noun
            instructions[2] = verb
            pointer = 0
            while pointer < len(instructions):
                instruction = instructions[pointer]
                match instruction:
                    case 1:
                        instructions[instructions[pointer + 3]] = instructions[instructions[pointer + 1]
                                                                               ] + instructions[instructions[pointer + 2]]
                        pointer += 3
                    case 2:
                        instructions[instructions[pointer + 3]] = instructions[instructions[pointer + 1]
                                                                               ] * instructions[instructions[pointer + 2]]
                        pointer += 3
                    case 99:
                        break
                pointer += 1
            if instructions[0] == 19690720:
                return 100 * noun + verb


print(part_one(get_input()))
print(part_two(get_input()))
