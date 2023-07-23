# Desenhar uma estrela de 5 pontas
import turtle


def main():

    x = 300
    for _ in range(5):
        # O angulo externo seria 180° menos o valor do angulo interno.
        # Sendo este 180° menos duas vezes o valor do angulo externo do pentagrama (72°)
        turtle.forward(x)
        turtle.left(2 * 72) # Valor do angulo externo simplificado

    turtle.done()

if __name__ == '__main__':

    main()