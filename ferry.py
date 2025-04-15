ticket_id_counter = 20000

class BookingSystem:
    def __init__(self, passenger_id, passenger_name, date, form_of_id):
        global ticket_id_counter
        self.ticket_id = ticket_id_counter
        self.form_of_id = form_of_id
        self.date = date
        self.passenger_id = passenger_id
        self.passenger_name = passenger_name
        self.total_cost = 0
        self.status = "Pending"
        self.approval_reference = " "

        ticket_id_counter += 1

    def customer_info(self):
        self.form_of_id = input("Enter form of ID (Passport, Driver's License): ")
        self.id_number = input("Enter ID number: ")
        self.passenger_name = input("Enter passenger name: ")
        print(f"Ticket ID: {self.ticket_id} generated for {self.passenger_name}")

    def ferry_service_details(self):
        items = []
        total_cost = 0
        while True:
            service_item_name = input("Enter service item name (type 'done' to complete): ")
            if service_item_name.lower() == 'done':
                break
            try:
                item_price = float(input("Enter service item price: $"))
                items.append({service_item_name: item_price})
                total_cost += item_price
            except ValueError:
                print("Invalid price. Please try again.")
        self.total_cost = total_cost
        print(f"\nTotal Cost: ${total_cost:.2f}")

    def booking_approval(self):
        if self.total_cost < 300:
            self.status = "Approved"
        else:
            self.status = "Not Approved"
        print(f"Status: {self.status}")

        if self.status == "Approved":
            self.approval_reference = self.id_number[:3] + "20001"[-2:]
            print(f"Approval Ref: {self.approval_reference}")

    def display_booking_info(self):
        print(f"\n--- Booking Info ---")
        print(f"Form of ID: {self.form_of_id}")
        print(f"ID Number: {self.id_number}")
        print(f"Passenger Name: {self.passenger_name}")
        print(f"Date of Travel: {self.date}")
        print(f"Ticket ID: {self.ticket_id}")
        print(f"Total: ${self.total_cost:.2f}")
        print(f"Status: {self.status}")
        print(f"Approval Reference Number: {self.approval_reference}")

    @staticmethod
    def booking_statistic(bookings):
        total_bookings = len(bookings)
        approved = 0
        pending = 0
        not_approved = 0

        for booking in bookings:
            if booking.status == "Approved":
                approved += 1
            elif booking.status == "Pending":
                pending += 1
            else:
                not_approved += 1

        print("\n--- Booking Statistics ---")
        print(f"Total bookings submitted: {total_bookings}")
        print(f"Total approved bookings: {approved}")
        print(f"Total pending bookings: {pending}")
        print(f"Total not approved bookings: {not_approved}")

bookings = []

for i in range(5):
    print(f"\n=== Booking {i + 1} ===")
    passenger_id = input("Enter passenger ID: ")
    passenger_name = input("Enter passenger name: ")
    date = input("Enter date of travel (e.g. 2025-04-11): ")
    form_of_id = input("Enter form of ID (Passport, Driver's License): ")

    booking = BookingSystem(passenger_id, passenger_name, date, form_of_id)

    booking.customer_info()
    booking.ferry_service_details()

    bookings.append(booking)

print("\nInitial Booking Statistics:")
BookingSystem.booking_statistic(bookings)

for booking in bookings:
    booking.booking_approval()

print("\n=== All Bookings After Approval ===")
for booking in bookings:
    booking.display_booking_info()

print("\nFinal Booking Statistics:")
BookingSystem.booking_statistic(bookings)