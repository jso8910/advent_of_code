from hashlib import md5


def get_input():
    with open('day_5/input.txt') as f:
        return f.read()


def part_one(key):
    i = 0
    pwd = ''
    while len(pwd) < 8:
        res = md5((key + str(i)).encode('utf-8')).hexdigest()
        if res[0:5] == '00000':
            pwd += res[5]
        i += 1

    return pwd


def part_two(key):
    i = 0
    pwd = ['' for _ in range(8)]
    while len(list(l for l in pwd if l)) < 8:
        res = md5((key + str(i)).encode('utf-8')).hexdigest()
        if res[0:5] == '00000' and res[5].isdigit() and int(res[5]) < 8 and pwd[int(res[5])] == '':
            pwd[int(res[5])] = res[6]
        i += 1

    return "".join(pwd)


print(part_one(get_input()))
print(part_two(get_input()))
