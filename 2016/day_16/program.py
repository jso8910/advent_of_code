def get_input():
    with open("day_16/input.txt", "r") as f:
        return f.read()


def invert_bits(num):
    return "".join(["1" if bit == "0" else "0" for bit in num])


def gen_checksum(num_bin_str):
    checksum = ""
    for pair in range(0, len(num_bin_str), 2):
        pair = num_bin_str[pair:pair + 2]
        if pair[0] == pair[1]:
            checksum += "1"
        else:
            checksum += "0"
    if len(checksum) % 2 == 0:
        return gen_checksum(checksum)

    return checksum


def part_one(num):
    while True:
        num = num + "0" + invert_bits(num[::-1])
        if len(num) >= 272:
            return gen_checksum(num[:272])


def part_two(num):
    while True:
        num = num + "0" + invert_bits(num[::-1])
        if len(num) >= 35651584:
            return gen_checksum(num[:35651584])


print(part_one(get_input()))
print(part_two(get_input()))
