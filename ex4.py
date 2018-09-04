#Variable with a value
cars = 100

#Variable with a value
space_in_a_car = 4.0
#Variable with a value
drivers = 30
#Variable with a value
passengers = 90
#Variable which performs mathematical operation on the given two varialbe values
cars_not_driven = cars - drivers
#Variable which performs mathematical operation on the given two varialbe values
cars_driven = drivers
#Variable which performs mathematical operation on the given two varialbe values
carpool_capacity = cars_driven * space_in_a_car
#Variable which performs mathematical operation on the given two varialbe values
average_passengers_per_car = passengers / cars_driven

#Displays String/Text Inside Quotation and the Variable Value
print("There are", cars, "cars available.")
#Displays String/Text Inside Quotation and the Variable Value
print("There are only", drivers, "drivers available.")
#Displays String/Text Inside Quotation and the Variable Value
print("There will be ", cars_not_driven, "empty cars today.")
#Displays String/Text Inside Quotation and the Variable Value
print("We can transport", carpool_capacity, "people today")
#Displays String/Text Inside Quotation and the Variable Value
print("We have", passengers, "to carpool today.")
#Displays String/Text Inside Quotation and the Variable Value
print("We need to put about", average_passengers_per_car, "in each car.")
