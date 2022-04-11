command = input().split(" ")

product_dict = {}

while True:
    if command[0] == "buy":
        break

    item = command[0]
    price = float(command[1])
    current_quantity = int(command[2])

    if item not in product_dict:
        product_dict[item] = [price, current_quantity]
    else:
        product_dict[item] = [price, (product_dict[item][1] + current_quantity)]

    command = input().split(" ")

for i in product_dict:
    total = product_dict[i][0] * product_dict[i][1]
    print(f"{i} -> {total:.2f}")
