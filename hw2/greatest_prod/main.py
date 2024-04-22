import random


def greatest_prod(seq):
    pos_maxim = max(seq[0], seq[1])
    pos_predmaxim = min(seq[0], seq[1])
    neg_maxim = min(seq[0], seq[1])
    neg_predmaxim = max(seq[0], seq[1])
    if len(seq) > 2:
        for i in range(2, len(seq)):
            if seq[i] >= pos_maxim:
                pos_predmaxim = pos_maxim
                pos_maxim = seq[i]
            elif seq[i] > pos_predmaxim:
                pos_predmaxim = seq[i]

        for i in range(2, len(seq)):
            if seq[i] <= neg_maxim:
                neg_predmaxim = neg_maxim
                neg_maxim = seq[i]
            elif seq[i] < neg_predmaxim:
                neg_predmaxim = seq[i]


    if pos_maxim * pos_predmaxim > neg_maxim * neg_predmaxim:
        return pos_predmaxim, pos_maxim
    else:
        return neg_maxim, neg_predmaxim


def slow(seq):
    a = 0
    b = 0
    for i in range(len(seq)):
        for j in range(len(seq)):
            if i !=j:
                if seq[i] * seq[j] > a * b:
                    a = seq[i]
                    b = seq[j]

    return min(a, b), max(a, b)


def main():
    # seq = list(map(int, input().split()))
    # print(*greatest_prod(seq))
    # print(*slow(seq))

    while True:
        seq = [0] * 30
        for i in range(30):
            seq[i] = random.randint(-1000, 1000)
        ans_fast = greatest_prod(seq)
        ans_slow = slow(seq)
        if ans_fast == ans_slow:
            print("PASS")
        else:
            print(seq)
            print("WA", ans_fast, ans_slow)
            break


main()
