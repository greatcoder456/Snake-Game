import turtle
import time
import random

# Define Global Variables
delay = 0.2
score = 0
high_score = 0
segments = []

#Setting up the screen, title, background color, width etc.
# must return the window created
def setUpScreen():
    # Set up the screen
    wn = turtle.Screen()
    wn.title('Snake Game')
    # Set background color
    wn.bgcolor('grey')
    # Set height and width
    wn.setup(600, 600)
    # Turns off the screen updates
    wn.tracer(0)
    return wn

# Write score and highscore on the screen
def trackScoreOnScreen():
    pen = turtle.Turtle()
    # Set color
    pen.color('white')
    # penup and hide turtle
    pen.penup()
    pen.hideturtle()
    # Move the score to top of screen
    pen.goto(0,260)
    pen.write("Score: 0  High Score: 0", align="center", font=("Courier", 24, "normal"))
    return pen

# Create and return the Head of the snake
def createSnakeHead():
    # Snake head
    head = turtle.Turtle()
    # Set speed, shape, color and move it center of the screen
    head.speed(0)
    head.shape('square')
    head.color('black')
    head.penup()
    head.goto(0,0)
    # Set direction as stop
    head.direction= 'stop'
    return head

# Create and return the first food on the screen
def createFood():
    # Create Snake food
    food = turtle.Turtle()
    # Set speed, shape, color and move it some location of the screen
    head.speed(0)
    head.color('yellow')
    head.shape('circle')
    head.penup()
    x = random.randrange(-250,250)
    y = random.randrange(-250, 250)
    head.goto(100, 0)
    return food

# Function to call when up key is pressed
# Snake can go up only when the direction is right or left and not down
def go_up():
    # remove print statement after implementing this function
    if head.direction != 'down':
        head.direction='up'


# Function to call when down key is pressed
# Snake can go down only when the direction is right or left and not up
def go_down():
     # remove print statement after implementing this function
    if head.direction != 'up':
        head.direction='down'

# Function to call when left key is pressed
# Snake can go left only when the direction is up or down and not right
def go_left():
    # remove print statement after implementing this function
    if head.direction != 'right':
        head.direction = 'left'

# Function to call when right key is pressed
# Snake can go right only when the direction is up or down and not left
def go_right():
    # remove print statement after implementing this function
    if head.direction != 'left':
        head.direction='right'
        

# Bind Up, Down, Left and Right keys with their function
def bindKeyboardKeys(win):
    # remove print statement after implementing this function
    win.listen()
    win.onkeypress(go_up, 'Up')
    win.onkeypress(go_down, 'Down')
    win.onkeypress(go_left, 'Left')
    win.onkeypress(go_right, 'Right')

# Function to call to move the snake, based on the direction of the snake
# snake body should move automatically in that direction
# should be called from the main loop. 
def moveHead():
    # remove print statement after implementing this function
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

# Move segments

def moveSegments():
    global segments
    
    # Move the end segments first in reverse order
    # Using for loop move the segments
    # For example if there are 3 segments 2, 1, and 0
    # Move second segment to location of first and move first segment to location of zero
    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)


    # Move segment 0 to where the head is
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x,y)


# Detect collision of snake head with the screen borders
# If collision detected return True else return False
def detectCollisionWithBorder(head):
    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
        return True
    # remove print statement after implementing this function
    
    return False

# Handle the collision if detected true
def handleCollisionWithBorder(head, trackScore):
    global delay
    global score
    
    # Make head goto center of the screen
    head.goto(0,0)
    # Make head goto center of the screen
    head.goto(0,0)
    # Make head direction dummy so that it do not move
    head.direction = "stop"
    # Hide the segments
    for segment in segments:
        segment.goto(1000, 1000)
    # Clear the segments list
    segments.clear()
    # Reset the score
    score = 0
    # Reset the delay
    delay = 0.2
    # Clear trackscore and start from 0
    trackScore.clear()
    trackScore.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal")) 
    

# Detect collision of snake head with food
# If collision detected return True else return False
def detectCollisionWithFood(head, food):
    # remove print statement after implementing this function
    if head.distance(food) < 20:
        return True
    return False

# Handle the collision if detected true
def handleCollisionWithFood(head, trackScore, food):
    global delay
    global score
    global high_score
    
    # Move the food to a random spot
    x = random.randint(-290, 290)
    y = random.randint(-290, 290)
    food.goto(x,y)

    # Add a segment, define its shape and color
    # append it to the segments list
    new_segment = turtle.Turtle()
    new_segment.speed(0)
    new_segment.shape("square")
    new_segment.color("blue")
    new_segment.penup()
    segments.append(new_segment)

    # Shorten the delay, to move snake faster
    delay -= 0.001

    # Increase the score by 10
    score += 10

    # check for high score and update it if player made a new high score
    if score > high_score:
        high_score = score
    
    # Update trackScore 
    trackScore.clear()
    trackScore.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))  


# Detect collision of snake head with its body
# needs to check for all segment, thus will use for loop
# If collision detected return True else return False
def detectCollisionOfHeadWithSegment(head):
    # remove print statement after implementing this function
    for segment in segments:
        if segment.distance(head) < 20:
            return True
    
    return False


####################################
#                                  #
#   Start of the main function     #
#                                  #
####################################

#Call Functions in main program
wn = setUpScreen()
head = createSnakeHead()
food = createFood()
trackScore = trackScoreOnScreen()
bindKeyboardKeys(wn)

# Start of main game loop
while True:
    wn.update()
    
    # Check for a collision of head with the screen border
    if detectCollisionWithBorder(head):
        time.sleep(1)
        handleCollisionWithBorder(head, trackScore)

    # Check for a collision with the food
    if detectCollisionWithFood(head, food):
        handleCollisionWithFood(head, trackScore, food)
        
    moveSegments()
    moveHead()    

    # Detect collision of snake body with its head
    if detectCollisionOfHeadWithSegment(head):
        time.sleep(1)
        handleCollisionWithBorder(head, trackScore)
        
    # Sleep for time equal to delay to add delay
    time.sleep(delay)


wn.mainloop()