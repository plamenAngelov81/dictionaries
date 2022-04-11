store = {}
command = input()

while True:

    if command == "statistics":
        break

    current_tack = command.split(": ")
    food = current_tack[0]
    quantity = int(current_tack[1])
    if food in store.keys():
        store[food] += quantity
    else:
        store[food] = quantity

    command = input()

print("Products in stock:")

for (key, value) in store.items():
    print(f"- {key}: {value}")

all_keys = len(store.keys())
total_values = sum(store.values())

print(f"Total Products: {all_keys}")
print(f"Total Quantity: {total_values}")
