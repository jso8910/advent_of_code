def get_input():
    with open("day_4/input.txt", "r") as f:
        return list(map(lambda x: x.split(), f.read().splitlines()))


def part_one(passphrases):
    valid = 0
    for passphrase in passphrases:
        if len(passphrase) == len(set(passphrase)):
            valid += 1
    return valid


def part_two(passphrases):
    valid = 0
    for passphrase in passphrases:
        valid_passphrase = True
        if len(passphrase) == len(set(passphrase)):
            for word in passphrase:
                for word_2 in passphrase:
                    if word == word_2:
                        continue
                    if sorted(word) == sorted(word_2):
                        valid_passphrase = False
            if valid_passphrase:
                valid += 1
    return valid


print(part_one(get_input()))
print(part_two(get_input()))
