planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
g_ms2 = [2.65, 1.11, 1, 2.64, 0.40, 0.94, 1.13, 0.88]

print("Calculate your jump lenght in a different plantet")

myJump = float(input("What is your jump lenght (meters) "))
planet = input(f"Chose your plantet from the list: {planets}")

def calculateweight(planet, lenght):
    print(f"/m Earth jump lenght in meters is: {lenght}")   

    planet_index = planets.index(planet)
    print(f"Jump lenght in {planets[planet_index]} is {myJump * g_ms2[planet_index]} meters")


calculateweight(planet, myJump) 