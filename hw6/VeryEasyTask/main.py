def check(m, param):
    n, x, y = param
    return (m // x) + (m // y) >= n - 1


def lbinsearch(l, r, check, param):
    while l < r:
        m = (l + r) // 2
        if check(m, param):
            r = m
        else:
            l = m + 1
    return l


n, x, y = map(int, input().split())
if x > y:
    x, y = y, x
print(x + lbinsearch(0, x * n + 1, check, (n, x, y)))
