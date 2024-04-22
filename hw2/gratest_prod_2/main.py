import random


def fast(seq):
    seq.sort()
    pm1 = seq[-1]
    pm2 = seq[-2]
    pm3 = seq[-3]
    nm1 = seq[0]
    nm2 = seq[1]

    prod1 = pm1 * pm2 * pm3
    prod2 = prod1 - 1
    if pm1 >= 0:
        prod2 = nm1 * nm2 * pm1

    if prod1 > prod2:
        return pm1, pm2, pm3
    else:
        return nm1, nm2, pm1


def slow(seq):
    m1 = max(seq[0], seq[1], seq[2])
    m3 = min(seq[0], seq[1], seq[2])
    m2 = seq[0] + seq[1] + seq[2] - m1 - m3
    for i in range(len(seq)):
        for j in range(len(seq)):
            for k in range(len(seq)):
                if i != j and i != k and j != k:
                    if seq[i] * seq[j] * seq[k] > m1 * m2 * m3:
                        m1 = seq[i]
                        m2 = seq[j]
                        m3 = seq[k]
    return m1, m2, m3


def main():
    # seq = list(map(int, input().split()))
    # print(*fast(seq))
    # print(*slow(seq))

    while True:
        randvals = [0] * 30
        for i in range(30):
            randvals[i] = random.randint(-100, 100)
        ans_fast = fast(randvals)
        ans_slow = slow(randvals)
        mult_fast = 1
        mult_slow = 1
        for i in range(3):
            mult_fast *= ans_fast[i]
            mult_slow *= ans_slow[i]
        if mult_fast != mult_slow:
            print(randvals)
            print("WA", ans_fast, ans_slow)
            break
        else:
            print("PASS")


main()
