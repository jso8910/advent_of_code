def get_input():
    with open("day_23/input.txt", "r") as f:
        file = f.read().splitlines()

    instructions = []
    for line in file:
        match line.split(" "):
            case ["set", x, y]:
                if y not in "abcdefgh":
                    y = int(y)
                instructions.append(("set", x, y))
            case ["sub", x, y]:
                if y not in "abcdefgh":
                    y = int(y)
                instructions.append(("sub", x, y))
            case ["mul", x, y]:
                if y not in "abcdefgh":
                    y = int(y)
                instructions.append(("mul", x, y))
            case ["jnz", x, y]:
                if x not in "abcdefgh":
                    x = int(x)
                if y not in "abcdefgh":
                    y = int(y)
                instructions.append(("jnz", x, y))
    return instructions


def part_one(instructions):
    registers = {val: 0 for val in "abcdefgh"}
    num_mul = 0
    i_pointer = 0
    while i_pointer < len(instructions):
        instruction = instructions[i_pointer]
        match instruction:
            case ("set", x, y):
                if isinstance(y, str):
                    y = registers[y]
                registers[x] = y
                i_pointer += 1
            case ("sub", x, y):
                if isinstance(y, str):
                    y = registers[y]
                registers[x] -= y
                i_pointer += 1
            case ("mul", x, y):
                if isinstance(y, str):
                    y = registers[y]
                registers[x] *= y
                num_mul += 1
                i_pointer += 1
            case ("jnz", x, y):
                if isinstance(x, str):
                    x = registers[x]
                if isinstance(y, str):
                    y = registers[y]
                if x != 0:
                    i_pointer += y
                else:
                    i_pointer += 1

    return num_mul


def part_two(instructions):
    a = 1
    b = 0
    c = 0
    d = 0
    e = 0
    f = 0
    g = 0
    h = 0

    # Optimized program
    b = 65
    c = b
    if a != 0:
        b *= 100
        b += 100000
        # Value of b = 65*100+100000 = 106,500
        c = b
        c += 17000
        # Value of c = 106,500 + 17,000 = 123,500

    # This loop should run 1001 times (because b is set after the check)
    for b in range(b, c + 1, 17):
        f = 1
        # The two loops are just a b is prime checker
        for d in range(2, int(b**0.5)+1):
            if b % d == 0 and 2 <= b // d < b:
                h += 1
                break

    return h


print(part_one(get_input()))
print(part_two(get_input()))
