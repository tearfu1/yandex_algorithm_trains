k = int(input())
operations = input()
prevlens = 0
ans = 0
for i in range(k, len(operations)):
    if operations[i] == operations[i - k]:
        prevlens += 1
        ans += prevlens
    else:
        prevlens = 0
print(ans)
