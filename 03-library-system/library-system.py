issued_books = []

student_name = input("Enter student name: ")
book_name = input("Enter book name: ")
days_taken = int(input("Enter number of days taken to return: "))

due_period = 7

if days_taken > due_period:
    fine = (days_taken - due_period) * 2
else:
    fine = 0

print("Student:", student_name)
print("Book:", book_name)
print("Days taken:", days_taken)
print("Fine:", fine)

issued_books.append(book_name)