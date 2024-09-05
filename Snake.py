##############
# SNAKE GAME #
##############

# A simple version of the famous snake game is programmed in this file.

# Import library
import turtle
import random
import time

# Game variables
delay = 0.1
score = 0
max_score = 0
segments = []

# Game window setup
window = turtle.Screen()
window.title("Snake Game")
window.bgcolor("black")
window.setup(width=700, height=700)
window.tracer(0)

# Draw borders
turtle.speed(5)
turtle.pensize(4)
turtle.penup()
turtle.goto(-310, 250)
turtle.pendown()
turtle.color("black")
turtle.forward(600)
turtle.right(90)
turtle.forward(500)
turtle.right(90)
turtle.forward(600)
turtle.right(90)
turtle.forward(600)
turtle.penup()
turtle.hideturtle()

# Create snake head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("white")
head.penup()
head.goto(0, 0)
head.direction = "Stop"

# Create food
food = turtle.Turtle()
food_color = random.choice(['yellow', 'green', 'tomato'])
food_shape = random.choice(['triangle', 'circle', 'square'])
food.speed(0)
food.shape(food_shape)
food.color(food_color)
food.penup()
food.goto(20, 20)

# Scoreboard
scoreboard = turtle.Turtle()
scoreboard.speed(0)
scoreboard.shape("square")
scoreboard.color("white")
scoreboard.penup()
scoreboard.hideturtle()
scoreboard.goto(0, 250)
scoreboard.write("Score: 0, Max score: 0", align="center", font=("Courier", 25, "bold"))

# Define movement functions
def move_up():
    if head.direction != "down":
        head.direction = "up"

def move_down():
    if head.direction != "up":
        head.direction = "down"

def move_left():
    if head.direction != "right":
        head.direction = "left"

def move_right():
    if head.direction != "left":
        head.direction = "right"

# Move the snake
def move():
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

# Reset the game
def reset_game():
    global score, delay, segments
    score = 0
    delay = 0.1
    head.goto(0, 0)
    head.direction = "Stop"
    
    # Hide all body segments off-screen
    for segment in segments:
        segment.goto(1000, 1000)
    
    # Clear segments list
    segments.clear()
    
    # Respawn food at a random position
    food.goto(random.randint(-290, 290), random.randint(-290, 290))
    
    # Move the scoreboard back to the top
    scoreboard.goto(0, 250)
    
    # Reset the background color to black
    window.bgcolor('black')
    
    # Reset the scoreboard
    update_scoreboard()

# Game over
def game_over():
    head.direction = "Stop"
    
    # Move scoreboard to the center for the game over message
    scoreboard.goto(0, 0)
    scoreboard.write(f"GAME OVER\nYour score is: {score}\nPress SPACE to restart", align="center", font=("Courier", 30, "bold"))
    
    # Listen for space key to restart the game
    window.listen()
    window.onkey(reset_game, "space")

# Update the scoreboard
def update_scoreboard():
    scoreboard.clear()
    scoreboard.write(f"Score: {score}, Max score: {max_score}", align="center", font=("Courier", 25, "bold"))

# Detect collisions with the border
def check_collision_with_border():
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        game_over()

# Detect collisions with the snake body
def check_collision_with_body():
    for segment in segments:
        if segment.distance(head) < 20:
            game_over()

# Key bindings
window.listen()
window.onkey(move_up, "Up")
window.onkey(move_down, "Down")
window.onkey(move_left, "Left")
window.onkey(move_right, "Right")

# Main game loop
while True:
    window.update()
    
    check_collision_with_border()
    check_collision_with_body()
    
    # Check if the snake eats the food
    if head.distance(food) < 20:
        # Move food to a random position
        food_color = random.choice(['yellow', 'green', 'tomato'])
        food_shape = random.choice(['triangle', 'circle', 'square'])
        food.shape(food_shape)
        food.color(food_color)
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y)

        # Add a new segment to the snake
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)
        
        # Increase score
        score += 10
        if score > max_score:
            max_score = score
        
        # Reduce delay to speed up the snake
        delay -= 0.001
        
        update_scoreboard()
    
    # Move the end segments first in reverse order
    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)

    # Move segment 0 to where the head is
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)
    
    move()
    
    time.sleep(delay)

window.mainloop()