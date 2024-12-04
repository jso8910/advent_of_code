import re


def get_input():
    with open("day_4/input.txt", "r") as f:
        file = [s.split("\n") for s in f.read().split("\n\n")]

    passports = []
    for p in file:
        passport = {}
        for line in p:
            for field in line.split(" "):
                passport[field.split(":")[0]] = field.split(":")[1]
        passports.append(passport)

    return passports


def part_one(passports):
    fields = {
        "byr",
        "iyr",
        "eyr",
        "hgt",
        "hcl",
        "ecl",
        "pid",
        "cid"
    }
    num_valid = 0
    # print(passports[0])
    for passport in passports:
        if fields - set(passport.keys()) in (set(), set(("cid",))):
            num_valid += 1

    return num_valid


def part_two(passports):
    fields = {
        "byr",
        "iyr",
        "eyr",
        "hgt",
        "hcl",
        "ecl",
        "pid",
        "cid"
    }
    num_valid = 0
    # print(passports[0])
    for passport in passports:
        if fields - set(passport.keys()) not in (set(), set(("cid",))):
            # num_valid += 1
            continue
        if not (1920 <= int(passport["byr"]) <= 2002):
            continue
        if not (2010 <= int(passport["iyr"]) <= 2020):
            continue
        if not (2020 <= int(passport["eyr"]) <= 2030):
            continue
        match passport["hgt"][-2:]:
            case "in":
                if not (59 <= int(passport["hgt"][:-2]) <= 76):
                    continue
            case "cm":
                if not (150 <= int(passport["hgt"][:-2]) <= 193):
                    continue
            case _:
                continue

        if not re.fullmatch("#[0-9a-f]{6}", passport["hcl"]):
            continue

        if not passport["ecl"] in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
            continue

        if not re.fullmatch("[0-9]{9}", passport["pid"]):
            continue
        num_valid += 1

    return num_valid


print(part_one(get_input()))
print(part_two(get_input()))
