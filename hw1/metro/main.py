a = int(input())
b = int(input())
n = int(input())
m = int(input())

tmin_a = 1 + (n - 1) * (a + 1)
tmin_b = 1 + (m - 1) * (b + 1)
tmax_a = a + n * (a + 1)
tmax_b = b + m * (b + 1)

if not (tmin_a > tmax_b or tmin_b > tmax_a):
    ans_max = min(tmax_a, tmax_b)
    ans_min = max(tmin_b, tmin_a)
    print(ans_min, ans_max)
else:
    print(-1)

