n = int(input())
a = list(map(int, input().split()))
m = int(input())

acs = [float("inf")] * 1000
for i in range(m):
    bi, ci = map(int, input().split())
    acs[bi - 1] = min(acs[bi - 1], ci)

a_classes = [0] * 1000
for i in a:
    a_classes[i - 1] += 1

ans = 0
for i in range(len(a_classes)):
    minim = 1001
    for j in range(i, len(acs)):
        if acs[j] < minim:
            minim = acs[j]
    ans += a_classes[i] * minim
print(ans)
