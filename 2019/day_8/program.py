def get_input():
    with open("day_8/input.txt", "r") as f:
        return list(map(int, f.read()))


def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]


def part_one(transmission):
    images = list(chunks(transmission, 25*6))
    m_zeros = min(images, key=lambda x: x.count(0))
    return m_zeros.count(1) * m_zeros.count(2)


def part_two(transmission):
    images = list(chunks(transmission, 25*6))
    final_image = [2 for _ in range(25*6)]
    for layer in images:
        if all(f != 2 for f in final_image):
            break
        for idx, pixel in enumerate(layer):
            if final_image[idx] == 2:
                final_image[idx] = pixel

    s = ""
    for idx, pixel in enumerate(final_image):
        s += "█" if pixel else " "
        if (idx+1) % 25 == 0:
            s += "\n"
    return s


print(part_one(get_input()))
print(part_two(get_input()))
