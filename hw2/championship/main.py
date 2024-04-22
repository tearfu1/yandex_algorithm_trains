def get_vasiliy_place(throws):
    wp = 0
    ans = 0
    max_vasiliy_throw = 0
    places = {}
    for i in range(len(throws)):
        if throws[i] not in places:
            places[throws[i]] = 1
        else:
            places[throws[i]] += 1
        if throws[i] > throws[wp]:
            wp = i
    for i in range(1, len(throws) - 1):
        if wp < i and throws[i] > throws[i + 1] and throws[i] % 10 == 5:
            if throws[i] > max_vasiliy_throw:
                max_vasiliy_throw = throws[i]

    if max_vasiliy_throw != 0:
        for i in places.keys():
            if i > max_vasiliy_throw:
                ans += places[i]
        ans += 1

    return ans


def main():
    _ = int(input())
    throws = list(map(int, input().split()))
    print(get_vasiliy_place(throws))


main()
