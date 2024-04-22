n = int(input())
xs = set()
for i in range(n):
    x, y = map(int, input().split())
    xs.add(x)

print(len(xs))
