num = int(input())

parking_dict = {}

for i in range(1, num + 1):
    data = input().split(" ")
    command = data[0]
    name = data[1]
    if command == "register":
        name = data[1]
        plate_number = data[2]
        if name in parking_dict:
            print(f"ERROR: already registered with plate number {plate_number}")
        else:
            parking_dict[name] = plate_number
            print(f"{name} registered {plate_number} successfully")

    elif command == "unregister":
        if name not in parking_dict:
            print(f"ERROR: user {name} not found")
        else:
            parking_dict.pop(name)
            print(f"{name} unregistered successfully")

for i in parking_dict:
    print(f"{i} => {parking_dict[i]}")
