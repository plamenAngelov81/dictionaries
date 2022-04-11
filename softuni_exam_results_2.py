data = input().split("-")

exam_stat = {}
number_of_exams = {}

while True:

    if data[0] == "exam finished":
        break

    if len(data) == 3:
        username = data[0]
        course = data[1]
        grade = int(data[2])

        if course not in number_of_exams:
            number_of_exams[course] = 0
        number_of_exams[course] += 1

        if course not in exam_stat:
            exam_stat[course] = {username: grade}
        else:
            if username in exam_stat[course].keys():
                if grade > exam_stat[course][username]:
                    exam_stat[course][username] = grade
            else:
                exam_stat[course][username] = grade

    if len(data) == 2:
        username = data[0]
        if data[1] == "banned":
            for key, value in exam_stat.items():
                if username in value:
                    del exam_stat[key][username]

    data = input().split("-")

print("Results:")
for key, value in exam_stat.items():
    for n in value:
        print(f"{n} | {value[n]}")

print("Submissions:")
for key, value in number_of_exams.items():
    print(f"{key} - {value}")
