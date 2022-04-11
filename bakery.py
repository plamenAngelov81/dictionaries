food_data = input().split()

food_stat = {}

for i in range(0, len(food_data), 2):
    food = food_data[i]
    quantity = int(food_data[i + 1])

    food_stat[food] = quantity

print(food_stat)
