import random

all_complaints = []

num_complaints = int(input("How many complaints to register? "))

for i in range(num_complaints):
    print(f"\n--- Complaint {i+1} ---")
    description = input("Enter complaint description: ")
    priority = input("Enter priority (Low/Medium/High): ")

    complaint = {
        "id": "CMP" + str(random.randint(1000, 9999)),
        "description": description,
        "priority": priority,
        "status": "Pending",
        "resolution_date": "Not resolved"
    }

    all_complaints.append(complaint)
    print("Registered with ID:", complaint["id"])

print("\n===== ALL COMPLAINTS =====")
for c in all_complaints:
    print(c)

search_id = input("\nEnter Complaint ID to update status: ")

found = False
for complaint in all_complaints:
    if complaint["id"].lower() == search_id.lower():
        found = True
        new_status = input("Enter new status (Pending/In Progress/Resolved): ")
        complaint["status"] = new_status
        if new_status.lower() == "resolved":
            complaint["resolution_date"] = input("Enter resolution date: ")
        print("Updated complaint:", complaint)

if not found:
    print("Complaint ID not found.")

print("\n===== FINAL COMPLAINT LIST =====")
for c in all_complaints:
    print(c)