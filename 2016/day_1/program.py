def get_input():
    with open("day_1/input.txt") as f:
        file = f.read().split(", ")

    instructions = []
    for thing in file:
        instructions.append((thing[0], int(thing[1:])))

    return instructions


def part_one(instructions):
    current_loc = 0 + 0j
    current_dir = -1j
    for instruction in instructions:
        if instruction[0] == "R":
            match current_dir:
                case 1j:
                    current_dir = 1
                case 1:
                    current_dir = -1j
                case -1j:
                    current_dir = -1
                case -1:
                    current_dir = 1j
        else:
            match current_dir:
                case 1j:
                    current_dir = -1
                case 1:
                    current_dir = 1j
                case -1j:
                    current_dir = 1
                case -1:
                    current_dir = -1j

        current_loc += current_dir * instruction[1]

    return int(abs(current_loc.real) + abs(current_loc.imag))


def part_two(instructions):
    current_loc = 0 + 0j
    current_dir = -1j
    visited_locs = {current_loc}
    for instruction in instructions:
        if instruction[0] == "R":
            match current_dir:
                case 1j:
                    current_dir = -1
                case 1:
                    current_dir = 1j
                case -1j:
                    current_dir = 1
                case -1:
                    current_dir = -1j
        else:
            match current_dir:
                case 1j:
                    current_dir = 1
                case 1:
                    current_dir = -1j
                case -1j:
                    current_dir = -1
                case -1:
                    current_dir = 1j

        locs = {current_loc + current_dir *
                i for i in range(1, instruction[1] + 1)}
        current_loc += current_dir * instruction[1]
        # if current_loc in visited_locs:
        #     break
        old_visited = visited_locs.copy()
        [visited_locs.add(l) for l in locs]
        if visited_locs - locs != old_visited:
            current_loc, = locs - (visited_locs - old_visited)
            break

    return int(abs(current_loc.real) + abs(current_loc.imag))


print(part_one(get_input()))
print(part_two(get_input()))
