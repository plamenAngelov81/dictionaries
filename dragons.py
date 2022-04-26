n = int(input())

dragon_dict = {}

for i in range(1, n + 1):
    dragon_data = input().split()
    dragon_class = dragon_data[0]
    dragon_name = dragon_data[1]
    damage = dragon_data[2]
    hp = dragon_data[3]
    armor = dragon_data[4]
    if dragon_class not in dragon_dict:
        dragon_dict[dragon_class] = {}
        if dragon_name not in dragon_dict[dragon_class]:
            dragon_dict[dragon_class][dragon_name] = [damage, hp, armor]
    else:
        dragon_dict[dragon_class][dragon_name] = [damage, hp, armor]

for x in dragon_dict:
    current_damage = 0
    current_hp = 0
    current_armor = 0
    for z in dragon_dict[x]:
        current_damage += int(dragon_dict[x][z][0])
        current_hp += int(dragon_dict[x][z][1])
        current_armor += int(dragon_dict[x][z][2])
    average_damage = current_damage / len(dragon_dict[x])
    average_hp = current_hp / len(dragon_dict[x])
    average_armor = current_armor / len(dragon_dict[x])
    print(f"{x}::({average_damage:.2f}/{average_hp:.2f}/{average_armor:.2f})")
    for y in dragon_dict[x]:
        print(f"-{y} -> damage: {dragon_dict[x][y][0]}, health: {dragon_dict[x][y][1]}, armor: {dragon_dict[x][y][2]}")
