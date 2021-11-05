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
    time_s = math.sqrt((2 * experimentalData.BuildingHeight) / experimentalData.Gravity) 

   #  Distance = (ExperimentalData[velocity] * time_s)
    Distance = (experimentalData.velocity * time_s)

    print(f"The gun selected was {experimentalData.gun}. The {experimentalData.gun} has a catridge of {experimentalData.catridge}. The {experimentalData.gun} is a {experimentalData.ammunition} weapon. The rate of fire of the {experimentalData.gun} is the {experimentalData.velocity}. The building selected is {experimentalData.Building}. It has a height of {experimentalData.BuildingHeight}m. The bullet is going to travel {Distance} meters. It will travel this distance in {time_s}s\n")

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

experimentalData = ExperimentalData("M4A1", "5.56X45mm", "FMJ", 957, "Aquablue1", 85, 9.81)

myDataset = [
ExperimentalData("M4A1", "5.56X45mm", "FMJ", 957, "Aquablue1", 85, 9.81),
ExperimentalData("Mosin", "7.62X54mmR", "BCP FMJ", 840, "Aquablue1", 85, 9.81),
ExperimentalData("M4A1", "5.56X45mm", "HP", 947, "Aquablue1", 85, 9.81),
ExperimentalData("M4A1", "5.56X45mm", "FMJ", 957, "Caribean Sea View", 102, 9.81),
ExperimentalData("RSASS Nato", "7.62X51mm", "M61", 849, "Aquablue1", 85, 9.81),



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
