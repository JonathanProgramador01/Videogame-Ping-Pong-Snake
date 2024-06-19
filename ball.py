## Estaaa es la respondable de que se muevaaa mi pelotaaa
from turtle import *
import random
POCIONES_DE_X = [-15, 15]
POCIONES_DE_Y = [20,10,-20,-10,15,-15]
class Ball:
    def __init__(self):
        self.ball = Turtle(shape="circle")
        self.ball.color("black")
        self.avanzar_x = random.choice(POCIONES_DE_X)
        self.avanzar_y = random.choice(POCIONES_DE_Y)
        self.ball.penup()


    def start(self):
        self.ball.home()
        self.avanzar_y = random.choice(POCIONES_DE_Y)
        self.avanzar_x = self.avanzar_x * -1

    def move_ball(self):
        x = self.ball.xcor() + self.avanzar_x
        y = self.ball.ycor() + self.avanzar_y
        self.ball.goto(x, y)
    def pared_de_y(self):
        if self.ball.ycor() >= 258 or self.ball.ycor() <= -258:
            #print("ESTA TOCANDOOO LA PAREDDDD")
            return True

    def pared_de_x_del_jugador1(self):
        if self.ball.xcor() >= 600:
            return True
    def pared_de_x_del_jugador2(self):
        if self.ball.xcor() <= -600:
            return True


    def cambiar_direccion_de_y(self):
        self.avanzar_y *= -1

    def distancia(self, jugador1, jugador2):
        #print("Jugador 1 ",self.ball.distance(jugador1))
        #print("Jugadoe 2 ",self.ball.distance(jugador2))
        #print("DISTANCIA DE x", self.ball.xcor())
        if self.ball.xcor() >= 550 or self.ball.xcor() <= -550:
            #print("ESTA TOCADOOO LA BARDAA DE XXXXX")
            if self.ball.distance(jugador1) < 55 or self.ball.distance(jugador2) < 55:
                return True


#### flag = 1 es para mi pared y
##### flag = 2 es para mi barra x
    def cambio_de_direccion_de_x(self):
            self.avanzar_x *= -1
    def get_y(self):
        return self.ball.ycor()


    def get_x(self):
        return self.ball.xcor()

