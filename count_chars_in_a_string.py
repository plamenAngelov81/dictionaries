string = input()

letters = [x for x in string if x != " "]

letter_counter = {}

for letter in letters:
    if letter not in letter_counter:
        letter_counter[letter] = 1
    else:
        letter_counter[letter] += 1

for i in letter_counter:
    print(f"{i} -> {letter_counter[i]}")
