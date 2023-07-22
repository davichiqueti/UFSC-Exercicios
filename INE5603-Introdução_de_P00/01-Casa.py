# Etapas:
# 1. Definir dados iniciais
# 2. Desenhar o corpo da casa
# 3. Desenhar a porta
# 4. Desenhar a janela
# 5. Desenhar o telhado
import turtle
import math
import time


def buildHomeBase(constructor,x): 
    # 2. Desenhar o corpo da casa
    constructor.fillcolor('#d7c7b8')
    constructor.begin_fill() # Inicia o preenchimento da cor

    for _ in range(2):

        constructor.forward(2 * x)
        constructor.left(90)
        constructor.forward(x)
        constructor.left(90)
    
    constructor.end_fill()

def buildHomeDoor(constructor,x):
    # 3. Desenhar a porta
    constructor.fillcolor('#c93731')
    constructor.forward(x / 3)
    constructor.begin_fill() # Inicia o preenchimento da cor
    constructor.left(90)
    constructor.forward(2*x / 3)
    constructor.right(90)
    constructor.forward(x / 3)
    constructor.right(90)
    constructor.forward(2*x / 3)
    constructor.end_fill() 

def buildHomeWindow(constructor,x): 
    # 4. Desenhar a janela
    constructor.fillcolor('#FFFFFF')
    constructor.up() # Não desenhar
    constructor.left(90)
    constructor.forward(x / 3)
    constructor.left(90)
    constructor.forward(x / 3)
    constructor.down() # Voltar a desenhar
    constructor.begin_fill() # Inicia o preenchimento da cor
    [(constructor.forward(x / 3), constructor.right(90)) for i in range(4)]
    constructor.end_fill()
    constructor.up()
    constructor.right(90)
    constructor.forward(x / 3 + x / 6)
    constructor.left(90)
    constructor.down()
    constructor.begin_fill()
    [(constructor.forward(x / 3), constructor.right(90)) for i in range(4)]
    constructor.end_fill()

def buildHomeRoof(constructor,x): 
    # 5. Desenhar o telhado
    constructor.fillcolor('#8b5742')
    constructor.up() # Não desenhar
    constructor.forward(2 * x / 3)
    constructor.right(90)
    constructor.forward(x / 3 + x / 6)
    constructor.left(45)
    constructor.down() # Voltar a desenhar
    constructor.begin_fill() # Inicia o preenchimento da cor
    [(constructor.left(90), constructor.forward(x * math.sqrt(2))) for i in range(2)]
    # Adicionar um beiral
    constructor.forward(x / 6)
    constructor.left(135)
    constructor.forward(2 * math.sqrt((x/6)**2 / 2) + 2 * x)
    constructor.left(135)
    constructor.forward(x / 6)
    constructor.end_fill()

def main():
    # 1. Definir dados iniciais
    x = 100
    constructor = turtle.Turtle()
    # Chamar funções de desenho
    buildHomeBase(constructor,x)
    buildHomeDoor(constructor,x)
    buildHomeWindow(constructor,x)
    buildHomeRoof(constructor,x)
    turtle.done()

if __name__ == '__main__':

    main()