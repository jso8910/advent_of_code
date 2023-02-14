def get_input():
    with open("day_5/input.txt", "r") as f:
        return list(map(int, f.read().split(",")))


def leading_zeros(number):
    return f"{number:05d}"


def part_one(instructions):
    pointer = 0
    output = []
    input_queue = [1]
    while pointer < len(instructions):
        instruction = leading_zeros(instructions[pointer])
        modes_p1 = int(instruction[2])
        modes_p2 = int(instruction[1])
        modes_p3 = int(instruction[0])
        match int(instruction) % 100:
            case 1:
                v1 = instructions[instructions[pointer + 1]
                                  ] if modes_p1 == 0 else instructions[pointer + 1]
                v2 = instructions[instructions[pointer + 2]
                                  ] if modes_p2 == 0 else instructions[pointer + 2]
                instructions[instructions[pointer + 3]] = v1 + v2
                pointer += 4
            case 2:
                v1 = instructions[instructions[pointer + 1]
                                  ] if modes_p1 == 0 else instructions[pointer + 1]
                v2 = instructions[instructions[pointer + 2]
                                  ] if modes_p2 == 0 else instructions[pointer + 2]
                instructions[instructions[pointer + 3]] = v1 * v2
                pointer += 4
            case 3:
                instructions[instructions[pointer + 1]] = input_queue.pop()
                pointer += 2
            case 4:
                v1 = instructions[instructions[pointer + 1]
                                  ] if modes_p1 == 0 else instructions[pointer + 1]
                output.append(v1)
                pointer += 2
            case 99:
                break
            case _:
                raise ValueError(
                    f"Instruction at pointer {pointer} (instruction: {instruction}) is not valid")
    return output[-1]


def part_two(instructions):
    pointer = 0
    output = []
    input_queue = [5]
    while pointer < len(instructions):
        instruction = leading_zeros(instructions[pointer])
        modes_p1 = int(instruction[2])
        modes_p2 = int(instruction[1])
        modes_p3 = int(instruction[0])
        match int(instruction) % 100:
            case 1:
                v1 = instructions[instructions[pointer + 1]
                                  ] if modes_p1 == 0 else instructions[pointer + 1]
                v2 = instructions[instructions[pointer + 2]
                                  ] if modes_p2 == 0 else instructions[pointer + 2]
                instructions[instructions[pointer + 3]] = v1 + v2
                pointer += 4
            case 2:
                v1 = instructions[instructions[pointer + 1]
                                  ] if modes_p1 == 0 else instructions[pointer + 1]
                v2 = instructions[instructions[pointer + 2]
                                  ] if modes_p2 == 0 else instructions[pointer + 2]
                instructions[instructions[pointer + 3]] = v1 * v2
                pointer += 4
            case 3:
                instructions[instructions[pointer + 1]] = input_queue.pop()
                pointer += 2
            case 4:
                v1 = instructions[instructions[pointer + 1]
                                  ] if modes_p1 == 0 else instructions[pointer + 1]
                output.append(v1)
                pointer += 2
            case 5:
                v1 = instructions[instructions[pointer + 1]
                                  ] if modes_p1 == 0 else instructions[pointer + 1]
                v2 = instructions[instructions[pointer + 2]
                                  ] if modes_p2 == 0 else instructions[pointer + 2]
                if v1 != 0:
                    pointer = v2
                else:
                    pointer += 3
            case 6:
                v1 = instructions[instructions[pointer + 1]
                                  ] if modes_p1 == 0 else instructions[pointer + 1]
                v2 = instructions[instructions[pointer + 2]
                                  ] if modes_p2 == 0 else instructions[pointer + 2]
                if v1 == 0:
                    pointer = v2
                else:
                    pointer += 3
            case 7:
                v1 = instructions[instructions[pointer + 1]
                                  ] if modes_p1 == 0 else instructions[pointer + 1]
                v2 = instructions[instructions[pointer + 2]
                                  ] if modes_p2 == 0 else instructions[pointer + 2]
                instructions[instructions[pointer + 3]] = int(v1 < v2)
                pointer += 4
            case 8:
                v1 = instructions[instructions[pointer + 1]
                                  ] if modes_p1 == 0 else instructions[pointer + 1]
                v2 = instructions[instructions[pointer + 2]
                                  ] if modes_p2 == 0 else instructions[pointer + 2]
                instructions[instructions[pointer + 3]] = int(v1 == v2)
                pointer += 4
            case 99:
                break
            case _:
                raise ValueError(
                    f"Instruction at pointer {pointer} (instruction: {instruction}) is not valid")

    return output[-1]


print(part_one(get_input()))
print(part_two(get_input()))
