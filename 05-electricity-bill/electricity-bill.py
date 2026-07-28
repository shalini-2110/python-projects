units = float(input("Enter units consumed: "))

if units <= 100:
    energy_charge = units * 3
elif units <= 200:
    energy_charge = (100 * 3) + ((units - 100) * 5)
else:
    energy_charge = (100 * 3) + (100 * 5) + ((units - 200) * 7)

meter_charge = 50
subtotal = energy_charge + meter_charge

gst = subtotal * 18 / 100
total_with_gst = subtotal + gst

late = input("Is the payment late? (yes/no): ")
if late.lower() == "yes":
    late_fee = 100
    total_with_gst = total_with_gst + late_fee
else:
    late_fee = 0

print("\n===== ELECTRICITY BILL =====")
print("Units Consumed:", units)
print("Energy Charge:", energy_charge)
print("Meter Charge:", meter_charge)
print("GST (18%):", gst)
print("Late Fee:", late_fee)
print("Final Bill Amount:", total_with_gst)