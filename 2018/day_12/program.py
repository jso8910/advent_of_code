from collections import defaultdict


def get_input():
    with open("day_12/input.txt", "r") as f:
        file = f.read().split("\n\n")
    plant_state = defaultdict(bool, {idx: char == "#" for idx,
                                     char in enumerate(file[0].split(": ")[1])})
    rules = defaultdict(bool)
    for line in file[1].split("\n"):
        key = tuple(char == "#" for char in line.split(" => ")[0])
        val = line.split(" => ")[1] == "#"
        rules[key] = val

    return rules, plant_state


def part_one(rules, plant_state):
    for i in range(20):
        new_state = defaultdict(bool)
        for idx in range(min((p for p in plant_state if plant_state[p]), default=0) - 2, max((p for p in plant_state if plant_state[p]), default=0) + 2 + 1):
            pattern = tuple(plant_state[i]
                            for i in range(idx - 2, idx + 2 + 1))
            new_state[idx] = rules[pattern]
        plant_state = new_state

    return sum(key for key in plant_state if plant_state[key])


def part_two(rules, plant_state):
    cache = {}
    for i in range(150):
        """
        I used this code for input analysis
        if i % 10000 == 0 and i != 0:
            print(i)
            for m in range(500):
                print(min(cache[m+1][0]), end=": ")
                for idx, plant in cache[m + 1][0].items():
                    print("#" if plant else ".", end="")
                print(
                    f"\n{sum(key for key in cache[m + 1][0] if cache[m + 1][0][key])}")
        """

        new_state = defaultdict(bool)
        for idx in range(min((p for p in plant_state if plant_state[p]), default=0) - 2, max((p for p in plant_state if plant_state[p]), default=0) + 2 + 1):
            pattern = tuple(plant_state[i]
                            for i in range(idx - 2, idx + 2 + 1))
            new_state[idx] = rules[pattern]
        plant_state = new_state
        """
        Here's the caching code
        cache[i + 1] = (plant_state,
                        sum(key for key in plant_state if plant_state[key]))
        """

    """
    EXPLANATION
    The index of the first plant, after a certain point between 100 and 150, is this:
    N_CYCLE-CONSTANT
    And, there is a constant pattern so, if you start at that index, the pattern of plant cycle is always the same
    So, you simply substract the original number to get the initial index being -CONSTANT and add 50 billion to get 50 billion-CONSTANT
    Cool, right?
    """
    return sum(key-(150)+50_000_000_000 for key in plant_state if plant_state[key])


print(part_one(*get_input()))
print(part_two(*get_input()))
