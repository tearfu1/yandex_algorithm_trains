def check(m, param):
    a, k = param
    summ = 0
    for wire in wires:
        summ += wire // m
    return summ >= k


def rbinsearch(l, r, check, param):
    while l < r:
        m = (l + r + 1) // 2
        if check(m, param):
            l = m
        else:
            r = m - 1
    return l


n, k = map(int, input().split())
wires = []
for i in range(n):
    wires.append(int(input()))
print(rbinsearch(0, max(wires), check, (wires, k)))
