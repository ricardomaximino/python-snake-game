from turtle import Screen
from Snake import Snake
from Food import Food
from ScoreBoard import ScoreBoard
import time

screen = Screen()
screen.setup(1000, 900)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)
screen.update()
score_board = ScoreBoard()
snake = Snake()
food = Food()

screen.listen()
screen.onkey(snake.move_up, "Up")
screen.onkey(snake.move_down, "Down")
screen.onkey(snake.turn_left, "Left")
screen.onkey(snake.turn_right, "Right")

is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with the food
    if snake.head.distance(food) < 18:
        food.refresh()
        score_board.increase_score()
        snake.increase_body()

    # Detect collision with the wall
    if snake.head.xcor() > 480 or snake.head.xcor() < -500 or snake.head.ycor() > 450 or snake.head.ycor() < -450:
        snake.reset()
        score_board.reset()

    # Detect collision with the body
    for snake_body_piece in snake.body[1:]:
        if snake.head.distance(snake_body_piece) < 10:
            snake.reset()
            score_board.reset()

if not is_game_on:
    exit(0)
screen.exitonclick()
