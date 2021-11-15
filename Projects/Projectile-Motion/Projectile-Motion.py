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

def projectilefunction(experimentalData: ExperimentalData):
    planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
    g_ms2 = [3.7, 8.87, 9.81, 3.711, 24.79, 10.44, 8.69, 11.15]

    planet = planets.index(experimentalData.planet)
    time_s = math.sqrt((2 * experimentalData.BuildingHeight) / g_ms2[planet]) 
    #  Distance = (ExperimentalData[velocity] * time_s)
    Distance = (experimentalData.velocity * time_s)
    
  # Parallel Lists
    
# Planet Index
    

# Planet Gravity
   

    print(f"The gun selected was {experimentalData.gun}. The {experimentalData.gun} has a catridge of {experimentalData.catridge}. The {experimentalData.gun} is a {experimentalData.ammunition} weapon. The rate of fire of the {experimentalData.gun} is the {experimentalData.velocity}. The building selected is {experimentalData.Building}. It has a height of {experimentalData.BuildingHeight}m. The bullet is going to travel {Distance} meters. It will travel this distance in {time_s}s. \n")
    print(f"The experiment is carried out in {experimentalData.planet} with a gravity of {g_ms2[planet]}")


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
ExperimentalData("M4A1", "5.56X45mm", "FMJ", 957, "Aquablue1", 85,"Mercury"),
ExperimentalData("Mosin", "7.62X54mmR", "BCP FMJ", 840, "Aquablue1", 85, "Venus"),
ExperimentalData("M4A1", "5.56X45mm", "HP", 947, "Aquablue1", 85, "Earth"),
ExperimentalData("M4A1", "5.56X45mm", "FMJ", 957, "Caribean Sea View", 102, "Mars"),
ExperimentalData("RSASS Nato", "7.62X51mm", "M61", 849, "Aquablue1", 85, "Jupiter")
]

for data in myDataset:
    print("\n--------------------------------------------------\n")
    projectilefunction(data)    

# Serialitation
myOutputPath = Path(__file__).parents[0]
myOutputFilePath = os.path.join(myOutputPath, "Project-Motion.json")

print(myOutputFilePath)

with open(myOutputFilePath, "w") as outfile:
    json.dump([data.__dict__ for data in myDataset], outfile)
    # json.dump(myDataset[0]. __dict__, outfile)

deserialize = open(myOutputFilePath)
experimentJson = json.load(deserialize)

for e in experimentJson:
    print("\n------------------------------\n")
    projectilefunction(ExperimentalData(**e))

# print(myDataset[1].gun)
# projectilefunction(experimentalData)
