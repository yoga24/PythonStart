import turtle
import time
import random

turtleVar = turtle.Pen()
# turtleVar.forward(50)
# turtleVar.left(90)
# turtleVar.forward(50)
# turtleVar.left(90)
# turtleVar.forward(50)
# turtleVar.left(90)
# turtleVar.forward(50)

for side in range(0, 4):
    turtleVar.forward(50)
    turtleVar.left(90)

time.sleep(2)
turtleVar.reset()
for side in range(1, 38):
    turtleVar.forward(200)
    turtleVar.left(175)

time.sleep(2)

turtleVar.reset()


def square(a):
    for side in range(0, 4):
        turtleVar.forward(a)
        turtleVar.left(90)


turtleVar.up()
turtleVar.right(90)
turtleVar.forward(200)
turtleVar.right(90)
turtleVar.forward(200)
turtleVar.right(180)
turtleVar.down()

randomList = []

for leng in range(20, 700, 50):
    rand = random.randint(5, 400)
    while rand in randomList:
        rand = random.randint(5, 400)
    square(rand)

# square(5)
# square(10)
# square(25)
# square(50)
# square(100)
# square(200)
# square(400)
# square(800)

time.sleep(5)
