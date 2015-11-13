# Implementation of classic arcade game Pong

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 15
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True

# initialize ball_pos and ball_vel for new bal in middle of table
ball_pos = [0,0]
ball_vel = [0.0,0.0]
paddle1_pos = float(HEIGHT/2)
paddle2_pos = float(HEIGHT/2)
paddle1_vel = float(0)
paddle2_vel = float(0)
pad_acc = 5
score1 = 0
score2 = 0
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    ball_pos = [WIDTH/2, HEIGHT/2]
    ball_vel[0] = random.randrange(2,4)
    ball_vel[1] = random.randrange(1,3)
    if direction == RIGHT:
        ball_vel[1] = - ball_vel[1]
    if direction == LEFT:
        ball_vel[0] = - ball_vel[0]
        ball_vel[1] = - ball_vel[1]      
#    print ball_vel, ball_pos
    
# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2# these are ints
    paddle1_pos = float(HEIGHT/2)
    paddle2_pos = float(HEIGHT/2)
    paddle1_vel = float(0)
    paddle2_vel = float(0)
    score1 = 0
    score2 = 0
    spawn_ball(RIGHT)

def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
    # update paddle's vertical position, keep paddle on the screen
    if paddle1_pos + paddle1_vel >= HALF_PAD_HEIGHT and paddle1_pos + paddle1_vel <= HEIGHT - HALF_PAD_HEIGHT:
        paddle1_pos += paddle1_vel
        
    if paddle2_pos + paddle2_vel >= HALF_PAD_HEIGHT and paddle2_pos + paddle2_vel <= HEIGHT - HALF_PAD_HEIGHT:
        paddle2_pos += paddle2_vel

    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
    
    # draw paddles
    #    paddle1
    pad1_top = [HALF_PAD_WIDTH, paddle1_pos - HALF_PAD_HEIGHT]
    pad1_bot = [HALF_PAD_WIDTH, paddle1_pos + HALF_PAD_HEIGHT]
    canvas.draw_line(pad1_top, pad1_bot, PAD_WIDTH, "White")
    #    paddle2
    pad2_top = [WIDTH - HALF_PAD_WIDTH, paddle2_pos - HALF_PAD_HEIGHT]
    pad2_bot = [WIDTH - HALF_PAD_WIDTH, paddle2_pos + HALF_PAD_HEIGHT]
    canvas.draw_line(pad2_top, pad2_bot, PAD_WIDTH, "White")
    
    # update ball
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]  
    
    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 1, "RED", "WHITE")
    
    #Reflection Top and Bottom Wall:
    if ball_pos[1] >= HEIGHT - BALL_RADIUS:
        ball_vel[1] = - ball_vel[1]
    elif ball_pos[1] <= BALL_RADIUS:
        ball_vel[1] = - ball_vel[1]
        
    # determine whether paddle and ball collide    
    if (ball_pos[0] <= PAD_WIDTH + BALL_RADIUS):	# if it hits left wall
        # If ball position is between vertical range of paddles
        if (paddle1_pos - HALF_PAD_HEIGHT <= ball_pos[1] <= paddle1_pos + HALF_PAD_HEIGHT):
            ball_vel[0] = - ball_vel[0]
            # incrementing velocity of ball by 10%
            ball_vel[0] += ball_vel[0] * .10
            ball_vel[1] += ball_vel[1] * .10
            score1 = score1 + 1
            
        # else it scores, respawns ball
        else:
            score2 += 1
            spawn_ball(True)
            
    if (ball_pos[0] >= WIDTH - PAD_WIDTH - BALL_RADIUS):	#if it hits right wall
        # If ball position is between vertical range of paddles
        if (paddle2_pos - HALF_PAD_HEIGHT <= ball_pos[1] <= paddle2_pos + HALF_PAD_HEIGHT):
            ball_vel[0] = - ball_vel[0]
            # incrementing velocity of ball by 10%
            ball_vel[0] += ball_vel[0]* .10
            ball_vel[1] += ball_vel[1]*.10
            score2 = score2 + 1
            
        # else it scores, respawns ball
        else:
            score1 += 1
            spawn_ball(False)
                   
        print "ball_vel", ball_vel, "Score1", score1, "Score2", score2
    
    # draw scores
    canvas.draw_text(str(score1), [150,50], 45, "White")
    canvas.draw_text(str(score2), [450,50], 45, "White")
        
def keydown(key):
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP["up"]:
        paddle2_vel -= pad_acc
    elif key == simplegui.KEY_MAP["down"]:
        paddle2_vel += pad_acc
    elif key == simplegui.KEY_MAP['w']:
        paddle1_vel -= pad_acc
    elif key == simplegui.KEY_MAP['s']:
        paddle1_vel += pad_acc

def keyup(key):
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP["up"]:
        paddle2_vel += pad_acc
    elif key == simplegui.KEY_MAP["down"]:
        paddle2_vel -= pad_acc
    elif key == simplegui.KEY_MAP['w']:
        paddle1_vel += pad_acc
    elif key == simplegui.KEY_MAP['s']:
        paddle1_vel -= pad_acc



frame = simplegui.create_frame("Pong Game by Koly Sengupta", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)

# start frame
frame.start()
new_game()
