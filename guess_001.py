# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console
import random
import simplegui

# number of guesses
number_guess = 7


# helper function to start and restart the game
def new_game():
    global number_guess
    global guess
    input_guess(guess)
    range100()
    range1000()
    # initialize global variables used in your code here
    
   
def decrement():
    global number_guess
    number_guess = number_guess - 1
    return number_guess 

# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a
    new_game() 
    secret_number = random.randrange(1, 100)
    # remove this when you add your code    
    return secret_number

def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    new_game()
    secret_number = random.randrange(1,1000)
    return secret_number
    
def input_guess(guess):
    # main game logic goes here	
    guessed_number = int(guess)
    # if button pressed for whatever...
    range100()
    range1000()
    
    if guessed_number == secret_number:
        print "You guessed correctly!"
        new_game()
        
    elif guessed_number > secret_number:
        print "Lower!"
        decrement()
        if number_guess == 0:
            new_game()
           
        # fix the counter going down
    elif guessed_number < secret_number:
        print "Higher!"
        decrement()
        if number_guess == 0:
            new_game()
                
    else:
        print "This should never print"
        new_game()
    return guessed_number
    
 
       
# create frame
frame = simplegui.create_frame("Guessing Game", 500, 500)

# register event handlers for control elements and start frame
# buttons for range 1 through 100 and 1 through 1000
frame.add_button("Range:1 - 100", range100, 100)
frame.add_button("Range:1 - 1000", range1000, 100)
# enter for input
frame.add_input("Your Guess?", input_guess, 200)

# call new_game 
new_game()
