def gensequence(l, x1, d1, a, c, m):
    seq = [x1]
    d = d1
    for _ in range(l - 1):
        seq.append(seq[-1] + d)
        d = ((a * d + c) % m)
    return seq


def lbinsearch(l, r, check, param):
    while l < r:
        m = (l + r) // 2
        if check(m, param):
            r = m
        else:
            l = m + 1
    return l


def checkisge(index, params):
    seq, x = params
    return seq[index] >= x


def checkisgt(index, params):
    seq, x = params
    return seq[index] > x


def cntless(seq, x):
    ans = lbinsearch(0, len(seq) - 1, checkisge, (seq, x))
    if seq[ans] < x:
        return len(seq)
    return ans


def cntgt(seq, x):
    return len(seq) - cntless(seq, x + 1)


def medianMerge(seq1, seq2):
    l = min(seq1[0], seq2[0])
    r = max(seq1[-1], seq2[-1])
    while l < r:
        m = (l + r) // 2
        less = cntless(seq1, m) + cntless(seq2, m)
        gt = cntgt(seq1, m) + cntgt(seq2, m)
        if less <= len(seq1) - 1 and gt <= len(seq1):
            return m
        if gt > len(seq1):
            l = m + 1
        if less > len(seq1) - 1:
            r = m - 1
    return l


n, l = map(int, input().split())
seqs = []

for i in range(n):
    x1, d1, a, c, m = map(int, input().split())
    seqs.append(gensequence(l, x1, d1, a, c, m))
for i in range(n):
    for j in range(i + 1, n):
        print(medianMerge(seqs[i], seqs[j]))
