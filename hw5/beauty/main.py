def main():
    n, k = map(int, input().split())

    seq = list(map(int, input().split()))
    begin = 0
    end = 0
    minim = float("inf")
    ans = [1, 1]
    cur_seq = {}
    for i in range(n):
        while end < n and len(cur_seq) != k:
            if seq[end] not in cur_seq:
                cur_seq[seq[end]] = 1
            else:
                cur_seq[seq[end]] += 1
            end += 1
        if len(cur_seq) == k:
            if end - begin < minim:
                minim = end - begin
                ans = [begin + 1, end]
        cur_seq[seq[begin]] -= 1
        if cur_seq[seq[begin]] == 0:
            del cur_seq[seq[begin]]
        begin += 1
    print(*ans)


main()
