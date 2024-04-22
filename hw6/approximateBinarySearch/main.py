def checkle(m, param):
    num, a = param
    return a[m] <= num


def checkge(m, param):
    num, a = param
    return a[m] >= num


def apprContains(num, a):
    resmin = rbinsearch(0, len(a) - 1, checkle, (num, a))
    resmax = lbinsearch(0, len(a) - 1, checkge, (num, a))

    if abs(a[resmin] - num) <= abs(a[resmax] - num):
        return a[resmin]
    return a[resmax]


def lbinsearch(l, r, check, param):
    while l < r:
        m = (l + r) // 2
        if check(m, param):
            r = m
        else:
            l = m + 1
    return l


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
        print(apprContains(num, a))


main()
