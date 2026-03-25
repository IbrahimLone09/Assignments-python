distance = int(input("Enter distance to travel: "))
unit = input("Choose unit for distance ('M' for miles ) and ('K' for kilometers): ").upper()


if unit == "M":
    distance = distance * 1.609
    print("Distance in km:" , distance)

elif unit == "K":
    print("Distance in km:" , distance)

else:
    print("Invalid output. Next time please select the correct option:")


fuel_efficiency = int(input("Enter the fuel efficiency (km per liter): "))
fuel_price = int(input("Enter the fuel price (per liter): "))

fuel_required = distance / fuel_efficiency
total_travel_cost = fuel_required * fuel_price

print(f"Fuel required is {fuel_required} liters")
print(f"Travel cost is {total_travel_cost} rs")

if 0 < distance < 60:
    category = "short trip"

elif 60 <= distance < 200:
    category = "medium trip"

else:
    category = "long trip"

print(f"Trip category is {category}!")

if total_travel_cost > 1500:
    print("Journey is expensive!")

else:
    print("Journey is affordable!")
