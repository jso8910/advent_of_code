from collections import defaultdict


def get_input():
    with open("day_25/input.txt", "r") as f:
        file = f.read().split("\n\n")
    states = {}
    for state in file[1:]:
        state_list = []
        for line in state.splitlines():
            match line.strip(" \t:-.").split(" "):
                case ["In", "state", letter]:
                    state_letter = letter
                case ["If", "the", "current", "value", "is", "0" | "1"]:
                    state_list.append({})
                case ["Write", "the", "value", n]:
                    state_list[-1]["new_val"] = int(n)
                case ["Move", "one", "slot", "to", "the", dir]:
                    state_list[-1]["dir"] = 1 if dir == "right" else -1
                case ["Continue", "with", "state", n_state]:
                    state_list[-1]["next"] = n_state
        states[state_letter] = state_list
    return (
        int(file[0].splitlines()[1].split(" ")[-2]),
        file[0].splitlines()[0].split(" ")[-1].strip("."),
        states
    )


def part_one(num_iters, state, rules):
    state = "A"
    tape = defaultdict(int)
    pointer = 0
    for i in range(num_iters):
        c = rules[state][tape[pointer]]
        tape[pointer] = c["new_val"]
        pointer += c["dir"]
        state = c["next"]

    return sum(tape.values())


print(part_one(*get_input()))
