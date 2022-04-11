words_input = input().split(" ")

words = []                                               # words = list(map(lambda x: x.lower() words_input))
for word in words_input:
    words.append(word.lower())

words_counter = {}
for i in words:
    if i not in words_counter:
        words_counter[i] = 1
    else:
        words_counter[i] += 1

odd_words = []
for j in words_counter.keys():
    if words_counter[j] % 2 != 0:
        odd_words.append(j)

print(" ".join(odd_words))
