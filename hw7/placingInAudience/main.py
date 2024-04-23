from heapq import heappop, heappush
n, d = map(int, input().split())
x = list(map(int, input().split()))
vars = []
for i in range(n):
    vars.append([x[i], -1, i])
    vars.append([x[i] + d, 1, i])
vars.sort()
maxim = 0
seqVar = [1] * n
heap = list(range(1, n + 1))
for i in range(len(vars)):
    if vars[i][1] == -1:
        nextVar = heappop(heap)
        maxim = max(nextVar, maxim)
        seqVar[vars[i][2]] = nextVar
    elif vars[i][1] == 1:
        var = seqVar[vars[i][2]]
        heappush(heap, var)
print(maxim)
print(*seqVar)
