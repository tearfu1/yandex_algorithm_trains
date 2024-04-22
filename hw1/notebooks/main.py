import random


def fast(a1, b1, a2, b2):
    # a1, b1, a2, b2 = map(int, input().split())
    if b1 > a1:
        a1, b1 = b1, a1
    if b2 > a2:
        a2, b2 = b2, a2
    a3 = 0
    b3 = 0
    if b1 > a2:
        a3 = b1
        b3 = a1 + b2
    elif b2 > a1:
        a3 = b2
        b3 = a2 + b1
    else:
        a3 = max(a1, a2)
        b3 = b1 + b2
    return a3, b3


def slow(a1, b1, a2, b2):
    a3 = 0
    b3 = 0
    sides = []
    squares = []
    if b1 > a1:
        a1, b1 = b1, a1
    if b2 > a2:
        a2, b2 = b2, a2
    if a2 > a1:
        a2, a1 = a1, a2
        b2, b1 = b1, b2
    s1 = a1 * (b1 + b2)
    sides.append([a1, b1 + b2])
    squares.append(s1)
    s2 = a1 * (b1 + a2)
    sides.append([a1, b1 + a2])
    squares.append(s2)
    s3 = (a1 + b2) * max(b1, a2)
    sides.append([a1 + b2, max(b1, a2)])
    squares.append(s3)
    s4 = (a1 + a2) * max(b1, b2)
    sides.append([a1 + a2, max(b1, b2)])
    squares.append(s4)
    min_s = min(s1, s2, s3, s4)
    ind = squares.index(min_s)
    a3, b3 = sides[ind]
    print(sides)
    return a3, b3


while True:
    randvals = [0] * 4
    for i in range(4):
        randvals[i] = random.randint(1, 1000 + 1)
    a1, b1, a2, b2 = randvals
    a3_slow, b3_slow = slow(a1, b1, a2, b2)
    a3_fast, b3_fast = fast(a1, b1, a2, b2)
    if a3_slow * b3_slow != a3_fast * b3_fast:
        print(randvals)
        print(a3_slow, b3_slow)
        print(a3_fast, b3_fast)
        print("FAIL")
        break
    else:
        print("PASS")
