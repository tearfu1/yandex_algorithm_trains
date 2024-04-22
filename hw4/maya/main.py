g, s = map(int, input().split())
word = input()
main_symcnt = {}
test_symcnt = {}
for i in range(65, 91):
    main_symcnt[chr(i)] = 0
    test_symcnt[chr(i)] = 0

for i in range(97, 123):
    main_symcnt[chr(i)] = 0
    test_symcnt[chr(i)] = 0


for sym in word:
    if sym not in main_symcnt:
        main_symcnt[sym] = 0
    main_symcnt[sym] += 1

seq = input()
for i in range(g):
    if seq[i] not in test_symcnt:
        test_symcnt[seq[i]] = 0
    test_symcnt[seq[i]] += 1

cnt = 0
if test_symcnt == main_symcnt:
    cnt += 1

for i in range(g, s):
    if seq[i] not in test_symcnt:
        test_symcnt[seq[i]] = 0
    test_symcnt[seq[i]] += 1
    test_symcnt[seq[i - g]] -= 1
    if main_symcnt == test_symcnt:
        cnt += 1
print(cnt)
