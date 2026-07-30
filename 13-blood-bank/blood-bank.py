import random

stock = {"A+": 5, "A-": 2, "B+": 4, "B-": 1, "O+": 2, "O-": 0, "AB+": 3, "AB-": 1}

print("===== CURRENT BLOOD STOCK =====")
for group in stock:
    print(group, ":", stock[group], "units")

choice = input("\nDo you want to (donate/search)? ")

if choice.lower() == "donate":
    name = input("Enter donor name: ")
    blood_group = input("Enter blood group (e.g., A+, O-): ").upper()

    if blood_group in stock:
        stock[blood_group] += 1
        receipt_no = "DON" + str(random.randint(1000, 9999))

        print("\n===== DONATION RECEIPT =====")
        print("Receipt No:", receipt_no)
        print("Donor Name:", name)
        print("Blood Group:", blood_group)
        print("Updated Stock:", stock[blood_group], "units")

        if stock[blood_group] < 3:
            print("ALERT: Stock still low for", blood_group)
    else:
        print("Invalid blood group.")

elif choice.lower() == "search":
    blood_group = input("Enter blood group to search: ")

    if blood_group in stock:
        print("\nAvailable stock for", blood_group, ":", stock[blood_group], "units")
        if stock[blood_group] < 3:
            print("ALERT: Low stock for", blood_group)
    else:
        print("Invalid blood group.")

else:
    print("Invalid choice.")