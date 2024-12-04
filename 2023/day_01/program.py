def get_input():
    with open("day_01/input.txt") as f:
        return [line.strip() for line in f]


def part_one(inp):
    processed = [[char for char in line if char.isdigit()] for line in inp]
    return sum([int("".join([line[0], line[-1]])) for line in processed])


def part_two(inp: list[str]):
    total = 0
    numbers = []
    number_translate = {
        "zero": "0",
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }
    for i, line in enumerate(inp):
        new_line = list(line)
        for idx, char in enumerate(line):
            for num in number_translate:
                if line[idx:].startswith(num):
                    new_line[idx] = number_translate[num]
        inp[i] = new_line
    processed = [[char for char in line if char.isdigit()] for line in inp]
    return sum([int("".join([line[0], line[-1]])) for line in processed])


print(part_one(get_input()))
print(part_two(get_input()))
