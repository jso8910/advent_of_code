def get_input():
    with open("day_02/input.txt", "r") as f:
        return [[int(x) for x in l.split()] for l in f.readlines()]


def check_row_safe(row):
    diff = [row[i + 1] - row[i] for i in range(len(row) - 1)]
    # Absolute difference between each item can't be more than 3 or less than 1
    if any(abs(e) < 1 or abs(e) > 3 for e in diff):
        return False

    # Must be all positive or all negative
    if not (all(e > 0 for e in diff) or all(e < 0 for e in diff)):
        return False
    return True


def part_one(inp):
    num_safe = 0
    for row in inp:
        num_safe += check_row_safe(row)
    return num_safe


def part_two(inp):
    num_safe = 0
    for idx, row in enumerate(inp):
        if check_row_safe(row):
            num_safe += 1
            continue
        # otherwise we need to remove one element and check if it's safe
        # remember we're removing an element from a row, not a difference
        for removed_idx in range(len(row)):
            new_row = row[:removed_idx] + row[removed_idx + 1 :]
            if check_row_safe(new_row):
                num_safe += 1
                break
            # else:
            #     print(new_row, new_diffs, original_row, removed_idx, original_row[removed_idx])
    return num_safe


print(part_one(get_input()))
print(part_two(get_input()))
