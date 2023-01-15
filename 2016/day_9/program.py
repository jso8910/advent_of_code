def get_input():
    with open("day_9/input.txt", "r") as f:
        return f.read()


def decompress(text, part_one=True):
    i = 0
    decompressed = 0
    while i < len(text):
        if text[i] == "(":
            end = text.find(")", i)
            length, times = map(int, text[i + 1:end].split("x"))
            sub_str = text[end + 1:end + 1 + length]
            if part_one:
                decompressed += len(sub_str) * times
            elif "(" in sub_str:
                decompressed += decompress(sub_str, False) * times
            else:
                decompressed += len(sub_str) * times
            i = end + 1 + length
        else:
            decompressed += 1
            i += 1
    return decompressed


def part_one(text):
    return decompress(text)


def part_two(text):
    return decompress(text, part_one=False)


print(part_one(get_input()))
print(part_two(get_input()))
