# bus details
bus_route = "HYDERABAD TO VIZAG"
bus_seats = 20
bus_fare = 100.00

#function to display bus details
def display_bus_details():
    print("Bus Route:", bus_route)
    print("Number of Available Seats:", bus_seats)
    print("Fare per Seat:", bus_fare)

# function to book a seat on the bus
def book_seat():

    global bus_seats
    if bus_seats > 0:
        print("Please enter your name:")
        name = input()
        print("Please enter your age:")
        age = int(input())
        print("Please enter your gender (M/F/O):")
        gender = input()
        print("Please enter your contact number:")
        contact = int(input())
        print("Booking confirmed for seat number", bus_seats)
        return True
    else:
        print("Sorry, all seats are booked.")
        return False

#function to calculate total fare for a given number of seats
def calculate_fare(num_seats):
    if num_seats>20:
	       print('invalid seats')
    return num_seats * bus_fare

#booking ticket
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
        book_seat()
    elif choice == 3:
        print("Please enter the number of seats:")
        num_seats = int(input())
        print("Total Fare:", calculate_fare(num_seats))
    elif choice == 4:
        print("Thank you for using the Bus Ticket Booking System")
        break
    else:
        print("Invalid choice, please try again.")
