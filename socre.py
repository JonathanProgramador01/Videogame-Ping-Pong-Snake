from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.inicialisacion()
        self.score = 0
        self.incremet_score()

    def inicialisacion(self):
        self.color("white")
        self.penup()
        self.hideturtle()
        self.setheading(90)
        self.forward(270)
        self.speed(0)
    def incremet_score(self):
        self.write(f"Score: {self.score}", False, "center", ("Arial", 20, "bold"))
        self.score += 1
    def game_over(self):
        self.goto(0,0)
        self.write("GAMEE OVER", False, "center", ("Arial", 50, "bold"))
