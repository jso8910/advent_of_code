import re


def get_input():
    with open("day_2/input.txt", "r") as f:
        file = f.read().splitlines()

    prog = re.compile("(\d+)-(\d+) ([a-z]): ([a-z]+)")
    policies = []
    for line in file:
        policy = {}
        match = prog.match(line)
        policy["password"] = match.group(4)
        policy["min_num"] = int(match.group(1))
        policy["max_num"] = int(match.group(2))
        policy["char"] = match.group(3)
        policies.append(policy)

    return policies


def part_one(policies):
    num_valid = 0
    for policy in policies:
        if policy["password"].count(policy["char"]) in range(policy["min_num"], policy["max_num"] + 1):
            num_valid += 1

    return num_valid


def part_two(policies):
    num_valid = 0
    for policy in policies:
        first_char_match = policy["password"][policy["min_num"] -
                                              1] == policy["char"]
        second_char_match = policy["password"][policy["max_num"] -
                                               1] == policy["char"]
        # One but not the other
        if first_char_match + second_char_match == 1:
            num_valid += 1

    return num_valid


print(part_one(get_input()))
print(part_two(get_input()))
