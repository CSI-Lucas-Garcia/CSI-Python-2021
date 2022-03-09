import random 
word_list = ["Santo", "Loyola","Ignacio","Servicioso","Honesto","Iglesia","Jerusalen","Hombredearmas","respeto","Sacerdote","Jesuita"]

def get_word(word_list):
    word = random.choice(word_list)
    return word.upper()

def play(word):
    word_completion = "-" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6
    print("Vamos a jugar Hangman")
    print("Theme: Caracteristicas de San Ignacio de Loyola")
    print(display_hangman(tries))
    print(word_completion)
    print("\n")
    while not guessed and tries > 0:
        guess = input("Adivina la palabra: ").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("Ya trataste eso", guess, "!")
            elif guess not in word:
                print(guess, "No es la palabra :(")     
                tries -= 1
                guessed_letters.append(guess)
            else:
                print("Lo hiciste", guess, "esta en la palabra!")
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess 
                word_completion = "".join(word_as_list)
                if "-" not in word_completion:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guessed in guessed_words:
                print("Ya trataste eso", guess, "!")
            elif guess != word:
                print(guess, "No es la palabra : (")
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word
        else:
            print("Invalid input")
        print(display_hangman(tries))
        print(word_completion)
        print("\n")
    
    if guessed:
        print("Buen trabajo, pegaste la palabra!!! :)")
    else: 
        print("Lo siento, pero te quedaste sin tries. La palabra era " + word + " Para la proxima vez!")
                
    
def display_hangman(tries):
    stages = [ """
                    _________________________
                    |                       | 
                    |                       |
                    |                       O
                    |                      /|\\
                    |                       |
                    |                      / \\
                    -
                """,
                """
                    _________________________
                    |                       | 
                    |                       |
                    |                       O
                    |                      /|\\ 
                    |                       |
                    |                      / 
                    -
                """,
                """
                    _________________________
                    |                       | 
                    |                       |
                    |                       O
                    |                      /|\\ 
                    |                       |
                    |                      
                    -
                """,
                """
                    _________________________
                    |                       | 
                    |                       |
                    |                       O
                    |                      /|
                    |                       |
                    |                      
                    -
                """,
                """
                    _________________________
                    |                       | 
                    |                       |
                    |                       O
                    |                       |
                    |                       |
                    |                      
                    -
                """,
                """
                    _________________________
                    |                       | 
                    |                       |
                    |                       O
                    |
                    |
                    |                      
                    -
                """,
                """
                    _________________________
                    |                       | 
                    |                       |
                    |                      
                    |                    
                    |
                    |
                    -
                """

        ]
    return stages[tries]

def main():
    word = get_word(word_list)
    play(word)
    while input("De nuevo? (Y/N)").upper() == "Y":
        word = get_word(word_list)
        play(word)

if __name__ == "__main__":
    main() 