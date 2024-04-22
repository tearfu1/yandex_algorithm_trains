c1, c2 = map(int, input().split())
colors1 = set()
for i in range(c1):
    colors1.add(int(input()))
colors2 = set()
for i in range(c2):
    colors2.add(int(input()))

same_colors = colors1.intersection(colors2)
print(len(same_colors))
print(*sorted(same_colors, key=int))

print(len(colors1.difference(colors2)))
print(*sorted(colors1.difference(colors2), key=int))

print(len(colors2.difference(colors1)))
print(*sorted(colors2.difference(colors1), key=int))
