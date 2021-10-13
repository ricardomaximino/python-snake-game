from turtle import Turtle

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
SHAPE = "square"
COLOR = "white"


class Snake:

    body = []

    def __init__(self):
        self.create_snake()
        self.head = self.body[0]

    def create_snake(self):
        last_x_cor = 0
        self.start = False
        for _ in range(0, 3):
            self.create_body_piece((last_x_cor, 0))
            last_x_cor -= 20

    def create_body_piece(self, position):
        body_piece = Turtle(SHAPE)
        body_piece.color(COLOR)
        body_piece.penup()
        body_piece.goto(position)
        self.body.append(body_piece)

    def increase_body(self):
        self.create_body_piece(self.body[-1].position())

    def reset(self):
        for body_piece in self.body:
            body_piece.goto(1000, 1000)
        self.body.clear()
        self.create_snake()
        self.head = self.body[0]

    def move(self):
        if self.start:
            for snack_piece in range(len(self.body) - 1, 0, -1):
                new_x = self.body[snack_piece - 1].xcor()
                new_y = self.body[snack_piece - 1].ycor()
                self.body[snack_piece].goto(new_x, new_y)
            self.head.forward(20)

    def move_up(self):
        if self.start:
            if self.head.heading() != DOWN:
                self.head.setheading(UP)
        else:
            self.start = True

    def move_down(self):
        if self.start:
            if self.head.heading() != UP:
                self.head.setheading(DOWN)
        else:
            self.start = True

    def turn_right(self):
        if self.start:
            if self.head.heading() != LEFT:
                self.head.setheading(RIGHT)
        else:
            self.start = True

    def turn_left(self):
        if self.start:
            if self.head.heading() != RIGHT:
                self.head.setheading(LEFT)
        else:
            self.start = True
