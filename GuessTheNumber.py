# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console
import simplegui
import math
import random
#Global Variables
secret_number = 0

# helper function to start and restart the game
def new_game():
    global secret_number
	global count
	count = 0
	secret_number is None
	print "New Game"
	


# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    global secret_number
	secret_number = random.randrange (0,100)

def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    global secret_number
	secret_number = random.randrange (0,1000)
    
def input_guess(guess):
    guess = int(guess)
    print "Guess was", guess
    diff = secret_number - guess
    if diff < 0:
        print "Lower!"
    elif diff > 0:
        print "Higher!"
    elif diff == 0:
        print "Correct!"
    else:
        print "Try hard!"


    
# create frame
frame = simplegui.create_frame('Guess the Number by Koly Sengupta', 200, 200)


# register event handlers for control elements and start frame

button1 = frame.add_button('Range is [0, 100]', range100, 200)
button2 = frame.add_button('Range is [0, 1000]', range1000, 200)
inp = frame.add_input('Enter the guess', input_guess, 100)

# call new_game 
new_game()


# always remember to check your completed program against the grading rubric
