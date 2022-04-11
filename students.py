student_data = input()
courses = {}
while True:
    if ":" not in student_data:
        break
    info = student_data.split(":")
    name = info[0]
    student_number = info[1]
    course = info[2]

    if course not in courses.keys():
        courses[course] = dict()

    courses[course][student_number] = name

    student_data = input()

student_data = student_data.replace("_", " ")

for student_number in courses[student_data]:
    print(f"{courses[student_data][student_number]} - {student_number}")
