n = int(input())
positions = set()

for i in range(n):
    before, after = map(int, input().split())
    if before + after == n - 1 and after >= 0 and before >= 0:
        positions.add((before, after))

print(len(positions))
