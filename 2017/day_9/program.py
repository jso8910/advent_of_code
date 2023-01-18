def get_input():
    with open("day_9/input.txt", "r") as f:
        return f.read()


def part_one(stream):
    current_depth = 1
    score = 0
    garbage = False
    canceled_next = False
    for char in stream:
        if char == "{" and not garbage:
            score += current_depth
            current_depth += 1
        elif char == "}" and not garbage:
            current_depth -= 1
        elif char == "<" and not garbage:
            garbage = True
        elif char == ">" and garbage and not canceled_next:
            garbage = False
        elif char == "!" and garbage and not canceled_next:
            canceled_next = True
        elif canceled_next:
            canceled_next = False

    return score


def part_two(stream):
    amount_garbage = 0
    garbage = False
    canceled_next = False
    for char in stream:
        if char == "<" and not garbage:
            garbage = True
        elif char == ">" and garbage and not canceled_next:
            garbage = False
        elif char == "!" and garbage and not canceled_next:
            canceled_next = True
        elif canceled_next:
            canceled_next = False
        elif garbage:
            amount_garbage += 1

    return amount_garbage


print(part_one(get_input()))
print(part_two(get_input()))
