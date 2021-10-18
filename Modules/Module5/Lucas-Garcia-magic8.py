print("Lets play magic 8 ball") 
import random

input("Ask it a question: ")
random_number = random.randint(1, 12)



if random_number == 1: 
    print("Yes")

elif random_number == 2: 

    print("It is decidedly so.")

elif random_number == 3: 
    print("Without a doubt")

elif random_number == 4: 
    print("Reply hazy, try again.")

elif random_number == 5: 
    print("Ask again later")

elif random_number == 6:
    print("Better not tell you now.")

elif random_number == 7: 
    print("My sources say NO.")

elif random_number == 8: 
    print("Outlook not so good.")

elif random_number == 9:
    print("Very doubtful.")

elif random_number == 10: 
    print("There is a chance")

elif random_number == 11: 
    print("No")

elif random_number == 12: 
    print("High probability")

else:
    print("error")
