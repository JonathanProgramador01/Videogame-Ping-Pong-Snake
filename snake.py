from turtle import Turtle
CORDENADAS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
class Snake:

    def __init__(self):
        self.snakes = []
        self.star()
        self.head = self.snakes[0]


    def star(self):
        for posicion in CORDENADAS:
            self.add_segment(posicion)


    def add_segment(self,position):
        cuerpo = Turtle("square")
        cuerpo.color("light slate gray")
        cuerpo.penup()
        cuerpo.goto(position)
        self.snakes.append(cuerpo)


    def extend(self):
        self.add_segment(self.snakes[-1].position())







    def move(self):
        for i in range(len(self.snakes) - 1, 0, -1):
            x = self.snakes[i - 1].xcor()
            y = self.snakes[i - 1].ycor()
            self.snakes[i].goto(x, y)
        self.snakes[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
