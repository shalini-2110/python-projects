import random

seats = []
for i in range(1, 11):
    seat = {"seat_no": i, "booked": False, "passenger": None}
    seats.append(seat)

num_bookings = int(input("How many bookings do you want to make? "))

for b in range(num_bookings):
    print("\n===== SEAT AVAILABILITY =====")
    for seat in seats:
        status = "Booked" if seat["booked"] else "Available"
        print("Seat", seat["seat_no"], ":", status)

    name = input("\nEnter passenger name: ")
    seat_no = int(input("Enter seat number to book: "))
    distance = float(input("Enter distance (km): "))

    selected_seat = None
    for seat in seats:
        if seat["seat_no"] == seat_no:
            selected_seat = seat

    if selected_seat is None:
        print("Invalid seat number.")
    elif selected_seat["booked"]:
        print("Seat already booked. Please choose another seat.")
    else:
        fare = distance * 5
        ticket_no = "TKT" + str(random.randint(1000, 9999))

        selected_seat["booked"] = True
        selected_seat["passenger"] = name

        print("\n----- BOOKING CONFIRMED -----")
        print("Ticket No:", ticket_no)
        print("Passenger:", name)
        print("Seat No:", seat_no)
        print("Distance:", distance, "km")
        print("Fare:", fare)