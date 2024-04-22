a = int(input())
b = int(input())
c = int(input())
summ = a * 2 + b * 3 + c * 4
cnt = a + b + c
l = 0
r = cnt + 1
while l < r:
    m = (l + r) // 2
    if (summ + m * 5) / (cnt + m) < 3.5:
        l = m + 1
    else:
        r = m
if l == 1333333333333333:
        l += 1
print(l)
