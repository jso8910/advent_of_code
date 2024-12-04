def get_input():
    with open("day_04/input.txt", "r") as file:
        return file.read().splitlines()


def part_one(grid):
    pattern = "XMAS"
    dirs = [(1, 1), (1, 0), (1, -1), (0, 1), (0, -1), (-1, 1), (-1, 0), (-1, -1)]
    count = 0
    for ridx, line in enumerate(grid):
        for cidx, char in enumerate(line):
            if char != "X":
                continue
            for d_r, d_c in dirs:
                for i in range(len(pattern)):
                    if ridx + i * d_r < 0 or ridx + i * d_r >= len(grid):
                        break
                    if cidx + i * d_c < 0 or cidx + i * d_c >= len(line):
                        break
                    if grid[ridx + i * d_r][cidx + i * d_c] != pattern[i]:
                        break
                else:  # executed if loop completes without break
                    count += 1
    return count


def part_two(grid):
    count = 0
    opposites = {"S": "M", "M": "S"}
    # This only starts from the top left corner to avoid quadruple counting X-MASes
    for ridx, line in enumerate(grid):
        for cidx, char in enumerate(line):
            if char in "AX":
                continue

            # First, check whether the two same characters are in the same row
            if cidx + 2 < len(line) and line[cidx] == line[cidx + 2]:
                if (
                    ridx + 2 < len(grid)
                    and grid[ridx + 2][cidx] == grid[ridx + 2][cidx + 2] == opposites[line[cidx]]
                    and grid[ridx + 1][cidx + 1] == "A"
                ):
                    count += 1
            # Then, check whether the two same characters are in the same column
            elif ridx + 2 < len(grid) and grid[ridx][cidx] == grid[ridx + 2][cidx]:
                if (
                    cidx + 2 < len(line)
                    and grid[ridx][cidx + 2] == grid[ridx + 2][cidx + 2] == opposites[grid[ridx][cidx]]
                    and grid[ridx + 1][cidx + 1] == "A"
                ):
                    count += 1
            else:
                continue
    return count


print(part_one(get_input()))
print(part_two(get_input()))
