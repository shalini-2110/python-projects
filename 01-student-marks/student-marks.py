name = input("Enter student name: ")

marks = []
for i in range(6):
    m = int(input(f"Enter marks for subject {i+1}: "))
    marks.append(m)

print("Name:", name)
print("Marks:", marks)