n = int(input())
keyboard = {}
pres_nums = list(map(int, input().split()))
for i in range(1, n + 1):
    keyboard[i] = pres_nums[i - 1]

seq_len = int(input())
seq = list(map(int, input().split()))
for key in seq:
    keyboard[key] -= 1
ans = ["YES" if keyboard[key] < 0 else "NO" for key in keyboard]
print(*ans, sep="\n")
