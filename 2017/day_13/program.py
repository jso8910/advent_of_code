def get_input():
    with open("day_13/input.txt", "r") as f:
        file = f.read().splitlines()

    firewall = {}
    for line in file:
        key = int(line.split(": ")[0])
        value = int(line.split(": ")[1])
        firewall[key] = value

    return firewall


def part_one(firewall):
    severity = 0
    for key, value in firewall.items():
        if key % (2 * (value - 1)) == 0:
            severity += key * value

    return severity


def part_two(firewall):
    delay = 0
    while True:
        caught = False
        for key, value in firewall.items():
            if (key + delay) % (2 * (value - 1)) == 0:
                caught = True
                continue
        if not caught:
            return delay
        delay += 1


print(part_one(get_input()))
print(part_two(get_input()))
