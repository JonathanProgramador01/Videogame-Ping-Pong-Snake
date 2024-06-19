from turtle import Screen
from barras import Barras
from ball import Ball
from lineas import Backgroud
from score import Score
import time
from tkinter import *
from principal import snake

Window_of_tkinter = Tk()
Window_of_tkinter.title("Ping Pong")


canva= Canvas(width=600,height=550)
image = PhotoImage(file="Zoro (ashura).gif")
canva.create_image(325,275,image=image)
canva.pack()




def Pingpong_de_dos_jugadores(flag = 0):
    Window_of_turtle = Screen()
    Window_of_turtle.setup(width=1200, height=600)
    Window_of_turtle.title("Ping Pong")
    Window_of_turtle.bgpic("Mejora.gif")



    Jugador1 = Barras(direccion_inicial=570)
    Jugador2 = Barras(direccion_inicial=-577)

    backgroud = Backgroud()
    ball = Ball()
    score = Score()

    if flag == 1:#1 = de que son de dos jugadores
        Window_of_turtle.onkey(Jugador1.arriva, "Up")
        Window_of_turtle.onkey(Jugador1.abajo, "Down")

    Window_of_turtle.onkey(Jugador2.arriva, "w")
    Window_of_turtle.onkey(Jugador2.abajo, "s")
    Window_of_turtle.listen()



    Window_of_turtle.tracer(0)
    juego_esta_activo = True
    ultimo_tiempo = time.time()
    ultimo_tiempo2 = time.time()
    velocidad = 0.3

    while juego_esta_activo:
        tiempo_actual = time.time()
        if tiempo_actual - ultimo_tiempo >= velocidad:

            valor_anterior = ball.get_y()
            ball.move_ball()
            valor_actual = ball.get_y()

            #print("valor anterior ", valor_anterior)
            #print("Valor despuess ", valor_actual)
            print(ball.get_x())
            if flag == 0:
                Jugador1.bot(ball.get_x(),valor_anterior, valor_actual,ball.ball)


            if ball.distancia(Jugador1.barra, Jugador2.barra):
                ball.cambio_de_direccion_de_x()
            if ball.pared_de_y():
                ball.cambiar_direccion_de_y()

            if ball.pared_de_x_del_jugador1():
                velocidad = 0.3
                ball.start()
                score.punto_jugador2()

            if ball.pared_de_x_del_jugador2():
                velocidad = 0.3
                score.punto_jugador1()
                ball.start()

            ultimo_tiempo = tiempo_actual



        if tiempo_actual - ultimo_tiempo2 >= 0.5: #este es el encargado de mi velocidad
            if velocidad <= 0.01:
                velocidad = 0.01
            else:
                velocidad -= 0.00161
            ultimo_tiempo2 = tiempo_actual

        if score.chechar_scores_jugador1():



            juego_esta_activo = False

        if score.chechar_scores_jugador2():


            juego_esta_activo = False


        Window_of_turtle.update()










def vs(): #este es cuando es de dos jugadoresss
    Window_of_tkinter.destroy()
    Pingpong_de_dos_jugadores(1)

imagen_de_mi_boton1 = PhotoImage(file="file (1).gif")
button = Button( text="Ping Pong", font=("Arial",15,"bold"),bg="#71DD5D", image=imagen_de_mi_boton1, compound="top")
button.config(width=170,height=330, highlightthickness=0,command=vs)
button.place(x=100, y=120)




def Pc(): #### este es de un jugadorrr osea con un bottt
    Window_of_tkinter.destroy()
    snake()




imagen_de_mi_boton2 = PhotoImage(file="file (5).gif")
button2 = Button( text="Snake",font=("Arial",15,"bold"),bg="#FBB006", image=imagen_de_mi_boton2, compound="top")
button2.config(width=170,height=330,highlightthickness=0, command=Pc)
button2.place(x=350, y=120)






Window_of_tkinter.mainloop()




