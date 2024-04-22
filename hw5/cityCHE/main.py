n, r = map(int, input().split())

distances = list(map(int, input().split()))

first = 0
second = 0
goodPoses = 0
for i in range(n):
    while second < n and distances[second] - distances[first] <= r:
        second += 1
    if second < n and distances[second] - distances[first] > r:
        goodPoses += n - second
        first += 1
print(goodPoses)