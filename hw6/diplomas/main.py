w, h, n = map(int, input().split())

l = 0
r = max(w, h) * n
while l < r:
    m = (l + r) // 2
    if (m // w) * (m // h) < n:
        l = m + 1
    else:
        r = m
print(r)
