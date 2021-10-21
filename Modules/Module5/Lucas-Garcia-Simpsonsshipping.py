

print("Welcome to Simpsons' Shipping")
weight:float = float(input("What is the weight of your package:"))


# Ground shipping
if (weight == 2 and weight < 2):
    cost_ground = weight * 1.75 + 20
    print("Ground Shipping: $", float(cost_ground))
elif (weight == 3 and weight <=  6):
    cost_ground = weight * 3.50 + 20 
    print("Ground Shipping: $", float(cost_ground))
elif (weight == 7 and weight <= 10):
    cost_ground = weight * 4.50 + 20
    print("Ground Shipping: $", float(cost_ground))
else:
    cost_ground = weight * 5.25 + 20
    print("Ground Shipping: $", float(cost_ground))

    


if (weight == 2 and weight < 2):
    cost_ground = weight * 3.50 + 5
    print("Courier Shipping: $", float(cost_ground))
elif (weight == 3 and weight <=  6):
    cost_ground = weight * 7 + 8 
    print("Courier Shipping: $", float(cost_ground))
elif (weight == 7 and weight <= 10):
    cost_ground == weight * 9 + 12
    print("Courier Shipping: $", float(cost_ground))
else:
    cost_ground == weight * 10.50 + 15
    print("Courier Shipping: $", float(cost_ground))

if (weight == 2 and weight < 2):
    cost_ground = weight * 5.25 + 0
    print("Drone Shipping: $", float(cost_ground))
elif (weight == 3 and weight <=  6):
    cost_ground = weight * 10.50 + 0 
    print("Drone Shipping: $", float(cost_ground))
elif (weight == 7 and weight <= 10):
    cost_ground == weight * 13.50 + 0
    print("Drone Shipping: $", float(cost_ground))
else: 
    cost_ground = weight * 15.75 + 0
    print("Drone Shipping: $", float(cost_ground))


