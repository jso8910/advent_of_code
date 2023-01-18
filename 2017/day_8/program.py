from collections import defaultdict


def get_input():
    with open("day_8/input.txt", "r") as f:
        file = f.read().splitlines()

    instructions = []
    for line in file:
        match line.split(" "):
            case [reg, op_name, val, "if", reg2, op, val2]:
                instructions.append({"register": reg, "operation": op_name, "value": int(
                    val), "condition": {"register": reg2, "operator": op, "value": int(val2)}})

    return instructions


def part_one(instructions):
    registers = defaultdict(int)
    for instruction in instructions:
        def op(): return None
        match instruction["operation"]:
            case "inc":
                def op(): registers[instruction["register"]
                                    ] += instruction["value"]
            case "dec":
                def op(): registers[instruction["register"]
                                    ] -= instruction["value"]
        match instruction["condition"]["operator"]:
            case ">":
                if registers[instruction["condition"]["register"]] > instruction["condition"]["value"]:
                    op()
            case "<":
                if registers[instruction["condition"]["register"]] < instruction["condition"]["value"]:
                    op()
            case ">=":
                if registers[instruction["condition"]["register"]] >= instruction["condition"]["value"]:
                    op()
            case "<=":
                if registers[instruction["condition"]["register"]] <= instruction["condition"]["value"]:
                    op()
            case "==":
                if registers[instruction["condition"]["register"]] == instruction["condition"]["value"]:
                    op()
            case "!=":
                if registers[instruction["condition"]["register"]] != instruction["condition"]["value"]:
                    op()

    return max(registers.values())


def part_two(instructions):
    registers = defaultdict(int)
    max_value = 0
    for instruction in instructions:
        def op(): return None
        match instruction["operation"]:
            case "inc":
                def op(): registers[instruction["register"]
                                    ] += instruction["value"]
            case "dec":
                def op(): registers[instruction["register"]
                                    ] -= instruction["value"]
        match instruction["condition"]["operator"]:
            case ">":
                if registers[instruction["condition"]["register"]] > instruction["condition"]["value"]:
                    op()
            case "<":
                if registers[instruction["condition"]["register"]] < instruction["condition"]["value"]:
                    op()
            case ">=":
                if registers[instruction["condition"]["register"]] >= instruction["condition"]["value"]:
                    op()
            case "<=":
                if registers[instruction["condition"]["register"]] <= instruction["condition"]["value"]:
                    op()
            case "==":
                if registers[instruction["condition"]["register"]] == instruction["condition"]["value"]:
                    op()
            case "!=":
                if registers[instruction["condition"]["register"]] != instruction["condition"]["value"]:
                    op()
        max_value = max(max(registers.values()), max_value)

    return max_value


print(part_one(get_input()))
print(part_two(get_input()))
