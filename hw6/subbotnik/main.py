def check(m, param):
    r, c, heights = param
    cnt = 0
    i = 0
    while i < len(heights) - c + 1:
        if heights[i + c - 1] - heights[i] <= m:
            cnt += 1
            i += c
        else:
            i += 1
    return cnt >= r


def lbinsearch(l, r, check, param):
    while l < r:
        m = (l + r) // 2
        if check(m, param):
            r = m
        else:
            l = m + 1
    return l


n, r, c = map(int, input().split())
heights = []
for i in range(n):
    heights.append(int(input()))
heights.sort()

print(lbinsearch(0, heights[-1], check, (r, c, heights)))
