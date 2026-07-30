import random

invoice_no = "INV" + str(random.randint(1000, 9999))

package = input("Enter service package (Basic/Standard/Premium): ")

if package.lower() == "basic":
    service_charge = 1500
elif package.lower() == "standard":
    service_charge = 3000
elif package.lower() == "premium":
    service_charge = 5000
else:
    service_charge = 0
    print("Invalid package.")

spare_parts_cost = float(input("Enter spare parts cost (0 if none): "))

subtotal = service_charge + spare_parts_cost
gst = subtotal * 18 / 100
final_amount = subtotal + gst

start_day = int(input("Enter service start day (e.g., 10): "))
delivery_day = start_day + 3

print("\n===== SERVICE INVOICE =====")
print("Invoice No:", invoice_no)
print("Package:", package)
print("Service Charge:", service_charge)
print("Spare Parts Cost:", spare_parts_cost)
print("Subtotal:", subtotal)
print("GST (18%):", gst)
print("Final Amount:", final_amount)
print("Estimated Delivery Day:", delivery_day)