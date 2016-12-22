# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console
import simplegui
import random

global guess
global secret_number
global number_of_guesses

# helper function to start and restart the game
def new_game():
    # initialize global variables used in your code here
    guess = 0
    secret_number = 0
    number_of_guesses = 7
    
# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    secret_number = random.randrange(1, 100)
    print secret_number
    # remove this when you add your code    
    return secret_number
    

def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    
    secret_number = random.randrange(1, 1000)
    print secret_number
    return secret_number
    
    
    
def input_guess(guess):
    new_game()
    # main game logic goes here	
    intguess = int(guess)
   
    print intguess
    # if wants 1, 100, choose -> secret_number
    
    # if wants 1, 1000, choose -> secret_number
    return intguess
    # remove this when you add your code
    

    
# create frame
frame = simplegui.create_frame("Guessing Game", 300, 300)

# register event handlers for control elements and start frame
frame.add_button("Range: 1 - 100", range100, 200)
frame.add_button("Range: 1 - 1000", range1000, 200)

frame.add_input("Your Guess?", input_guess, 200)
# call new_game 
new_game()


# always remember to check your completed program against the grading rubric
