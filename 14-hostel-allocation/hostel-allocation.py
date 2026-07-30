rooms = []
for i in range(1, 6):
    room = {"room_no": i, "occupants": [], "capacity": 2}
    rooms.append(room)

hostel_fee = 8000

num_students = int(input("How many students to allocate? "))

for s in range(num_students):
    print("\n===== ROOM OCCUPANCY =====")
    for room in rooms:
        print("Room", room["room_no"], ":", len(room["occupants"]), "/", room["capacity"], "-", room["occupants"])

    name = input("\nEnter student name: ")

    allocated_room = None
    for room in rooms:
        if len(room["occupants"]) < room["capacity"]:
            allocated_room = room
            break

    if allocated_room is None:
        print("No rooms available. Cannot allocate", name)
    else:
        allocated_room["occupants"].append(name)
        print("\n===== HOSTEL RECEIPT =====")
        print("Student:", name)
        print("Room No:", allocated_room["room_no"])
        print("Hostel Fee:", hostel_fee)