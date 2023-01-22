def get_input():
    with open("day_2/input.txt", "r") as f:
        return f.read().splitlines()


def part_one(boxes):
    count_2 = 0
    count_3 = 0
    for box in boxes:
        count_2 += any(box.count(letter) ==
                       2 for letter in "abcdefghijklmnopqrstuvwxyz")
        count_3 += any(box.count(letter) ==
                       3 for letter in "abcdefghijklmnopqrstuvwxyz")

    return count_2 * count_3


def part_two(boxes):
    for box in boxes:
        for box_2 in boxes:
            letters = [letter_1 != letter_2 for letter_1,
                       letter_2 in zip(box, box_2)]
            if sum(letters) == 1:
                return box[0:letters.index(True)] + box[letters.index(True) + 1:]


print(part_one(get_input()))
print(part_two(get_input()))
