with open("input.txt", "r") as f:
    text = f.read().split()
    word_cnt = {}
    word_num_before = []
    for word in text:
        if word not in word_cnt:
            word_cnt[word] = 0
        else:
            word_cnt[word] += 1
        word_num_before.append(word_cnt[word])

    print(*word_num_before)
