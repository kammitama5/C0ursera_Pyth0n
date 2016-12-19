# Rock-paper-scissors-lizard-Spock template


# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# helper functions

def name_to_number(name):
    if name == 'rock':
      return 0
    elif name == 'Spock':
      return 1
    elif name == 'paper':
      return 2
    elif name == 'lizard':
      return 3
    elif name == 'scissors':
      return 4
    else:
      return 'not a valid number'


def number_to_name(number):
    if number == 0:
      return 'rock'
    elif name == 1:
      return 'Spock'
    elif name == 2:
      return 'paper'
    elif name == 3:
      return 'lizard'
    elif name == 4:
      return 'scissors'
    else:
      return -1


def rpsls(player_choice): 
    
    # print a blank line to separate consecutive games
    print "/n"

    # print out the message for the player's choice
    name1 = raw_input("Please enter your choice")
    name = int(name)
    # convert the player's choice to player_number using the function name_to_number()
    name_to_number(name)
    # compute random guess for comp_number using random.randrange()
    comp_number = randrange(0, 4) 
    # convert comp_number to comp_choice using the function number_to_name()
    print(number_to_name(comp_number))
    # print out the message for computer's choice
    
    # compute difference of comp_number and player_number modulo five
    difference = (comp_number - player_number) % 5
    # use if/elif/else to determine winner, print winner message

    
# test your code - THESE CALLS MUST BE PRESENT IN YOUR SUBMITTED CODE
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

# always remember to check your completed program against the grading rubric


