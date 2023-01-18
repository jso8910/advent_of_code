def get_input():
    with open("day_1/input.txt", "r") as f:
        return f.read()


def part_one(digits):
    total = 0
    for i in range(len(digits)):
        if digits[i] == digits[(i + 1) % len(digits)]:
            total += int(digits[i])
    return total


def part_two(digits):
    total = 0
    half = len(digits) // 2
    for i in range(len(digits)):
        if digits[i] == digits[(i + half) % len(digits)]:
            total += int(digits[i])
    return total


print(part_one(get_input()))
print(part_two(get_input()))
