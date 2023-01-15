def get_input():
    with open("day_10/input.txt", "r") as f:
        file = f.read().splitlines()

    instructions = []
    bot_rules = {}
    for line in file:
        match line.split(" "):
            case ["value", value, "goes", "to", "bot", bot]:
                instructions.append({"value": int(value), "bot": int(bot)})
            case ["bot", bot, "gives", "low", "to", low_type, low, "and", "high", "to", high_type, high]:
                # print(low_type == "output", bot, bot == "138")
                bot_rules[int(bot)] = {
                    "low_type": low_type,
                    "low": int(low),
                    "high_type": high_type,
                    "high": int(high)
                }
            # case _:
            #     print("Unknown instruction:", line)

    return instructions, bot_rules


def part_one(instructions, bot_rules):
    bot_comparisons = {}

    for instruction in instructions:
        match instruction:
            case {"value": value, "bot": bot}:
                if bot not in bot_comparisons:
                    bot_comparisons[bot] = {
                        "values": set(), "rule": bot_rules[bot]}
                bot_comparisons[bot]["values"].add(value)

    while True:
        for bot in list(bot_comparisons.keys()):
            if len(bot_comparisons[bot]["values"]) < 2:
                continue
            if bot_comparisons[bot]["values"] == {17, 61}:
                return bot
            rule = bot_comparisons[bot]["rule"]
            if rule["low_type"] == "bot":
                if rule["low"] not in bot_comparisons:
                    bot_comparisons[rule["low"]] = {
                        "values": set(), "rule": bot_rules[rule["low"]]}
                bot_comparisons[rule["low"]]["values"].add(
                    list(sorted(bot_comparisons[bot]["values"]))[0])
            if rule["high_type"] == "bot":
                if rule["high"] not in bot_comparisons:
                    bot_comparisons[rule["high"]] = {
                        "values": set(), "rule": bot_rules[rule["high"]]}
                bot_comparisons[rule["high"]]["values"].add(
                    list(sorted(bot_comparisons[bot]["values"]))[1])


def part_two(instructions, bot_rules):
    bot_comparisons = {}
    outputs = {}

    for instruction in instructions:
        match instruction:
            case {"value": value, "bot": bot}:
                if bot not in bot_comparisons:
                    bot_comparisons[bot] = {
                        "values": set(), "rule": bot_rules[bot]}
                bot_comparisons[bot]["values"].add(value)

    while list(sorted(bot_comparisons.keys())) != list(sorted(bot_rules.keys())) or not all(outputs.get(i, None) for i in range(3)):
        for bot in list(bot_comparisons.keys()):
            if len(bot_comparisons[bot]["values"]) < 2:
                continue
            rule = bot_comparisons[bot]["rule"]
            if rule["low_type"] == "bot":
                if rule["low"] not in bot_comparisons:
                    bot_comparisons[rule["low"]] = {
                        "values": set(), "rule": bot_rules[rule["low"]]}
                bot_comparisons[rule["low"]]["values"].add(
                    list(sorted(bot_comparisons[bot]["values"]))[0])
            else:
                outputs[rule["low"]
                        ] = list(sorted(bot_comparisons[bot]["values"]))[0]
            if rule["high_type"] == "bot":
                if rule["high"] not in bot_comparisons:
                    bot_comparisons[rule["high"]] = {
                        "values": set(), "rule": bot_rules[rule["high"]]}
                bot_comparisons[rule["high"]]["values"].add(
                    list(sorted(bot_comparisons[bot]["values"]))[1])
            else:
                outputs[rule["high"]
                        ] = list(sorted(bot_comparisons[bot]["values"]))[1]

    return outputs[0] * outputs[1] * outputs[2]


print(part_one(*get_input()))
print(part_two(*get_input()))
