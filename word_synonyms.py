num = int(input())

synonyms = {}

for i in range(1, num + 1):
    word = input()
    word_value = input()
    if word not in synonyms:
        synonyms[word] = []

    synonyms[word].append(word_value)

for y in synonyms:
    strings = ", ".join(synonyms[y])
    print(f"{y} - {strings}")
