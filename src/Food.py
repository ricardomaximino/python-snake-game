from turtle import Turtle
import random

SHAPE = "square"
COLOR = "white"
SIZE = 1
SPEED = "fastest"


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape(SHAPE)
        self.penup()
        self.shapesize(stretch_len=SIZE, stretch_wid=SIZE)
        self.color(COLOR)
        self.speed(SPEED)
        self.refresh()

    def refresh(self):
        random_x = random.randint(-410, 410)
        random_y = random.randint(-410, 410)
        self.goto(random_x, random_y)
