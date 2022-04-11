ore = input()

ore_dict = {}

while True:

    if ore == "stop":
        break

    quantity = int(input())

    if ore not in ore_dict:
        ore_dict[ore] = quantity
    else:
        ore_dict[ore] += quantity

    ore = input()

for i in ore_dict.keys():
    print(f"{i} -> {ore_dict[i]}")
