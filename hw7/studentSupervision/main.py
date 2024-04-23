n, m = map(int, input().split())
begins = []
ends = []
for i in range(m):
    begin, end = map(int, input().split())
    begins.append(begin)
    ends.append(end)

spectated = []
for i in range(m):
    spectated.append([begins[i], -1])
    spectated.append([ends[i], 1])

spectated.sort()

spectatedCnt = 0
spectatedSum = 0
for i in range(len(spectated)):
    if spectatedCnt > 0:
        if spectatedCnt == 1 and spectated[i-1][1] == -1:
            spectatedSum += 1
        spectatedSum += spectated[i][0] - spectated[i - 1][0]
    if spectated[i][1] == -1:
        spectatedCnt += 1
    else:
        spectatedCnt -= 1
print(n - spectatedSum)
