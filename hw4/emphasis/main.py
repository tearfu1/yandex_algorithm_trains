n = int(input())
stress_dict = {}
for i in range(n):
    word = input()
    if word.lower() not in stress_dict:
        stress_dict[word.lower()] = set()
    stress_dict[word.lower()].add(word)

task = input().split()
mistakes = 0
for word in task:
    def countCapitals(ex):
        cnt = 0
        for sym in ex:
            if 65 <= ord(sym) <= 90:
                cnt += 1
        return cnt

    if word.lower() not in stress_dict:
        emph = countCapitals(word)
        if emph != 1:
            mistakes += 1
    else:
        if word not in stress_dict[word.lower()]:
            mistakes += 1
print(mistakes)