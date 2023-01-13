from collections import defaultdict


def get_input():
    with open("day_2/input.txt") as f:
        file = f.read().splitlines()

    digits = []
    for line in file:
        d = []
        for char in line:
            match char:
                case "D":
                    d.append(1j)
                case "U":
                    d.append(-1j)
                case "R":
                    d.append(1)
                case "L":
                    d.append(-1)
        digits.append(d)

    return digits


def part_one(digits):
    code = ""
    loc = 1 + 1j
    for digit in digits:
        for d in digit:
            loc += d
            if not 0 <= loc.real <= 2 or not 0 <= loc.imag <= 2:
                loc -= d
        code += str(int(loc.real + 3*loc.imag + 1))

    return code


def part_two(digits):
    keypad_str = """
  1
 234
56789
 ABC
  D
    """
    keypad = defaultdict(lambda: None)
    for y, line in enumerate(keypad_str.splitlines()):
        for x, char in enumerate(line):
            if char != " ":
                keypad[x + 1j*y] = char

    code = ""
    loc = 1 + 1j
    for digit in digits:
        for d in digit:
            loc += d
            if not keypad[loc]:
                loc -= d
        code += keypad[loc]

    return code


print(part_one(get_input()))
print(part_two(get_input()))
