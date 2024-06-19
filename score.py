from turtle import *

class Score(Turtle):
    def __init__(self):
        super().__init__(visible=False)
        self.penup()
        self.speed(0)
        self.color("#CCAACC")
        self.score_jugador1 = 0
        self.score_jugador2 = 0

        self.score_del_jugador1()
        self.score_del_jugador2()

    def score_del_jugador1(self):
        self.goto(120.0, 100.0)
        self.write(arg=str(self.score_jugador1), move=False, align="center", font=("Arial", 120, "bold"))
    def score_del_jugador2(self):
        self.goto(-120.0, 100.0)
        self.write(arg=str(self.score_jugador2), move=False, align="center", font=("Arial", 120, "bold"))

    def punto_jugador1(self):
        self.clear()
        self.score_jugador1 += 1
        self.score_del_jugador1()
        self.score_del_jugador2()

    def punto_jugador2(self):
        self.clear()
        self.score_jugador2 += 1
        self.score_del_jugador2()
        self.score_del_jugador1()

    def chechar_scores_jugador1(self):
        if self.score_jugador1 == 5:
            return True
    def chechar_scores_jugador2(self):
        if self.score_jugador2 == 5:
            return True

    def ganador(self):
        self.textinput(title, "GANASTEEEE")





