n = int(input())
events = []
for i in range(n):
    a, b = map(int, input().split())
    if b - a >= 5:
        events.append([a, -1, i])
        events.append([b - 5, 1, i])
events.sort()
if len(events) == 0:
    print("0 1 10")
elif len(events) == 2:
    print(f'1 {events[0][0]} {events[0][0] + 10}')
else:
    bestans = 0
    firstbest, secondbest = 0, 0
    firstad = set()
    for i in range(len(events)):
        event1 = events[i]
        if event1[1] == -1:
            firstad.add(event1[2])
            if len(firstad) > bestans:
                bestans = len(firstad)
                firstbest = event1[0]
                secondbest = event1[0] + 5
        secondadcnt = 0
        for j in range(i + 1, len(events)):
            event2 = events[j]
            if event2[1] == -1 and event2[2] not in firstad:
                secondadcnt += 1
            if event2[0] - 5 >= event1[0] and len(firstad) + secondadcnt > bestans:
                bestans = len(firstad) + secondadcnt
                firstbest = event1[0]
                secondbest = event2[0]
            if event2[1] == 1 and event2[2] not in firstad:
                secondadcnt -= 1
        if event1[1] == 1:
            firstad.remove(event1[2])
    print(f"{bestans} {firstbest} {secondbest}")