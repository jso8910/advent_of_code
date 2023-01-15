import string


def get_input():
    with open('day_4/input.txt') as f:
        file = f.read().splitlines()

    names = []
    for line in file:
        name = line.split('-')
        name_str = '-'.join(name[:-1])
        sector_id = int(name[-1].split('[')[0])
        checksum = name[-1].split("[")[1].replace("]", "")
        names.append([name_str, sector_id, checksum])

    return names


def part_one(names):
    sum_sector_ids = 0
    for name in names:
        letters = {}
        for letter in name[0]:
            if letter.isalpha():
                if letter in letters:
                    letters[letter] += 1
                else:
                    letters[letter] = 1
        letters = sorted(letters.items(), key=lambda x: (-x[1], x[0]))
        letters = ''.join([letter[0] for letter in letters])
        if letters[:5] == name[2]:
            sum_sector_ids += name[1]

    return sum_sector_ids


def caesar(n):
    az = string.ascii_lowercase
    n = n % 26
    return str.maketrans(az, az[n:] + az[:n])


def part_two(names):
    # sum_sector_ids = 0
    real_rooms = []
    for name in names:
        name = name.copy()
        letters = {}
        for letter in name[0]:
            if letter.isalpha():
                if letter in letters:
                    letters[letter] += 1
                else:
                    letters[letter] = 1
        letters = sorted(letters.items(), key=lambda x: (-x[1], x[0]))
        letters = ''.join([letter[0] for letter in letters])
        if letters[:5] == name[2]:
            real_rooms.append(name)

    for room in real_rooms:

        room[0] = room[0].translate(caesar(room[1]))
        if 'north' in room[0].lower():
            str.maketrans
            return room[1]


print(part_one(get_input()))
print(part_two(get_input()))
