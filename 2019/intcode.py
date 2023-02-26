def leading_zeros(number):
    return f"{number:05d}"


def get_value(instructions, mode, param_num, pointer, relative_base):
    if mode == 2:
        return instructions[relative_base + instructions[pointer + param_num]]
    elif mode == 1:
        return instructions[pointer + param_num]
    elif mode == 0:
        return instructions[instructions[pointer + param_num]]


def get_inp_pointer(instructions, mode, param_num, pointer, relative_base):
    if mode == 2:
        return relative_base + instructions[pointer + param_num]
    elif mode == 0:
        return instructions[pointer + param_num]


class Intcode:
    def run(self, instructions, input_queue, pointer=0, relative_base=0):
        self.program = instructions
        output = []
        while pointer < len(instructions):
            input_requested = False
            instruction = leading_zeros(instructions[pointer])
            modes_p1 = int(instruction[2])
            modes_p2 = int(instruction[1])
            modes_p3 = int(instruction[0])
            match int(instruction) % 100:
                case 1:
                    v1 = get_value(instructions, modes_p1,
                                   1, pointer, relative_base)
                    v2 = get_value(instructions, modes_p2,
                                   2, pointer, relative_base)
                    instructions[get_inp_pointer(
                        instructions, modes_p3, 3, pointer, relative_base)] = v1 + v2
                    pointer += 4
                case 2:
                    v1 = get_value(instructions, modes_p1,
                                   1, pointer, relative_base)
                    v2 = get_value(instructions, modes_p2,
                                   2, pointer, relative_base)
                    instructions[get_inp_pointer(
                        instructions, modes_p3, 3, pointer, relative_base)] = v1 * v2
                    pointer += 4
                case 3:
                    # If the stupid user didn't send an input, prompt them
                    if input_queue:
                        instructions[get_inp_pointer(
                            instructions, modes_p1, 1, pointer, relative_base)] = input_queue.popleft()
                        pointer += 2
                    else:
                        input_requested = True
                case 4:
                    v1 = get_value(instructions, modes_p1,
                                   1, pointer, relative_base)
                    output.append(v1)
                    pointer += 2
                case 5:
                    v1 = get_value(instructions, modes_p1,
                                   1, pointer, relative_base)
                    v2 = get_value(instructions, modes_p2,
                                   2, pointer, relative_base)
                    if v1 != 0:
                        pointer = v2
                    else:
                        pointer += 3
                case 6:
                    v1 = get_value(instructions, modes_p1,
                                   1, pointer, relative_base)
                    v2 = get_value(instructions, modes_p2,
                                   2, pointer, relative_base)
                    if v1 == 0:
                        pointer = v2
                    else:
                        pointer += 3
                case 7:
                    v1 = get_value(instructions, modes_p1,
                                   1, pointer, relative_base)
                    v2 = get_value(instructions, modes_p2,
                                   2, pointer, relative_base)
                    instructions[get_inp_pointer(
                        instructions, modes_p3, 3, pointer, relative_base)] = int(v1 < v2)
                    pointer += 4
                case 8:
                    v1 = get_value(instructions, modes_p1,
                                   1, pointer, relative_base)
                    v2 = get_value(instructions, modes_p2,
                                   2, pointer, relative_base)
                    instructions[get_inp_pointer(
                        instructions, modes_p3, 3, pointer, relative_base)] = int(v1 == v2)
                    pointer += 4
                case 9:
                    v1 = get_value(instructions, modes_p1,
                                   1, pointer, relative_base)
                    relative_base += v1
                    pointer += 2
                case 99:
                    break
                case _:
                    raise ValueError(
                        f"Instruction at pointer {pointer} (instruction: {instruction}) is not valid")
            yield instruction, output, input_queue, input_requested, pointer, relative_base
