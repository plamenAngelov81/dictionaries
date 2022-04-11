material_data = input().split(" ")


legend_data = {"shards": 0, "fragments": 0, "motes": 0}
junk_data = {}

stop_condition = False

while True:

    materials = []

    for material in material_data:
        materials.append(material.lower())

    for i in range(0, len(materials), 2):
        special_item = ""
        item = materials[i + 1]
        quantity = int(materials[i])
        if item in ["shards", "fragments", "motes"]:
            if item not in legend_data:
                legend_data[item] = quantity
            else:
                legend_data[item] += quantity

            if legend_data[item] >= 250:
                legend_data[item] -= 250

                if item == "shards":
                    special_item = "Shadowmourne"
                elif item == "fragments":
                    special_item = "Valanyr"
                elif item == "motes":
                    special_item = "Dragonwrath"

                stop_condition = True
        else:
            if item not in junk_data:
                junk_data[item] = quantity
            else:
                junk_data[item] += quantity

        if stop_condition:
            print(f"{special_item} obtained!")
            break

    if stop_condition:
        break

    material_data = input().split(" ")

for i in legend_data:
    print(f"{i}: {legend_data[i]}")

for y in junk_data:
    print(f"{y}: {junk_data[y]}")
