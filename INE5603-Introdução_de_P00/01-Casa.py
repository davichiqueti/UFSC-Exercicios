# Etapas:
# 1. Definir dados iniciais
# 2. Desenhar o corpo da casa
# 3. Desenhar a porta
# 4. Desenhar a janela
# 5. Desenhar o telhado
import turtle
import math
import time


u = 100
constructor = turtle.Turtle()

def buildHomeBase(): 
    # 2. Desenhar o corpo da casa
    constructor.fillcolor('#d7c7b8')
    constructor.begin_fill() # Inicia o preenchimento da cor

    for _ in range(2):

        constructor.forward(2 * u)
        constructor.left(90)
        constructor.forward(u)
        constructor.left(90)
    
    constructor.end_fill()

def buildHomeDoor():
    # 3. Desenhar a porta
    constructor.fillcolor('#c93731')
    constructor.begin_fill() # Inicia o preenchimento da cor
    constructor.left(90)
    constructor.forward(2*u / 3)
    constructor.right(90)
    constructor.forward(u / 3)
    constructor.right(90)
    constructor.forward(2*u / 3)
    constructor.end_fill() 

def buildHomeWindow(): 
    # 4. Desenhar a janela
    constructor.fillcolor('#FFFFFF')
    constructor.begin_fill() # Inicia o preenchimento da cor

    for _ in range(4):

        constructor.forward(u / 3)
        constructor.left(90)
    
    constructor.end_fill()
    # Adionar um traço para o desenho das janelas
    constructor.forward(u / 6)
    constructor.left(90)
    constructor.forward(u / 3)
    constructor.left(90)

    for _ in range(2):

        constructor.forward(u / 6)
        constructor.left(90)

    constructor.forward(u / 3)

def buildHomeRoof(): 
    # 5. Desenhar o telhado com beiral
    constructor.fillcolor('#8b5742')
    constructor.begin_fill() # Inicia o preenchimento da cor
    constructor.left(45)

    for _ in range (2):

        constructor.left(90)
        constructor.forward(u * math.sqrt(2))

    # Adicionar um beiral
    constructor.forward(u / 6)
    constructor.left(135)
    constructor.forward(2 * math.sqrt((u/6)**2 / 2) + 2 * u)
    constructor.left(135)
    constructor.forward(u / 6)
    constructor.end_fill()

def goToWithoutDrawing(x, y):
    # Função para posicionar a tartaruga sem desenhar
    constructor.up()
    constructor.goto(x, y)
    constructor.down()
    constructor.setheading(0) # Deixar a tartaruga com um direcionamento neutro

def main():
    # 1. Definir dados iniciais
    buildHomeBase() # 2. Desenhar o corpo da casa
    goToWithoutDrawing(u/3, 0)
    buildHomeDoor() # 3. Desenhar a porta
    goToWithoutDrawing(u, u/3)
    buildHomeWindow() # 4.1 Desenhar a janela 1
    goToWithoutDrawing(1.5 * u, u/3)
    buildHomeWindow() # 4.2 Desenhar a janela 2
    goToWithoutDrawing(2 * u , u)
    buildHomeRoof() # 5. Desenhar o telhado com beiral
    turtle.done()


if __name__ == '__main__':

    main()