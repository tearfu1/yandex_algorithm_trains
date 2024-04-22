n = int(input())
syn_dict1 = {}
syn_dict2 = {}
for i in range(n):
    word1, word2 = input().split()
    syn_dict1[word1] = word2
    syn_dict2[word2] = word1

find_syn = input()
try:
    print(syn_dict1[find_syn])
except KeyError:
    print(syn_dict2[find_syn])
