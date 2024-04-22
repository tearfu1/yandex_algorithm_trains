a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

if max(a, b) <= max(d, e) and min(a, b) <= min(d, e):
    print("YES")
elif max(a, c) <= max(d, e) and min(a, c) <= min(d, e):
    print("YES")
elif max(b, c) <= max(d, e) and min(b, c) <= min(d, e):
    print("YES")
else:
    print("NO")