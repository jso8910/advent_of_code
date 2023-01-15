import re


def get_input():
    with open("day_7/input.txt", "r") as f:
        file = f.read().splitlines()

    ips = []
    for line in file:
        hypernets = re.findall(r"\[(\w+)\]", line)
        line = re.sub(r"\[(\w+)\]", " ", line)
        ips.append({"line": line, "hypernets": hypernets})

    return ips


def abba(text):
    for idx in range(1, len(text) - 2):
        if text[idx] == text[idx + 1] and text[idx] != text[idx - 1]:
            if text[idx - 1] == text[idx + 2]:
                return True

    return False


def find_abas(text):
    abas = []
    for idx in range(1, len(text) - 1):
        if " " != text[idx - 1] == text[idx + 1] != text[idx]:
            abas.append(text[idx - 1] + text[idx] + text[idx + 1])

    return abas


def has_corresponding_bab(text, aba):
    for idx in range(1, len(text) - 1):
        if text[idx - 1] == aba[1] and text[idx] == aba[0] and text[idx + 1] == aba[1]:
            return True

    return False


def part_one(ips):
    tls_valid = 0
    for ip in ips:
        if abba(ip["line"]) and not abba(" ".join(ip["hypernets"])):
            tls_valid += 1

    return tls_valid


def part_two(ips):
    ssl_valid = 0
    for ip in ips:
        abas = find_abas(ip["line"])
        bab = any(has_corresponding_bab(
            " ".join(ip["hypernets"]), aba) for aba in abas)
        if bab:
            ssl_valid += 1

    return ssl_valid


print(part_one(get_input()))
print(part_two(get_input()))
