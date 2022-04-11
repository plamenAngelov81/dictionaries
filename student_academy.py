num = int(input())

academy = {}

for i in range(1, num + 1):
    name = input()
    grade = float(input())

    if name not in academy:
        academy[name] = [grade]
    else:
        academy[name] += [grade]

for i in academy:

    average = sum(academy[i]) / len(academy[i])
    if average >= 4.50:
        print(f"{i} -> {average:.2f}")
