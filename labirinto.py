"""Labirinto - atravesse se for capaz.

Este jogo está parcialmente implementado.
Seu objetivo é compreender o funcionamento do código
e completar ou melhorar os trechos indicados com TODO,
para que fique funcionalmente semelhante ao jogo
presente no pacote freegames.

Depois, você deverá resolver os desafios propostos abaixo:

1. Manter pontuação contando os cliques (e tempo).
2. Gerar o mesmo labirinto duas vezes.
3. Permitir que o jogador desfaça o último movimento.
4. Fazer com que o caminho percorrido seja gradualmente.
5. Evitar que no primeiro clique seja feito um traço.
"""

import turtle

import random

import time

from random import random

from freegames import line

screen = turtle.Screen()

pontos = 0

score_display = turtle.Turtle()
score_display.speed(0)
score_display.color("black")
score_display.penup()
score_display.hideturtle()
score_display.goto(0, 260)

def desenhar():
    """Desenha o labirinto."""
    turtle.color('black')
    turtle.width(5)

    for x in range(-200, 200, 40):
        for y in range(-200, 200, 40):
            if random() > 0.5:
                line(x, y, x + 40, y + 40)
            else:
                # TODO desenhar uma linha que vai do ponto (x, y + 40) ao ponto (x + 40, y)
                line(x, y + 40, x + 40, y)
                pass

    turtle.update()

def aumentar_pontuacao():
    global pontos
    pontos += 1
    atualizar_placar()
    print(f"Pontuação atual: {pontos}")

def toque(x, y):
    """Desenha o caminho do jogador ao clicar."""
    if abs(x) > 198 or abs(y) > 198:
        turtle.up()
    else:
        turtle.down()

    turtle.width(2)
    turtle.color('red')
    turtle.goto(x, y)
    turtle.dot(4)

    aumentar_pontuacao()

def atualizar_placar():
    score_display.clear()
    score_display.write(f"Pontuação: {pontos}", align="center", font=("Arial", 20, "normal"))



turtle.setup(420, 420, 370, 0)
turtle.hideturtle()
turtle.tracer(False)
    
# TODO chamar função que desenha o labirinto
desenhar()

# TODO Associar função toque ao clique do mouse
screen.onscreenclick(toque, btn=1)
atualizar_placar()

turtle.mainloop()