import random

token = "PK" + str(random.randint(1000, 9999))

vehicle_type = input("Enter vehicle type (bike/car/bus): ")
hours = float(input("Enter number of hours parked: "))
entry_time = input("Enter entry time (e.g., 10:00 AM): ")

if vehicle_type.lower() == "bike":
    rate = 10
elif vehicle_type.lower() == "car":
    rate = 20
elif vehicle_type.lower() == "bus":
    rate = 50
else:
    rate = 0
    print("Invalid vehicle type.")

fee = rate * hours

print("\n===== PARKING RECEIPT =====")
print("Token:", token)
print("Vehicle Type:", vehicle_type)
print("Entry Time:", entry_time)
print("Hours Parked:", hours)
print("Rate per hour:", rate)
print("Total Fee:", fee)