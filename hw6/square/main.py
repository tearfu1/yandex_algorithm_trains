def check(b, param):
    n, m, plates = param
    pp = b * (n + m - 2 * b) - b ** 2
    p = 2 * pp + 2 * b ** 2
    return p <= plates


def rbinsearch(l, r, check, param):
    while l < r:
        m = (l + r + 1) // 2
        if check(m, param):
            l = m
        else:
            r = m - 1
    return l


n = int(input())
m = int(input())
plates = int(input())
print(rbinsearch(0, (min(n, m) - 1) // 2, check, (n, m, plates)))
