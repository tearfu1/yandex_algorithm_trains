def nearest_num(mas, num):
    ans = 0
    dif = float("inf")
    for i in mas:
        if abs(num - i) < dif:
            ans = i
            dif = abs(num - i)
    return ans


def main():
    n = int(input())
    mas = list(map(int, input().split()))
    x = int(input())
    print(nearest_num(mas, x))


main()
