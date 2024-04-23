n, m = map(int, input().split())
segmentsAndPoints = []
for i in range(n):
    ai, bi = map(int, input().split())
    segmentsAndPoints.append([min(ai, bi), -1])
    segmentsAndPoints.append([max(ai, bi), 1])
points = list(map(int, input().split()))


for i in range(m):
    segmentsAndPoints.append([points[i], 0, i])
del points
segmentsAndPoints.sort()
nowCnt = 0
ans = [""] * m
for i in range(len(segmentsAndPoints)):
    nowCnt += segmentsAndPoints[i][1] * (-1)
    if segmentsAndPoints[i][1] == 0:
        ans[segmentsAndPoints[i][2]] = str(nowCnt)

print(*ans)
