data = input().split(" -> ")

employee_dict = {}

while True:

    factory = data[0]

    if factory == "End":
        break

    employee_id = data[1]
    if factory not in employee_dict:
        employee_dict[factory] = [employee_id]
    else:
        if employee_id not in employee_dict[factory]:
            employee_dict[factory] += [employee_id]
    data = input().split(" -> ")

for j in employee_dict:
    print(f"{j}")
    for k in employee_dict[j]:
        print(f"-- {k}")
