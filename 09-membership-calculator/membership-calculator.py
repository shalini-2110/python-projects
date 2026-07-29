import random

membership_id = "MB" + str(random.randint(1000, 9999))

plan = input("Enter plan (monthly/quarterly/yearly): ")
is_student = input("Are you a student? (yes/no): ")
join_month = int(input("Enter joining month (1-12): "))

if plan.lower() == "monthly":
    fee = 500
    duration = 1
elif plan.lower() == "quarterly":
    fee = 1300
    duration = 3
elif plan.lower() == "yearly":
    fee = 4800
    duration = 12
else:
    fee = 0
    duration = 0
    print("Invalid plan.")

if is_student.lower() == "yes":
    discount = fee * 10 / 100
    final_fee = fee - discount
else:
    discount = 0
    final_fee = fee

expiry_month = join_month + duration

print("\n===== MEMBERSHIP RECEIPT =====")
print("Membership ID:", membership_id)
print("Plan:", plan)
print("Base Fee:", fee)
print("Student Discount:", discount)
print("Final Fee:", final_fee)
print("Joining Month:", join_month)
print("Expiry Month:", expiry_month)