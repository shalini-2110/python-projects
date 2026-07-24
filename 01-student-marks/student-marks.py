name = input("Enter student name: ")

marks = []
for i in range(6):
    m = int(input(f"Enter marks for subject {i+1}: "))
    marks.append(m)

print("Name:", name)
print("Marks:", marks)
total = sum(marks)
highest = max(marks)
lowest = min(marks)
average = (total - lowest) / 5
print("Total:", total)
print("Highest:", highest)
print("Lowest:", lowest)
print("Average (ignoring lowest):", average)
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

print("Failed Subjects:", failed_count)
print("Result:", result)
print("Grade:", grade)
print("Rank:", rank)