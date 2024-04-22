with open("input.txt", "r") as f:
    text = f.read().split()
    word_cnt = {}
    maxim = 0
    max_word = ""
    for word in text:
        if word not in word_cnt:
            word_cnt[word] = 1
        else:
            word_cnt[word] += 1
        if word_cnt[word] > maxim:
            maxim = word_cnt[word]
            max_word = word
        elif word_cnt[word] == maxim:
            max_word = min(max_word, word)

    print(max_word)
