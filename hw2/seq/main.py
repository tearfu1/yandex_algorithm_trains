def sym(seq):
    for start in range(len(seq)):
        i = start
        j = len(seq) - 1
        while i < len(seq) and seq[i] == seq[j] and j >= 0 and i <= j:
            i += 1
            j -= 1
            if i > j:
                ans = []
                for i in range(start - 1, -1, -1):
                    ans.append(seq[i])
                return ans


n = int(input())
a = list(map(int, input().split()))
ans = sym(a)
print(len(ans))
print(*ans)
