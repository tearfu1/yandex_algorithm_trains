n, k, m = map(int, input().split())

details = 0
if not (m > k):
    while n // k > 0:
        number_blanks = n // k
        n %= k
        if number_blanks > 0:
            details += number_blanks * (k // m)
            n += number_blanks * (k % m)
print(details)
