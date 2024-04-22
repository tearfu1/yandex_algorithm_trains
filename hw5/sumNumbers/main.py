n, k = map(int, input().split())
numbers = list(map(int, input().split()))
left = right = 0
summ = 0
cnt = 0
for i in range(n):
    while right < n and summ < k:
        summ += numbers[right]
        right += 1
    if summ == k:
        cnt += 1
    summ -= numbers[left]
    left += 1
print(cnt)
