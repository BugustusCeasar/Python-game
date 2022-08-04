import random

def guessing_game():
    while True:
        num = random.randint(1,101)
        num_guesses = 0
        guess = int(input ("Guess a number between 1 to 100"))
        if (guess > num):
            print ("The number you guessed was too high")
        num_guesses = num_guesses + 1
        if (guess < num):
            print ("The number you guess was too low")
        else: (guess == num)
        print ("Congrats you guessed the right number! You had", num_guesses, "guesses")


        
    
    



    
    


