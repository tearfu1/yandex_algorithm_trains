n, k = map(int, input().split())
text = input()
syms = {}
r = 0
maxim = 1
start = 1
maxval = 0
for i in range(n):
    while r < n and maxval <= k:
        if text[r] not in syms:
            syms[text[r]] = 0
        syms[text[r]] += 1
        maxval = max(maxval, syms[text[r]])
        r += 1
    if maxval > k:
        syms[text[r - 1]] -= 1
        substrlen = sum(syms.values())
        if substrlen > maxim:
            maxim = substrlen
            start = i + 1
        syms[text[r - 1]] += 1
    else:
        substrlen = sum(syms.values())
        if substrlen > maxim:
            maxim = substrlen
            start = i + 1
    syms[text[i]] -= 1
    if syms[text[i]] == 0:
        del syms[text[i]]
    if len(syms.values()) != 0:
        maxval = max(syms.values())
print(maxim, start)
