###### ESTA DE AQUII ES LA ENCARGAADA DE MIS BARAS
from turtle import *

class Barras:
    def __init__(self,direccion_inicial):
        self.barra = Turtle(shape="square")
        self.barra.shapesize(stretch_wid=1, stretch_len=6)
        self.barra.speed(0)
        self.barra.penup()
        self.barra.setheading(90)
        self.barra.color("#662B99")
        self.barra.goto(x=direccion_inicial, y=0)
    def arriva(self):

        if self.barra.ycor() <= 200:
            self.barra.forward(20)

    def abajo(self):
        if self.barra.ycor() >= -210:
            self.barra.backward(20)


    def bot(self,valor_de_x,valor_anterior,valor_actual,distancia_de_mi_ball):
        if valor_de_x>= 15:
            ##teng que checar mi distanciaa para que no se me mueva des masss
            print("Distanciaaa: ", self.barra.distance(distancia_de_mi_ball))
            if self.barra.distance(distancia_de_mi_ball) >= 100:

                if valor_anterior < valor_actual:
                    if self.barra.ycor() <= 200:
                        self.barra.forward(20)
                else:
                    if self.barra.ycor() >= -210:
                        self.barra.backward(20)



