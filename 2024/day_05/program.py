from collections import defaultdict


def get_input():
    with open("day_05/input.txt", "r") as f:
        contents = f.read()
        rules = defaultdict(list)
        for line in contents.split("\n\n")[0].split("\n"):
            rule = line.split("|")
            rules[int(rule[1])].append(int(rule[0]))

        updates = []
        for line in contents.split("\n\n")[1].split("\n"):
            if not line:
                break
            updates.append([int(x) for x in line.split(",")])
        return rules, updates


def part_one(rules, updates):
    total = 0
    for update in updates:
        valid = True
        for idx, num in enumerate(update):
            for num_rule in rules[num]:
                # Each number in the rules list must be before num
                if num_rule in update[idx:]:
                    valid = False
                    break
            if not valid:
                break
        else:
            total += update[len(update) // 2]
    return total


def part_two(rules, updates):
    total = 0
    for update in updates:
        ever_invalid = False
        valid = False
        while not valid:
            valid = True
            for idx, num in enumerate(update):
                for rule_num in rules[num]:
                    # Each number in the rules list must be BEFORE num
                    if rule_num in update[idx:]:
                        valid = False
                        ever_invalid = True
                        rule_num_idx = update.index(rule_num)
                        # Swap the two numbers
                        update[idx], update[rule_num_idx] = update[rule_num_idx], update[idx]
        if ever_invalid:
            total += update[len(update) // 2]
    return total


print(part_one(*get_input()))
print(part_two(*get_input()))
