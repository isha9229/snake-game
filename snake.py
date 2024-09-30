import turtle
import time
import random

# Set up the screen
win = turtle.Screen()
win.title("Nokia Snake Game")
win.bgcolor("black")
win.setup(width=600, height=600)

# Create the snake
snake = turtle.Turtle()
snake.speed(0)
snake.shape("square")
snake.color("white")
snake.penup()

# Create the food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 100)

# Create the score
score = 0
score_keeper = turtle.Turtle()
score_keeper.speed(0)
score_keeper.color("white")
score_keeper.penup()
score_keeper.hideturtle()
score_keeper.goto(0, 260)
score_keeper.write("Score: 0", align="center", font=("Courier", 24, "normal"))

# Create the snake's body
body = []

# Movement functions
def move_up():
    if snake.heading() != 270:
        snake.setheading(90)

def move_down():
    if snake.heading() != 90:
        snake.setheading(270)

def move_left():
    if snake.heading() != 0:
        snake.setheading(180)

def move_right():
    if snake.heading() != 180:
        snake.setheading(0)

# Keyboard bindings
win.listen()
win.onkey(move_up, "w")
win.onkey(move_down, "s")
win.onkey(move_left, "a")
win.onkey(move_right, "d")

# Main game loop
while True:
    win.update()

    # Check for collision with the border
    if snake.xcor() > 290 or snake.xcor() < -290 or snake.ycor() > 290 or snake.ycor() < -290:
        time.sleep(1)
        snake.goto(0, 0)
        snake.setheading(0)
        for part in body:
            part.goto(1000, 1000)
        body.clear()
        score = 0
        score_keeper.clear()
        score_keeper.write("Score: 0", align="center", font=("Courier", 24, "normal"))

    # Check for collision with the food
    if snake.distance(food) < 15:
        food.goto(random.randint(-290, 290), random.randint(-290, 290))
        new_body = turtle.Turtle()
        new_body.speed(0)
        new_body.shape("square")
        new_body.color("white")
        new_body.penup()
        body.append(new_body)
        score += 1
        score_keeper.clear()
        score_keeper.write("Score: {}".format(score), align="center", font=("Courier", 24, "normal"))

    # Move the snake's body
    for index in range(len(body) - 1, 0, -1):
        x = body[index - 1].xcor()
        y = body[index - 1].ycor()
        body[index].goto(x, y)

    if len(body) > 0:
        x = snake.xcor()
        y = snake.ycor()
        body[0].goto(x, y)

    # Move the snake
    snake.forward(20)

    # Check for collision with the snake's body
    for part in body:
        if part.distance(snake) < 15:
            time.sleep(1)
            snake.goto(0, 0)
            snake.setheading(0)
            for part in body:
                part.goto(1000, 1000)
            body.clear()
            score = 0
            score_keeper.clear()
            score_keeper.write("Score: 0", align="center", font=("Courier", 24, "normal"))

    time.sleep(0.1)