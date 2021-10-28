import time
from turtle import *
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import keyboard

sc = Screen()
sc.bgcolor("black")
sc.setup(height=600, width=600)
sc.title("My Snake Game")

segs = []
sc.tracer(0)    
sc.listen()

snake = Snake()
food = Food()   
scoree = Scoreboard()

sc.onkey(snake.move_right, "Right")
sc.onkey(snake.move_left, "Left")
sc.onkey(snake.move_up, "Up")
sc.onkey(snake.move_down, "Down")

game_is_on = True
while game_is_on:

    sc.update()
    time.sleep(0.1)
    snake.move_forward()

    if snake.head.distance(food) < 20:
        now_col = food.color()[0]
        food.refresh()
        scoree.score += 1
        scoree.ref()
        snake.extend()
        for segs in snake.segs:
            segs.color(now_col)

    if snake.head.xcor() >= 300 or snake.head.xcor() <= -300 or snake.head.ycor() >= 300 or snake.head.ycor() <= -300:
        game_over = Turtle()
        game_over.color("red")
        game_over.write(f"GAME OVER",align="center",font=("Arial",50,"normal"))
        break

    for segment in snake.segs:
        if snake.head == segment:
            pass
        elif snake.head.distance(segment) <= 10:
            game_is_on = False
            game_overr = Turtle()
            game_overr.color("red")
            game_overr.write(f"GAME OVER",align="center",font=("Arial",50,"normal"))

exitonclick()
