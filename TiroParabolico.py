from random import randrange
from turtle import *
from freegames import vector

# Editado por 
# Kevin Valdez - A01254336
# Daniela Ruiz - A01254229
# Ximena López - A01254325
# Gustavo Betancourt - A01252532

ball = vector(-200, -200)
speed = vector(0, 0)
targets = []

def tap(x, y):
    "Respond to screen tap."
    if not inside(ball):
        ball.x = -199
        ball.y = -199
        "En esta parte modificamos las sumas de X y Y para que los proyectiles vayan mas rapido"
        speed.x = (x + 500) / 25 
        speed.y = (y + 500) / 25 

def inside(xy):
    "Return True if xy within screen."
    return -200 < xy.x < 200 and -200 < xy.y < 200

def draw():
    "Draw ball and targets."
    clear()

    for target in targets:
        goto(target.x, target.y)
        dot(20, 'blue')

    if inside(ball):
        goto(ball.x, ball.y)
        dot(6, 'red')
    update()

def move():
    "Move ball and targets."
    if randrange(40) == 0:
        y = randrange(-150, 150)
        target = vector(200, y)
        targets.append(target)

    for target in targets:
        "Aqui se modifico para que los balones se movieran mas rapido en el eje X"
        target.x -= 0.5 * 5 

    if inside(ball):
        speed.y -= 0.35
        ball.move(speed)

    dupe = targets.copy()
    targets.clear()

    for target in dupe:
        if abs(target - ball) > 13:
            targets.append(target)

    draw()
    
    "Aqui se retiro un return para que no desaparecieran los balones y asi que volvieran a su posicion original"
    for target in targets:
        if not inside(target):
            target.x = 200

    ontimer(move, 50)

setup(420, 420, 370, 0)
hideturtle()
up()
tracer(False)
onscreenclick(tap)
move()
done()