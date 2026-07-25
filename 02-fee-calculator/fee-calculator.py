import random
receipt_no = "RC" + str(random.randint(1000, 9999))
tuition = 1400
lab = 7000
bus = 20000
hostel = 8000

total_fee = tuition + lab + bus + hostel

print("Total Fee before discount:", total_fee)
scholarship = input("Do you have a scholarship? (yes/no): ")

if scholarship.lower() == "yes":
    discount = total_fee * 15 / 100
    total_fee = total_fee - discount
    print("Scholarship Discount:", discount)

print("Total after scholarship:", total_fee)
late = input("Is the payment late? (yes/no): ")

if late.lower() == "yes":
    late_fee = 100
    total_fee = total_fee + late_fee
    print("Late Fee Applied:", late_fee)

print("Final Payable Amount:", total_fee)
print("\n===== FEE RECEIPT =====")
print("Receipt No:", receipt_no)
print("Tuition:", tuition)
print("Lab:", lab)
print("Bus:", bus)
print("Hostel:", hostel)
print("Final Payable Amount:", total_fee)