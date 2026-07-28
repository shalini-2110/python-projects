issued_books = []
total_fine = 0

student_name = input("Enter student name: ")
num_books = int(input("How many books do you want to issue (max 3)? "))

if num_books > 3:
    print("You can only issue a maximum of 3 books.")
else:
    for i in range(num_books):
        book_name = input(f"\nEnter name of book {i+1}: ")

        if book_name in issued_books:
            print(f"'{book_name}' is already issued. Skipping duplicate.")
            continue

        days_taken = int(input(f"Enter number of days taken to return '{book_name}': "))

        due_period = 7
        if days_taken > due_period:
            fine = (days_taken - due_period) * 2
        else:
            fine = 0

        total_fine = total_fine + fine
        issued_books.append(book_name)

        print(f"Book: {book_name} | Days taken: {days_taken} | Fine: {fine}")

    print("\n===== SUMMARY =====")
    print("Student:", student_name)
    print("Books issued:", issued_books)
    print("Total Fine:", total_fine)