n = int(input())
blocks = {}
for i in range(n):
    w, h = map(int, input().split())
    if w in blocks:
        if h > blocks[w]:
            blocks[w] = h
    else:
        blocks[w] = h

ans = 0
for height in blocks.values():
    ans += height

print(ans)
