def get_input():
    with open("day_6/input.txt", "r") as f:
        file = f.read().split("\n\n")

    return [s.splitlines() for s in file]


def part_one(groups):
    total_yes = 0
    for group in groups:
        group_set = set()
        for person in group:
            group_set |= set(person)
        total_yes += len(group_set)

    return total_yes


def part_two(groups):
    total_yes = 0
    for group in groups:
        group_set = set("abcdefghijklmnopqrstuvwxyz")
        for person in group:
            group_set &= set(person)
        total_yes += len(group_set)

    return total_yes


print(part_one(get_input()))
print(part_two(get_input()))
