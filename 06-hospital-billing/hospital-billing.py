import random

patient_id = "PT" + str(random.randint(1000, 9999))

name = input("Enter patient name: ")
patient_type = input("Enter patient type (General/VIP): ")

if patient_type.lower() == "vip":
    consultation_fee = 1000
else:
    consultation_fee = 500

medicine_charges = float(input("Enter medicine charges: "))
lab_charges = float(input("Enter lab charges: "))

subtotal = consultation_fee + medicine_charges + lab_charges

insurance = input("Does the patient have insurance? (yes/no): ")
if insurance.lower() == "yes":
    discount = subtotal * 20 / 100
    final_amount = subtotal - discount
else:
    discount = 0
    final_amount = subtotal

print("\n===== HOSPITAL INVOICE =====")
print("Patient ID:", patient_id)
print("Name:", name)
print("Patient Type:", patient_type)
print("Consultation Fee:", consultation_fee)
print("Medicine Charges:", medicine_charges)
print("Lab Charges:", lab_charges)
print("Subtotal:", subtotal)
print("Insurance Discount:", discount)
print("Final Amount:", final_amount)