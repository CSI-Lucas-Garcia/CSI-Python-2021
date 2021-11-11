import math 
from ExperimentalData import ExperimentalData
from pathlib import Path
import json
import os

# gun = "M4A1"
# cartridge = "5.56X45mm"
# ammunition = "FMJ"
# velocity = 957

# Building = "Aquablue1"
# BuildingHeight = 85

# Gravity = 9.81
# converting variables 

def projectilefunction(experimentalData: ExperimentalData):
    
    planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
    g_ms2 = [3.7, 8.87, 9.81, 3.711, 24.79, 10.44, 8.69, 11.15]

    time_s = math.sqrt((2 * experimentalData.BuildingHeight) / experimentalData.Gravity) 
    #  Distance = (ExperimentalData[velocity] * time_s)
    Distance = (experimentalData.velocity * time_s)
    print(f"The gun selected was {experimentalData.gun}. The {experimentalData.gun} has a catridge of {experimentalData.catridge}. The {experimentalData.gun} is a {experimentalData.ammunition} weapon. The rate of fire of the {experimentalData.gun} is the {experimentalData.velocity}. The building selected is {experimentalData.Building}. It has a height of {experimentalData.BuildingHeight}m. The bullet is going to travel {Distance} meters. It will travel this distance in {time_s}s. The planet {planets} has a gravity of {g_ms2} \n")



# # Planet Index
# planet = planets.index(input("Planet Name: "))
# # Planet Gravity
# g_ms2[planet]

# Convert to JSON object
# experimentalData = {

# "gun": "M4A1",
# "cartridge": "5.56X45mm",
# "ammunition": "FMJ",
# "velocity": 957,
# "Building": "Aquablue1",
# "BuildingHeight": 85m,
# "Gravity": 9.81

# }
 




# experimentalData = ExperimentalData("M4A1", "5.56X45mm", "FMJ", 957, "Aquablue1", 85, 9.81)

myDataset = [
ExperimentalData("M4A1", "5.56X45mm", "FMJ", 957, "Aquablue1", 85, 9.81),
ExperimentalData("Mosin", "7.62X54mmR", "BCP FMJ", 840, "Aquablue1", 85, 9.81),
ExperimentalData("M4A1", "5.56X45mm", "HP", 947, "Aquablue1", 85, 9.81),
ExperimentalData("M4A1", "5.56X45mm", "FMJ", 957, "Caribean Sea View", 102, 9.81),
ExperimentalData("RSASS Nato", "7.62X51mm", "M61", 849, "Aquablue1", 85, 9.81),

ExperimentalData("M4A1", "5.56X45mm", "FMJ", 957, "Aquablue1", 85, 3.7),
ExperimentalData("Mosin", "7.62X54mmR", "BCP FMJ", 840, "Aquablue1", 85, 3.7),
ExperimentalData("M4A1", "5.56X45mm", "HP", 947, "Aquablue1", 85, 3.7),
ExperimentalData("M4A1", "5.56X45mm", "FMJ", 957, "Caribean Sea View", 102, 3.7),
ExperimentalData("RSASS Nato", "7.62X51mm", "M61", 849, "Aquablue1", 85, 3.7),

ExperimentalData("M4A1", "5.56X45mm", "FMJ", 957, "Aquablue1", 85, 8.87),
ExperimentalData("Mosin", "7.62X54mmR", "BCP FMJ", 840, "Aquablue1", 85, 8.87),
ExperimentalData("M4A1", "5.56X45mm", "HP", 947, "Aquablue1", 85, 8.87),
ExperimentalData("M4A1", "5.56X45mm", "FMJ", 957, "Caribean Sea View", 102, 8.87),
ExperimentalData("RSASS Nato", "7.62X51mm", "M61", 849, "Aquablue1", 85, 8.87),

ExperimentalData("M4A1", "5.56X45mm", "FMJ", 957, "Aquablue1", 85, 3.711),
ExperimentalData("Mosin", "7.62X54mmR", "BCP FMJ", 840, "Aquablue1", 85, 3.711),
ExperimentalData("M4A1", "5.56X45mm", "HP", 947, "Aquablue1", 85, 3.711),
ExperimentalData("M4A1", "5.56X45mm", "FMJ", 957, "Caribean Sea View", 102, 3.711),
ExperimentalData("RSASS Nato", "7.62X51mm", "M61", 849, "Aquablue1", 85, 3.711),

ExperimentalData("M4A1", "5.56X45mm", "FMJ", 957, "Aquablue1", 85, 24.79),
ExperimentalData("Mosin", "7.62X54mmR", "BCP FMJ", 840, "Aquablue1", 85, 24.79),
ExperimentalData("M4A1", "5.56X45mm", "HP", 947, "Aquablue1", 85, 24.79),
ExperimentalData("M4A1", "5.56X45mm", "FMJ", 957, "Caribean Sea View", 102, 24.79),
ExperimentalData("RSASS Nato", "7.62X51mm", "M61", 849, "Aquablue1", 85, 24.79),

ExperimentalData("M4A1", "5.56X45mm", "FMJ", 957, "Aquablue1", 85, 10.44),
ExperimentalData("Mosin", "7.62X54mmR", "BCP FMJ", 840, "Aquablue1", 85, 10.44),
ExperimentalData("M4A1", "5.56X45mm", "HP", 947, "Aquablue1", 85, 10.44),
ExperimentalData("M4A1", "5.56X45mm", "FMJ", 957, "Caribean Sea View", 102, 10.44),
ExperimentalData("RSASS Nato", "7.62X51mm", "M61", 849, "Aquablue1", 85, 10.44),

ExperimentalData("M4A1", "5.56X45mm", "FMJ", 957, "Aquablue1", 85, 8.69),
ExperimentalData("Mosin", "7.62X54mmR", "BCP FMJ", 840, "Aquablue1", 85, 8.69),
ExperimentalData("M4A1", "5.56X45mm", "HP", 947, "Aquablue1", 85, 8.69),
ExperimentalData("M4A1", "5.56X45mm", "FMJ", 957, "Caribean Sea View", 102, 8.69),
ExperimentalData("RSASS Nato", "7.62X51mm", "M61", 849, "Aquablue1", 85, 8.69),

ExperimentalData("M4A1", "5.56X45mm", "FMJ", 957, "Aquablue1", 85, 11.15),
ExperimentalData("Mosin", "7.62X54mmR", "BCP FMJ", 840, "Aquablue1", 85, 11.15),
ExperimentalData("M4A1", "5.56X45mm", "HP", 947, "Aquablue1", 85, 11.15),
ExperimentalData("M4A1", "5.56X45mm", "FMJ", 957, "Caribean Sea View", 102, 11.15),
ExperimentalData("RSASS Nato", "7.62X51mm", "M61", 849, "Aquablue1", 85, 11.15),

]

for data in myDataset:
    print("\n--------------------------------------------------\n")
    projectilefunction(data)

# Serialitation
myOutputPath = Path(__file__).parents[0]
myOutputFilePath = os.path.join(myOutputPath, "Project-Motion.json")

with open(myOutputFilePath, "w") as outfile:
    json.dump([data.__dict__ for data in myDataset], outfile)
    # json.dump(myDataset[0]. __dict__, outfile)


# print(myDataset[1].gun)
# projectilefunction(experimentalData)
