from hashlib import md5
import re


def get_input():
    with open("day_14/input.txt", "r") as f:
        return f.read()


def hash_stretch(hashes):
    for i in range(len(hashes)):
        for _ in range(2016):
            hashes[i] = md5(hashes[i].encode('utf-8')).hexdigest()

    return hashes


def gen_hashes(salt, start_index, n, part_2=False):
    hashes = []
    for i in range(start_index, start_index + n + 1):
        hashes.append(md5((salt + str(i)).encode('utf-8')).hexdigest())

    if part_2:
        hashes = hash_stretch(hashes)
    return hashes


def part_one(salt):
    hash_list = gen_hashes(salt, 0, 1000)
    num_keys = 0
    i = -1
    while num_keys != 64:
        i += 1
        if len(hash_list) <= i:
            hash_list += gen_hashes(salt, len(hash_list), 10000)
        match = re.search(r"([a-z0-9A-Z])\1\1", hash_list[i])
        # print(match)
        if match:
            c = match.group(1)
            if len(hash_list) < i + 1002:
                hash_list += gen_hashes(salt, len(hash_list), 1010)
            for j in range(i + 1, i + 1002):
                if c * 5 in hash_list[j]:
                    num_keys += 1
                    break

    return i


def part_two(salt):
    hash_list = gen_hashes(salt, 0, 1000, part_2=True)
    num_keys = 0
    i = -1
    while num_keys != 64:
        i += 1
        if len(hash_list) <= i:
            hash_list += gen_hashes(salt, len(hash_list), 10000, part_2=True)
        match = re.search(r"([a-z0-9A-Z])\1\1", hash_list[i])
        # print(match)
        if match:
            c = match.group(1)
            if len(hash_list) < i + 1002:
                hash_list += gen_hashes(salt, len(hash_list),
                                        1010, part_2=True)
            for j in range(i + 1, i + 1002):
                if c * 5 in hash_list[j]:
                    num_keys += 1
                    break

    return i


print(part_one(get_input()))
print(part_two(get_input()))
