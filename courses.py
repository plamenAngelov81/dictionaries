data = input().split(" : ")

courses = {}

while True:
    module = data[0]
    if module == "end":
        break
    name = data[1]

    if module not in courses:
        courses[module] = [name]
    else:
        courses[module] += [name]

    data = input().split(" : ")

for i in courses.keys():
    print(f"{i}: {len(courses[i])}")
    for y in courses[i]:
        print(f"-- {y}")
