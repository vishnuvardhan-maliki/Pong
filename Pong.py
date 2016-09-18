# Implementation of classic arcade game Pong

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True
score1=0
score2=0

# initialize ball_pos and ball_vel for new bal in middle of table
ball_pos=[WIDTH/2,HEIGHT/2]
ball_vel=[(random.randrange(120, 240))/60,(random.randrange(60, 180))/60]

# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    ball_vel=[(random.randrange(120, 240))/60,(random.randrange(60, 180))/60]
    ball_pos=[WIDTH/2,HEIGHT/2]
    if(direction==LEFT):
        ball_vel[0]=-ball_vel[0]
        ball_vel[1]=ball_vel[1]
        
    elif(direction==RIGHT):
        ball_vel[1]=ball_vel[1]  
# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel,ball_pos  # these are numbers
    global score1, score2  # these are ints
    paddle1_pos=HEIGHT/2
    paddle2_pos=HEIGHT/2
    paddle1_vel=0
    paddle2_vel=0
    score1=0
    score2=0
    ball_pos=[WIDTH/2,HEIGHT/2]
    
def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel,paddle1_vel,paddle2_vel
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
       
    # update ball
    ball_pos[0]+=ball_vel[0]
    ball_pos[1]-=ball_vel[1]
            
    # draw ball
    canvas.draw_circle([ball_pos[0],ball_pos[1]],BALL_RADIUS,2,'White','White')
    # update paddle's vertical position, keep paddle on the screen
    paddle1_pos+=paddle1_vel
    paddle2_pos+=paddle2_vel
    if(paddle1_pos+40>HEIGHT):
        paddle1_vel=0
    if(paddle2_pos+40>HEIGHT):
        paddle2_vel=0
    if(paddle1_pos-40<0):
        paddle1_vel=0
    if(paddle2_pos-40<0):
        paddle2_vel=0
    
        
    # draw paddles
    canvas.draw_line((1,paddle1_pos-40), (1,paddle1_pos+40), 9, 'White')
    canvas.draw_line((WIDTH,paddle2_pos-40),(WIDTH,paddle2_pos+40),9,'White')
    
    # determine whether paddle and ball collide
    if(ball_pos[1]+20>=HEIGHT):
        ball_vel[1]=-ball_vel[1]
    if(ball_pos[1]<20):
        ball_vel[1]=-ball_vel[1]
    if(ball_pos[0]+20>WIDTH):
        ball_vel[0]=-ball_vel[0]
    if(ball_pos[0]<20):
        ball_vel[0]=-ball_vel[0]
    
    
    # draw scores
    canvas.draw_text(str(score1),(100,50),50,'Red')
    canvas.draw_text(str(score2),(500,50),50,'Red')
    if (not(ball_pos[1]>=paddle1_pos-40 and ball_pos[1]<=paddle1_pos+40)):
        
        if(ball_pos[0]<20):
            score2=score2+1
            spawn_ball(RIGHT)
            
    if((ball_pos[1]>=paddle1_pos-40 and ball_pos[1]<=paddle1_pos+40)and ball_pos[0]<=20):
        ball_vel[0]+=0.1*ball_vel[0]
       
    
    if(not(ball_pos[1]>=paddle2_pos-40 and ball_pos[1]<=paddle2_pos+40)):
        
        if(ball_pos[0]+20>WIDTH):
            score1=score1+1
            spawn_ball(LEFT)
    
    if((ball_pos[1]>=paddle2_pos-40 and ball_pos[1]<=paddle2_pos+40)and ball_pos[0]<=20):
        ball_vel[0]+=0.1*ball_vel[0]
        
   
        
def keydown(key):
    global paddle1_vel, paddle2_vel
    if (key==simplegui.KEY_MAP["s"] and paddle1_pos+40<HEIGHT):
        paddle1_vel=8
    elif (key==simplegui.KEY_MAP["down"] and paddle2_pos+40<HEIGHT):
        paddle2_vel=8
    elif (key==simplegui.KEY_MAP["w"]and paddle1_pos-40>0):
        paddle1_vel=-8
    elif(key==simplegui.KEY_MAP["up"]and paddle2_pos-40>0):
        paddle2_vel=-8
        
        
def keyup(key):
    global paddle1_vel, paddle2_vel
    if (key==simplegui.KEY_MAP["s"]):
        paddle1_vel=0
    elif (key==simplegui.KEY_MAP["down"]):
        paddle2_vel=0
    elif (key==simplegui.KEY_MAP["w"]):
        paddle1_vel=0
    elif(key==simplegui.KEY_MAP["up"]):
        paddle2_vel=0

#button handler
def handler():
    x=random.choice([LEFT,RIGHT])
    new_game()
    
# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)

button1 = frame.add_button('Restart', handler)

# start frame
new_game()
frame.start()
