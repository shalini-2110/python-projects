all_students = []
num_students = int(input("Enter the number of students: "))
for s in range(num_students):
    print(f"\n----student {s+1}----")
    name = input("Enter student name: ")
    marks = []
    for i in range(6):
        m =  int(input(f"Enter marks for subject {i+1}: "))
        marks.append(m)
        total = sum(marks)
    highest = max(marks)
    lowest = min(marks)
    average = (total - lowest) / 5

    failed_count = 0
    for mark in marks:
        if mark < 35:
            failed_count += 1

    if failed_count == 0:
        result = "Pass"
    else:
        result = "Fail"

    if average >= 90:
        grade = "A"
    elif average >= 80:
        grade = "B"
    elif average >= 70:
        grade = "C"
    elif average >= 60:
        grade = "D"
    elif average >= 35:
        grade = "E"
    else:
        grade = "F"

    if average >= 75:
        rank = "Distinction"
    elif average >= 60:
        rank = "First Class"
    elif average >= 50:
        rank = "Second Class"
    elif average >= 35:
        rank = "Pass"
    else:
        rank = "Fail"

    student = {
        "name": name,
        "marks": marks,
        "total": total,
        "highest": highest,
        "lowest": lowest,
        "average": average,
        "failed_count": failed_count,
        "result": result,
        "grade": grade,
        "rank": rank
    }

    all_students.append(student)

print("\n===== FINAL REPORT =====")
for student in all_students:
    print(f"\nName: {student['name']}")
    print(f"Marks: {student['marks']}")
    print(f"Total: {student['total']}")
    print(f"Highest: {student['highest']}")
    print(f"Lowest: {student['lowest']}")
    print(f"Average: {student['average']}")
    print(f"Failed Subjects: {student['failed_count']}")
    print(f"Result: {student['result']}")
    print(f"Grade: {student['grade']}")
    print(f"Rank: {student['rank']}")
