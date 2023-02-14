def get_input():
    with open("day_4/input.txt", "r") as f:
        file = f.read().split("-")
    return range(int(file[0]), int(file[1]) + 1)


def part_one(pwd_range):
    num_valid = 0
    for pwd in pwd_range:
        if sorted(str(pwd)) != list(str(pwd)):
            continue
        for c1, c2 in zip(str(pwd), str(pwd)[1:]):
            if c1 == c2:
                num_valid += 1
                break

    return num_valid


def part_two(pwd_range):
    num_valid = 0
    for pwd in pwd_range:
        if sorted(str(pwd)) != list(str(pwd)):
            continue
        for idx, (c1, c2) in enumerate(zip(str(pwd), str(pwd)[1:])):
            if c1 == c2:
                if idx == 0 and str(pwd)[idx + 2] == c1:
                    continue
                elif idx == len(str(pwd)) - 2 and str(pwd)[idx - 1] == c1:
                    continue
                elif idx > 0 and idx < len(str(pwd)) - 2 and str(pwd)[idx + 2] == c1 or str(pwd)[idx - 1] == c1:
                    continue
                num_valid += 1
                break

    return num_valid


print(part_one(get_input()))
print(part_two(get_input()))
