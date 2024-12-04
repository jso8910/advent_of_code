def get_input():
    with open("day_5/input.txt", "r") as f:
        file = f.read().splitlines()

    boarding_passes = []
    for line in file:
        boarding_pass = {}
        boarding_pass["row"] = line[:7]
        boarding_pass["seat"] = line[7:]
        boarding_passes.append(boarding_pass)

    return boarding_passes


def part_one(boarding_passes):
    highest_id = -1
    for bp in boarding_passes:
        lower = 0
        upper = 127
        for char in bp["row"]:
            if char == "B":
                lower = upper - (upper - lower + 1) / 2 + 1
            elif char == "F":
                upper = upper - (upper - lower + 1) / 2
        row = int(upper)
        lower = 0
        upper = 7
        for char in bp["seat"]:
            if char == "R":
                lower = upper - (upper - lower + 1) / 2 + 1
            elif char == "L":
                upper = upper - (upper - lower + 1) / 2

        seat = int(upper)
        if row * 8 + seat > highest_id:
            highest_id = row * 8 + seat

    return highest_id


def part_two(boarding_passes):
    seats = []
    for bp in boarding_passes:
        lower = 0
        upper = 127
        for char in bp["row"]:
            if char == "B":
                lower = upper - (upper - lower + 1) / 2 + 1
            elif char == "F":
                upper = upper - (upper - lower + 1) / 2
        row = int(upper)
        lower = 0
        upper = 7
        for char in bp["seat"]:
            if char == "R":
                lower = upper - (upper - lower + 1) / 2 + 1
            elif char == "L":
                upper = upper - (upper - lower + 1) / 2

        seat = int(upper)
        seats.append((row, seat))

    max_row = max(s[0] for s in seats)
    min_row = min(s[0] for s in seats)
    for row in range(min_row + 1, max_row):
        for s in range(8):
            if (row, s) not in seats:
                return row * 8 + s


print(part_one(get_input()))
print(part_two(get_input()))
