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