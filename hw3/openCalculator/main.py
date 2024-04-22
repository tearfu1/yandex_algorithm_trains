buttons = set(map(int, input().split()))
n = int(input())
digits = set()

while n > 0:
    digits.add(n % 10)
    n //= 10

print(len(digits) - len(digits.intersection(buttons)))
