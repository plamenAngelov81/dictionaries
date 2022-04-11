people = input()

phone_book = {}
condition = False

while True:
    people_data = people.split("-")

    if people_data[0].isdigit():
        for person in range(1, int(people_data[0]) + 1):
            name = input()

            if name not in phone_book:
                print(f"Contact {name} does not exist.")
            else:

                print(f"{name} -> {phone_book[name]}")
        condition = True

    else:
        if people_data[0] not in phone_book:
            phone_book[people_data[0]] = people_data[1]

    if condition:
        break

    people = input()

