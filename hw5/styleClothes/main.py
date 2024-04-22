n = int(input())
colors1 = list(map(int, input().split()))
m = int(input())
colors2 = list(map(int, input().split()))
minDist = abs(colors1[0] - colors2[0])
sameVals = [colors1[0], colors2[0]]
first1 = first2 = 0

for i in range(len(colors1) + len(colors2)):
    if first1 != len(colors1) - 1 and first2 != len(colors2) - 1:
        if colors2[first2 + 1] < colors1[first1 + 1]:
            first2 += 1
        else:
            first1 += 1

    elif len(colors1) == 1 and first2 != len(colors2) - 1:
        first2 += 1

    elif len(colors2) == 1 and first1 != len(colors1) - 1:
        first1 += 1

    dist = abs(colors1[first1] - colors2[first2])
    if dist < minDist:
        minDist = dist
        sameVals = [colors1[first1], colors2[first2]]
    elif minDist == 0:
        break

if first1 != len(colors1) - 1 and abs(colors2[-1] - colors1[first1 + 1]) < minDist:
    sameVals[0], sameVals[1] = colors1[first1 + 1], colors2[-1]
elif first2 != len(colors2) - 1 and abs(colors1[-1] - colors2[first2 + 1]) < minDist:
    sameVals[0], sameVals[1] = colors1[-1], colors2[first2 + 1]
print(*sameVals)
