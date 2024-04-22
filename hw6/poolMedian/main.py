n, l = map(int, input().split())
seqs = []
for i in range(n):
    seqs.append(list(map(int, input().split())))

for i in range(n):
    for j in range(i + 1, n):
        ans = [0] * 2 * l
        second = 0
        first = 0
        for k in range(l):
            if (first != l and second == l) or (first != l and seqs[i][first] < seqs[j][second]):
                ans[k] = seqs[i][first]
                first += 1
            else:
                ans[k] = seqs[j][second]
                second += 1

        print(ans[l - 1])
