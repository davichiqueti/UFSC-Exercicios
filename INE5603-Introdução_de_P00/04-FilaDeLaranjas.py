import turtle


constructor = turtle.Turtle()
constructor.speed(50)

def goToWithoutDrawing(x, y):
    # Função para posicionar a tartaruga sem desenhar
    constructor.up()
    constructor.goto(x, y)
    constructor.down()
    constructor.setheading(0)

def main():

    constructor.fillcolor('orange') # Definindo a cor do preenchimento
    orange_ray = 25 # Definindo o raio da laranja
    ray_variation = 5 # Definindo a variação do raio
    pos = 0

    for i in range(8):

        constructor.begin_fill()
        constructor.fillcolor('orange')
        goToWithoutDrawing(pos, 0)
        constructor.circle(orange_ray)
        constructor.end_fill()
        pos += (2 * orange_ray) + ray_variation # Adiciona o diamentro e a variação do raio a posição da tartaruga
        orange_ray += ray_variation

    turtle.done()

if __name__ == '__main__':

    main()