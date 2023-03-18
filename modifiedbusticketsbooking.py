import csv

BUS_ROUTE = "HYDERABAD TO VIZAG"
BUS_SEATS = 20
BUS_FARE = 100.00

def display_bus_details():
    print("Bus Route:", BUS_ROUTE)
    print("Number of Available Seats:", BUS_SEATS)
    print("Fare per Seat:", BUS_FARE)

def book_seat(name, age, gender, contact):
    global BUS_SEATS
    if BUS_SEATS > 0:
        seat_number = BUS_SEATS
        print("Booking confirmed for seat number", seat_number)

        with open('bookings.csv', mode='a', newline='') as csv_file:
            fieldnames = ['Name', 'Age', 'Gender', 'Contact', 'Seat Number']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writerow({
                'Name': name,
                'Age': age,
                'Gender': gender,
                'Contact': contact,
                'Seat Number': seat_number
            })

        BUS_SEATS -= 1
        return True
    else:
        print("Sorry, all seats are booked.")
        return False

def calculate_fare(num_seats):
    if num_seats > BUS_SEATS:
        print('Invalid number of seats')
    else:
        return num_seats * BUS_FARE

while True:
    print("Welcome to the Bus Ticket Booking System")
    print("----------------------------------------")
    print("1. Display Bus Details")
    print("2. Book a Seat")
    print("3. Calculate Fare")
    print("4. Exit")
    choice = int(input("Please enter your choice (1-4): "))
    if choice == 1:
        display_bus_details()
    elif choice == 2:
        print("Please enter your details:")
        name = "Ashok"
        age = "22"
        gender = "Male"
        contact = "7396560090"
        book_seat(name, age, gender, contact)
    elif choice == 3:
        print("Please enter the number of seats:")
        num_seats = int(input())
        total_fare = calculate_fare(num_seats)
        if total_fare:
            print("Total Fare:", total_fare)
    elif choice == 4:
        print("Thank you for using the Bus Ticket Booking System")
        break
    else:
        print("Invalid choice, please try again.")
