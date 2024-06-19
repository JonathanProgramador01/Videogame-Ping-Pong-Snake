from turtle import Turtle

class Backgroud(Turtle):
    def __init__(self):
        super().__init__(shape="turtle",visible=False)
        self.penup()
        self.speed(0)
        self.goto(x=0, y=-280)
        self.setheading(90)
        self.pen(pencolor="#CCAACC", pensize=10, speed=0)
        self.dotted_lines()
        self.goto(x=600, y=280)
        self.setheading(180)
        self.complet_line()
        self.goto(x=600, y=-280)
        self.complet_line()




    def dotted_lines(self):
        for i in range(14):
            self.pendown()
            self.forward(20)
            self.penup()
            self.forward(20)

    def complet_line(self):
        self.pendown()
        for i in range(60):
            self.forward(20)
        self.penup()