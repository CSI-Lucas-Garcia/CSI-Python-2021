gun = "M4A1"
cartridge = "5.56X45mm"
ammunition = "Single fire"
velocity = 800

Building = "Aquablue1"
BuildingHeight = 85

Gravity = 9.81

import math 

time_s = math.sqrt((2 * BuildingHeight) / Gravity) 
Distance = (velocity * time_s)

print(f"The gun i selected was {gun}. The {gun} has a catridge of {cartridge}. The {gun} is a {ammunition} weapon. The rate of fire of the {gun} is {velocity}. The buildin i selected is {Building}. It has a building height of {BuildingHeight}.\n")