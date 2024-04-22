import random
from math import ceil


def get_entrance_and_floor(flatno, flatsonfloor, floors):
    floorsbefore = (flatno - 1) // flatsonfloor
    entrance = floorsbefore // floors + 1
    floor = floorsbefore % floors + 1
    return entrance, floor


def check(k1, m, k2, p2, n2, flatsonfloor):
    entrance, floor = get_entrance_and_floor(k2, flatsonfloor, m)
    if entrance == p2 and floor == n2:
        return get_entrance_and_floor(k1, flatsonfloor, m)
    return (-1, -1)


def slow(k1, m, k2, p2, n2):
    ent = -1
    floor = -1
    goodflag = False
    for flatsonfloor in range(1, maxrandval + 1):
        nent, nfloor = check(k1, m, k2, p2, n2, flatsonfloor)
        if nent != -1:
            goodflag = True
            if ent == -1:
                ent, floor = nent, nfloor
            elif ent != nent and ent != 0:
                ent = 0
            elif floor != nfloor and floor != 0:
                floor = 0
    if goodflag:
        return (ent, floor)
    else:
        return (-1, -1)


def fast(k1, m, k2, p2, n2):
    # k1, m, k2, p2, n2 = map(int, input().split())
    p1 = 0
    n1 = 0
    flats = ceil(k2 / (m * (p2 - 1) + n2))
    if (m * (p2 - 1) + (n2 - 1)) * flats < k2 and n2 <= m:
        if p2 == 1 and n2 == 1:
            if k1 <= k2:
                n1 = 1
                p1 = 1
            else:
                if m == 1:
                    p1 = 0
                    n1 = 1
                else:
                    p1 = 1
                    n1 = 0
        else:
            p1 = ceil(k1 / (flats * m))
            n1 = ceil((k1 - (p1 - 1) * (flats * m)) / flats)
            norm_k2_1 = k2 - m * (p2 - 1) * flats
            norm_k2_2 = k2 - m * (p2 - 1) * (flats + 1)
            if (n2 - 1) * flats < norm_k2_1 and (n2 - 1) * (flats + 1) < norm_k2_2 and k1 != k2:
                if not (k1 / flats + 1 <= k1 / (flats + 1) + 1):
                    n1 = 0
    else:
        p1 = -1
        n1 = -1
    return p1, n1
    # print(p1, n1)


maxrandval = 30
while True:
    randvals = [0] * 5
    for i in range(5):
        randvals[i] = random.randint(1, maxrandval)
    k1, m, k2, p2, n2 = randvals
    slowans = slow(k1, m, k2, p2, n2)
    fastans = fast(k1, m, k2, p2, n2)
    if slowans == fastans:
        print(randvals, "OK")
    else:
        print("WA", slowans, fastans, randvals)
        break
