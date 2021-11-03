import math 
from ExperimentalData import ExperimentalData
# gun = "M4A1"
# cartridge = "5.56X45mm"
# ammunition = "FMJ"
# velocity = 957

# Building = "Aquablue1"
# BuildingHeight = 85

# Gravity = 9.81
# converting variables 

def projectilefunction(experimentalData: ExperimentalData):
    time_s = math.sqrt((2 * BuildingHeight) / Gravity) 

   #  Distance = (ExperimentalData[velocity] * time_s)
    Distance = (velocity * time_s)

    print(f"The gun i selected was {gun}. The {gun} has a catridge of {cartridge}. The {gun} is a {ammunition} weapon. The rate of fire of the {gun} is {velocity}. The buildin i selected is {Building}. It has a height of {BuildingHeight}.\n")

# Convert to JSON object
# experimentalData = {

# "gun": "M4A1",
# "cartridge": "5.56X45mm",
# "ammunition": "FMJ",
# "velocity": 957,
# "Building": "Aquablue1",
# "BuildingHeight": 85,
# "Gravity": 9.81

# }

experimentalData = ExperimentalData("M4A1", "5.56X45", "FMJ", 957, "Aquablue1", 85, 9.81)
projectilefunction(experimentalData)
