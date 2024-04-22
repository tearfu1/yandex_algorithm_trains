with open("input.txt","r") as f:
    sentences = f.read().splitlines()
    words = [sentence.split() for sentence in sentences]
    unique_words = set()
    for i in range(len(words)):
        for j in words[i]:
            unique_words.add(j)
    print(len(unique_words))