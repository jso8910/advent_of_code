import multiprocessing


def get_input():
    with open("day_5/input.txt", "r") as f:
        return f.read()


def react_polymer(polymer):
    new_polymer = ""
    i = 0
    while i < len(polymer):
        if i + 1 < len(polymer) and abs(ord(polymer[i]) - ord(polymer[i + 1])) == 32:
            i += 2
        else:
            new_polymer += polymer[i]
            i += 1

    return new_polymer


def part_one(polymer):
    old_polymer = ""
    while polymer != old_polymer:
        old_polymer = polymer
        polymer = react_polymer(polymer)

    return len(polymer)


def part_two(polymer):
    min_len = float("inf")
    for letter in "abcdefghijklmnopqrstuvwxyz":
        new_polymer = polymer.replace(letter, "").replace(letter.upper(), "")
        old_polymer = ""
        while new_polymer != old_polymer:
            old_polymer = new_polymer
            new_polymer = react_polymer(new_polymer)
        min_len = min(min_len, len(new_polymer))

    return min_len


print(part_one(get_input()))
print(part_two(get_input()))
