def checkle(m, param):
    num, a = param
    return num >= a[m]


def isContains(num, a):
    res = rbinsearch(0, len(a) - 1, checkle, (num, a))
    if a[res] != num:
        return False
    return True


def rbinsearch(l, r, check, param):
    while l < r:
        m = (l + r + 1) // 2
        if check(m, param):
            l = m
        else:
            r = m - 1
    return l


def main():
    n, k = map(int, input().split())
    a = sorted(list(map(int, input().split())))
    b = list(map(int, input().split()))

    for num in b:
        if isContains(num, a):
            print("YES")
        else:
            print("NO")


main()
