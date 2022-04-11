food_data = input().split(" ")
products = input().split(" ")

food_stat = {}

for i in range(0, len(food_data), 2):
    food = food_data[i]
    quantity = int(food_data[i + 1])

    food_stat[food] = quantity

for y in products:
    if y in food_stat:
        print(f"We have {food_stat[y]} of {y} left")
    else:
        print(f"Sorry, we don't have {y}")
