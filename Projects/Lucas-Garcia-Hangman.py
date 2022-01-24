import random 
word_list = ["Santo", "Hombre","Ignacio","Servicioso","Honesto","Iglesia","Jerusalen","Hombre de armas","respeto","Sacerdote","Jesuita"]


def get_word(word_list):
    word = random.choice(word_list)
    return word.upper()

def play(word):
    word_completion = "_" * len(word)
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
        guess = input("Adivina una palabra o letra: ").upper()
        if len(guess) == 1 and guess.isalpha():
            print("You already tried", guess, "!")
        elif guess not in word:
            print(guess, "Isn't in the word :(")     
            tries -=1
            guessed_letters.append(guess)
        else:
            print("You did it", guess, "is in the word!")
            guessed_letters.append(guess)







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
                                    -
                                    """,
                                    """

              _________________________
              |                       | 
              |                       |
              |                      
              |                    
              |
               
                                    -
                                    """,
                            

    ]