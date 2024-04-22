def check(m, param):
    n, a, b, w, h = param
    return (w // (a + 2 * m)) * (h // (b + 2 * m)) >= n


def rbinsearch(l, r, check, param):
    while l < r:
        m = (l + r + 1) // 2
        if check(m, param):
            l = m
        else:
            r = m - 1
    return l


n, a, b, w, h = map(int, input().split())
ans1 = rbinsearch(0, max(w, h), check, (n, a, b, w, h))
ans2 = rbinsearch(0, max(w, h), check, (n, b, a, w, h))
print(max(ans1, ans2))
