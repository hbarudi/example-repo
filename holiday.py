# Hashem Barudi
# ---
# Finally the task that introduces D E F in python at last.
# The task is to request from the user to type in
# the city they will travel to, how many nights at the hotel,
# and how many days to rent a car.
#
# first to collect the info from the user
# destination, number of nights, and number of days to rent a car.
# then define the functions to calculate the cost of the trip
# ---
# the mini database dictionary for destinations and prices:
travel_data = {
    "New York City, NY": {"airfare": 288, "hotel": 288},
    "Los Angeles, CA": {"airfare": 385, "hotel": 185},
    "Miami, FL": {"airfare": 317, "hotel": 125},
    "Chicago, IL": {"airfare": 344, "hotel": 172},
    "Las Vegas, NV": {"airfare": 275, "hotel": 137},
    "Boston, MA": {"airfare": 331, "hotel": 303},
    "San Francisco, CA": {"airfare": 424, "hotel": 132},
    "Orlando, FL": {"airfare": 269, "hotel": 154},
    "Seattle, WA": {"airfare": 378, "hotel": 172},
    "Denver, CO": {"airfare": 337, "hotel": 198}
}
# collect info from user:
print("This program calculates the cost to travel, stay in hotel, and rent a car.")
print("Destinations available: New York City, NY; Los Angeles, CA; Miami, FL;")
print("Chicago, IL; Las Vegas, NV; Boston, MA; San Francisco, CA;")
print("Orlando, FL; Seattle, WA; and Denver, CO.")
# best to place user inputs after setting up def
# city_flight = input("Type your destination (exit to exit): ")
# num_nights = input("Type number of hotel nights (exit to exit): ")
# rental_car_days = input("Type the number of days to rent a car (exit to exit): ")
# set up functions that calculate the total cost of trip:
def hotel_cost(city, nights):
    return travel_data[city]["hotel"] * nights
def plane_cost(city):
    return travel_data[city]["airfare"]
def car_rental(days):
    daily_rate = 65
    return daily_rate * days
def holiday_total_trip_cost(city, nights, car_days):
    return hotel_cost(city, nights) + plane_cost(city) + car_rental(car_days)
# collecting info from user and using it:
# ---
while True:
    city_flight = input("Type your destination (exit to exit): ")
    if city_flight.lower() == "exit":
        print("Closing application.")
        globals().clear()
        exit()
    elif city_flight not in travel_data:
        print("Sorry, destination not available, chose 1 of the following:")
        print("Destinations available: New York City, NY; Los Angeles, CA; Miami, FL;")
        print("Chicago, IL; Las Vegas, NV; Boston, MA; San Francisco, CA;")
        print("Orlando, FL; Seattle, WA; and Denver, CO.")
        continue
    else:
        break
#
while True:
    num_nights = input("Type number of hotel nights (exit to exit): ")
    if num_nights.lower() == "exit":
        print("Closing application.")
        globals().clear()
        exit()
    else:
        try:
            num_nights = int(num_nights)
            break
        except ValueError:
            print("Error: Type a valid number or exit to exit.")
            continue
#
while True:
    rental_car_days = input("Type the number of days to rent a car (exit to exit): ")
    if rental_car_days.lower() == "exit":
        print("Closing application.")
        globals().clear()
        exit()
    else:
        try:
            rental_car_days = int(rental_car_days)
            break
        except ValueError:
            print("Error: Type a valid number or exit to exit.")
            continue
# ---
# now the values are available, time to do the calculations:
total_trip_cost = holiday_total_trip_cost(city_flight, num_nights, rental_car_days)
print("")
print("Holiday Trip Details:")
print(f"Destination: {city_flight}")
print(f"Airfare: ${str(plane_cost(city_flight))}")
print(f"Hotel cost per night: ${travel_data[city_flight]["hotel"]}")
print(f"Number of nights hotel stay: {num_nights}")
print(f"The total hotel bill is: ${str(hotel_cost(city_flight, num_nights))}")
print("Rental car price is $65 per day.")
print(f"Number of days to rent a car: {rental_car_days}")
print(f"The total car rental bill is: ${str(car_rental(rental_car_days))}")
print(f"The total cost of the holiday trip is: ${total_trip_cost}")
globals().clear()
exit()