from pprint import pprint
import math


def get_input():
    with open("day_22/input.txt", "r") as f:
        file = f.read().splitlines()

    instructions = []
    for line in file:
        match line.split(" "):
            case ["deal", "into", "new", "stack"]:
                instructions.append({"op": "deal", "type": "new"})
            case ["deal", "with", "increment", n]:
                instructions.append(
                    {"op": "deal", "type": "increment", "value": int(n)})
            case ["cut", n]:
                n = int(n)
                if n < 0:
                    instructions.append(
                        {"op": "cut", "type": "bottom", "value": abs(n)})
                else:
                    instructions.append(
                        {"op": "cut", "type": "top", "value": abs(n)})
    return instructions


def part_one(instructions):
    LEN_DECK = 10007
    deck = list(range(LEN_DECK))
    for instruction in instructions:
        assert len(deck) == LEN_DECK
        if instruction["op"] == "cut" and instruction["type"] == "top":
            deck = deck[instruction["value"]:] + deck[:instruction["value"]]
        elif instruction["op"] == "cut" and instruction["type"] == "bottom":
            deck = deck[-instruction["value"]:] + deck[:-instruction["value"]]
        elif instruction["op"] == "deal" and instruction["type"] == "new":
            deck = deck[::-1]
        elif instruction["op"] == "deal" and instruction["type"] == "increment":
            inc = instruction["value"]
            new_deck = list(range(LEN_DECK))
            pointer = 0
            while deck:
                new_deck[pointer] = deck.pop(0)
                pointer += inc
                pointer %= len(new_deck)
            deck = new_deck

    return deck.index(2019)


def extended_euclidean(m, n):
    """
    Execute the extended euclidean algorithm for
    values m and n (where m is the length of the deck and
    n is the shuffle increment) in order to find the Bézout coefficients.
    """
    old_r, r = m, n
    old_s, s = 1, 0
    old_t, t = 0, 1

    while r != 0:
        quotient = old_r // r
        old_r, r = r, old_r - quotient * r
        old_s, s = s, old_s - quotient * s
        old_t, t = t, old_t - quotient * t

    return old_s, old_t


def modInverse(b, m):
    g = math.gcd(b, m)
    if (g != 1):
        return -1
    else:
        # If b and m are relatively prime,
        # then modulo inverse is b^(m-2) mode m
        return pow(b, m - 2, m)


# Function to compute a/b under modulo m
def modDivide(a, b, m):
    a = a % m
    inv = modInverse(b, m)
    if (inv == -1):
        return None
    else:
        return (inv*a) % m


def part_two(instructions):
    LEN_DECK = 119315717514047

    def new_deck(a, b):
        return -a, -b+1

    def cut(a, b, n):
        return a, b+n

    def shuffle(a, b, c, n):
        """
        I need to find a coefficient y for which (y*m + 1) mod n equals 0 which I can do using extended euclidean to find a bézout coefficient.
        Essentially, take a number x which this divides into. x = (y*m + 1)/n which rearranges into xn - ym = 1
        This is the form of Bézout's theorem but just subtracting instead of adding. Also, note that n and m must be coprime which is necessary for
        n to be a valid shuffle (and also m in the real problem is prime lol)

        Here I also convert b into a proper number offset. I could _probably_ do this earlier but I can't be bothered, hence the redundant variable b
        """
        x, y = extended_euclidean(n, LEN_DECK)
        return (a * (((-y)*LEN_DECK + 1)//n)), 0, c+a*b
    # ax + b
    a = 1
    # B is only needed in the intermediate
    # It will always be 0 at the end of a shuffle
    b = 0
    c = 0
    for instruction in instructions:
        if instruction["op"] == "cut" and instruction["type"] == "top":
            a, b = cut(a, b, instruction["value"])
        elif instruction["op"] == "cut" and instruction["type"] == "bottom":
            a, b = cut(a, b, -instruction["value"])
        elif instruction["op"] == "deal" and instruction["type"] == "new":
            a, b = new_deck(a, b)
        elif instruction["op"] == "deal" and instruction["type"] == "increment":
            a, b, c = shuffle(a, b, c, instruction["value"])
        a %= LEN_DECK
        b %= LEN_DECK
        c %= LEN_DECK

    # This won't ever occur but whatever
    if b:
        c += a*b

    """
    A transformation can be expressed as f(x) = ax + c mod m (m is the length of the deck).
    f(f(x)) = f(ax+c) = a(ax + c) + c = a^2 x + ac + c mod m. Notice the pattern (sorry my sum notation is weird lol)
    f^n (x) = a^n x + sum[upper=n, k=0](a^k * c) mod m
    The coefficient for a_n is trivial, but c_n isn't immediately obvious. However, you will probably recognize it as a geometric series.
    The first term is c (this is confusing because it's normally notated as a but whatever) and the ratio is equal to a.
    So, the result can be computed as c_n = c*(1-a^n)/(1-a) mod m. For this, you just need to do modular division, shamelessly copied from geeksforgeeks
    """
    cn = modDivide(c*(1-pow(a, 101741582076661, LEN_DECK)), (1-a), LEN_DECK)
    an = pow(a, 101741582076661, LEN_DECK)
    return (an*2020 + cn) % LEN_DECK


print(part_one(get_input()))
print(part_two(get_input()))
