first = input()
second = input()

number_of_pairs = dict()
pairs = set()
for i in range(len(first) - 1):
    pair = first[i:i + 2]
    if pair not in number_of_pairs:
        number_of_pairs[pair] = 1
    else:
        number_of_pairs[pair] += 1

for i in range(len(second) - 1):
    pair = second[i:i + 2]
    pairs.add(pair)

ans = 0
for pair in pairs:
    if pair in number_of_pairs:
        ans += number_of_pairs[pair]
print(ans)
