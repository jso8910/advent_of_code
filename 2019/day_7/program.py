from itertools import permutations


def get_input():
    with open("day_7/input.txt", "r") as f:
        return list(map(int, f.read().split(",")))


def leading_zeros(number):
    return f"{number:05d}"


def part_one(instructions):
    pointer = 0
    end_signals = []
    instructions_og = [i for i in instructions]
    for input_queue in permutations([0, 1, 2, 3, 4]):
        input_queue = list(input_queue)
        output = [0]
        for _ in range(5):
            instructions = [i for i in instructions_og]
            input_queue.insert(-1, output.pop())
            pointer = 0
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
                        instructions[instructions[pointer + 1]
                                     ] = input_queue.pop()
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
        end_signals.append(output.pop())
    return max(end_signals)


# This code was quite painful lol
def part_two(instructions):
    end_signals = []
    instructions_og = [i for i in instructions]
    for input_queue in permutations([5, 6, 7, 8, 9]):
        input_queue = list(input_queue)
        output = [0]
        pointers = [0, 0, 0, 0, 0]
        amp_pointer = 0
        instructionses = [[i for i in instructions_og] for _ in range(5)]
        progs_started = [False for _ in range(5)]
        while amp_pointer < 5:
            instructions = instructionses[amp_pointer]
            try:
                if not all(progs_started):
                    input_queue.insert(-1, output.pop())
                else:
                    input_queue.append(output.pop())
            except IndexError:
                break
            while pointers[amp_pointer] < len(instructions):
                instruction = leading_zeros(
                    instructions[pointers[amp_pointer]])
                modes_p1 = int(instruction[2])
                modes_p2 = int(instruction[1])
                modes_p3 = int(instruction[0])
                match int(instruction) % 100:
                    case 1:
                        v1 = instructions[instructions[pointers[amp_pointer] + 1]
                                          ] if modes_p1 == 0 else instructions[pointers[amp_pointer] + 1]
                        v2 = instructions[instructions[pointers[amp_pointer] + 2]
                                          ] if modes_p2 == 0 else instructions[pointers[amp_pointer] + 2]
                        instructions[instructions[pointers[amp_pointer] + 3]] = v1 + v2
                        pointers[amp_pointer] += 4
                    case 2:
                        v1 = instructions[instructions[pointers[amp_pointer] + 1]
                                          ] if modes_p1 == 0 else instructions[pointers[amp_pointer] + 1]
                        v2 = instructions[instructions[pointers[amp_pointer] + 2]
                                          ] if modes_p2 == 0 else instructions[pointers[amp_pointer] + 2]
                        instructions[instructions[pointers[amp_pointer] + 3]] = v1 * v2
                        pointers[amp_pointer] += 4
                    case 3:
                        progs_started[amp_pointer] = True
                        instructions[instructions[pointers[amp_pointer] + 1]
                                     ] = input_queue.pop()
                        pointers[amp_pointer] += 2
                    case 4:
                        v1 = instructions[instructions[pointers[amp_pointer] + 1]
                                          ] if modes_p1 == 0 else instructions[pointers[amp_pointer] + 1]
                        output.append(v1)
                        pointers[amp_pointer] += 2
                        if progs_started[amp_pointer]:
                            amp_pointer += 1
                            amp_pointer %= 5
                            break
                    case 5:
                        v1 = instructions[instructions[pointers[amp_pointer] + 1]
                                          ] if modes_p1 == 0 else instructions[pointers[amp_pointer] + 1]
                        v2 = instructions[instructions[pointers[amp_pointer] + 2]
                                          ] if modes_p2 == 0 else instructions[pointers[amp_pointer] + 2]
                        if v1 != 0:
                            pointers[amp_pointer] = v2
                        else:
                            pointers[amp_pointer] += 3
                    case 6:
                        v1 = instructions[instructions[pointers[amp_pointer] + 1]
                                          ] if modes_p1 == 0 else instructions[pointers[amp_pointer] + 1]
                        v2 = instructions[instructions[pointers[amp_pointer] + 2]
                                          ] if modes_p2 == 0 else instructions[pointers[amp_pointer] + 2]
                        if v1 == 0:
                            pointers[amp_pointer] = v2
                        else:
                            pointers[amp_pointer] += 3
                    case 7:
                        v1 = instructions[instructions[pointers[amp_pointer] + 1]
                                          ] if modes_p1 == 0 else instructions[pointers[amp_pointer] + 1]
                        v2 = instructions[instructions[pointers[amp_pointer] + 2]
                                          ] if modes_p2 == 0 else instructions[pointers[amp_pointer] + 2]
                        instructions[instructions[pointers[amp_pointer] + 3]
                                     ] = int(v1 < v2)
                        pointers[amp_pointer] += 4
                    case 8:
                        v1 = instructions[instructions[pointers[amp_pointer] + 1]
                                          ] if modes_p1 == 0 else instructions[pointers[amp_pointer] + 1]
                        v2 = instructions[instructions[pointers[amp_pointer] + 2]
                                          ] if modes_p2 == 0 else instructions[pointers[amp_pointer] + 2]
                        instructions[instructions[pointers[amp_pointer] + 3]
                                     ] = int(v1 == v2)
                        pointers[amp_pointer] += 4
                    case 99:
                        amp_pointer += 1
                        break
                    case _:
                        raise ValueError(
                            f"Instruction at pointer {pointers[amp_pointer]} (instruction: {instruction}) is not valid")
        end_signals.append(input_queue.pop())
    return max(end_signals)


# print(part_one(get_input()))
print(part_two(get_input()))
