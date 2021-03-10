from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Score

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Nadir's Snake Game")
screen.tracer(0)
score_board = 0
snake = Snake()
food = Food()
score = Score()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    # collision of food
    if snake.head.distance(food) < 15:
        food.refresh()
        score.add_score()
        snake.extend()
        print(score.score_board)

    # detect collision wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        is_game_on = False
        score.game_over()

    # detect tail of snake

    for segment in snake.segment:

        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            is_game_on = False
            score.game_over()

screen.exitonclick()
