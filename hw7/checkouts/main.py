n = int(input())
events = []
cnt = 0
for i in range(n):
    beginH, beginM, endH, endM = map(int, input().split())
    beginM += beginH * 60
    endM += endH * 60
    events.append([beginM, 1])
    events.append([endM, -1])
    if beginM >= endM:
        cnt += 1
events.sort()
ans = 0
start = 0
for event in events:
    cnt += event[1]
    if cnt == n:
        start = event[0]
    if cnt == n - 1 and event[1] == -1:
        ans += event[0] - start
if cnt == n:
    ans += 24 * 60 - start
print(ans)