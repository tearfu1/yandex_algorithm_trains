def countPrefixSum(where, to):
    prefixSumList = [0] * to
    sum = 0
    for elem in range(to):
        sum += where[elem]
        prefixSumList[elem] = sum
    return prefixSumList


n = int(input())
x = []
y = []
for i in range(n):
    xi, yi = map(int, input().split())
    x.append(xi)
    y.append(yi)

m = int(input())
tracks = []
for i in range(m):
    startFinish = list(map(int, input().split()))
    tracks.append(startFinish)

leftRight = [0] * n
minim1 = y[0]
for i in range(n):
    if y[i] > minim1:
        leftRight[i] = y[i] - minim1
    minim1 = y[i]

rightLeft = [0] * n
y.reverse()
minim2 = y[0]
for i in range(n):
    if y[i] > minim2:
        rightLeft[i] = y[i] - minim2
    minim2 = y[i]

leftRightPrefixSum = countPrefixSum(leftRight, len(leftRight))
rightLeftPrefixSum = countPrefixSum(rightLeft, len(rightLeft))
rightLeftPrefixSum.reverse()
for i in range(m):
    start, finish = tracks[i]
    if start <= finish:
        sum1 = leftRightPrefixSum[finish - 1]
        sum2 = leftRightPrefixSum[start - 1]
        print(sum1 - sum2)
    else:
        sum1 = rightLeftPrefixSum[start - 1]
        sum2 = rightLeftPrefixSum[finish - 1]
        print(sum2 - sum1)
