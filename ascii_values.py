letters = input().split(", ")
letters_dict = {}

for i in letters:
    letters_dict[i] = ord(i)

print(letters_dict)
