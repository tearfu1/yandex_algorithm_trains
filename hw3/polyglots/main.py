n = int(input())
common = set()
all = set()

m_first = int(input())
prev = set()

for i in range(m_first):
    prev.add(input())
all = all.union(prev)
common = common.union(prev)

for i in range(n - 1):
    m = int(input())
    current = set()
    for j in range(m):
        current.add(input())
    common = common.intersection(current)
    prev = current
    all = all.union(prev)

print(len(common))
print(*common, sep="\n")

print(len(all))
print(*all, sep="\n")
