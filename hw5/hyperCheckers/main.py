n, k = map(int, input().split())
allCards = list(map(int, input().split()))
cntNums = {}
for card in allCards:
    if card not in cntNums:
        cntNums[card] = 0
    cntNums[card] += 1
uniqnums = list(cntNums.keys())
uniqnums.sort()
right = 0
duplicates = 0
ans = 0
for i in range(len(uniqnums)):
    while right < len(uniqnums) and uniqnums[i] * k >= uniqnums[right]:
        if cntNums[uniqnums[right]] >= 2:
            duplicates += 1
        right += 1
    dist = right - i
    if cntNums[uniqnums[i]] >= 2:
        ans += (dist - 1) * 3
        duplicates -= 1
    if cntNums[uniqnums[i]] >= 3:
        ans += 1
    ans += (dist - 1) * (dist - 2) * 3
    ans += duplicates * 3
print(ans)
