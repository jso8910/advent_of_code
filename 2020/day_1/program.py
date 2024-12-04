def get_input():
    with open("day_1/input.txt", "r") as f:
        return set(int(n) for n in f.read().splitlines())


def part_one(numbers):
    for num in numbers:
        if 2020 - num in numbers:
            return num * (2020 - num)


def part_two(numbers):
    for num in numbers:
        for num2 in numbers:
            if num == num2:
                continue
            if 2020 - num - num2 in numbers:
                return num * num2 * (2020 - num - num2)


print(part_one(get_input()))
print(part_two(get_input()))
