import turtle
import threading
import time
from playsound import playsound

wn = turtle.Screen()
wn.title("Pong")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

#SCORE
score_a = 0
score_b = 0

#PADLE A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

#PADDLE B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

#LINE
line = turtle.Turtle()
line.speed(0)
line.shape("square")
line.color("gray")
line.shapesize(stretch_wid=30, stretch_len=0.07)
line.penup()
line.goto(0, 0)

#BALL
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.5#0.2#2
ball.dy = 0.5#0.2#2
static = True

pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(-2.5, 220)
pen.write("0      0",align="center", font=("Fixedsys", 60, "bold"))

pen2 = turtle.Turtle()
pen2.speed(0)
pen2.color("white")
pen2.penup()
pen2.hideturtle()
pen2.goto(0, 120)
pen2.write("PRESS ENTER TO START",align="center", font=("Fixedsys", 24, "bold"))



def update_score(sa,sb):
    pen.clear()
    pen.write("{}      {}".format(score_a,score_b),align="center", font=("Fixedsys", 60, "bold")) #Courier   

def paddle_a_up():
    y = paddle_a.ycor()
    if y <= 240:
        y += 20
        paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    if y >= -220:
        y -= 20
        paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    if y <= 240:
        y += 20
        paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    if y >= -220:
        y -= 20
        paddle_b.sety(y)

def play_sound():
    playsound("pong.mp3")

def init_playsoun():
    t = threading.Thread(target=play_sound)
    t.start()
    
def init_game():
    global static
    static = False
    pen2.clear()

def reset_screen():
    ball.goto(0, 0)
    ball.dx *= -1    
    pen2.write("PRESS ENTER TO START",align="center", font=("Fixedsys", 24, "bold"))
    paddle_a.goto(-350, 0)
    paddle_b.goto(350, 0)     
    
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")
wn.onkeypress(init_game, "Return")

while True:
    try:
        wn.update()

        #MOVE BALL
        if static == False:
            ball.setx(ball.xcor() + ball.dx)
            ball.sety(ball.ycor() + ball.dy)

        #BORDER
        if ball.ycor() > 290:
            ball.sety(290)
            ball.dy *= -1
            init_playsoun()

        if ball.ycor() < -290:
           ball.sety(-290)
           ball.dy *= -1
           init_playsoun()

        if ball.xcor() > 390:
            score_a += 1
            update_score(score_a, score_b)
            static = True
            time.sleep(1)
            reset_screen()

        if ball.xcor() < -390:
            score_b += 1
            update_score(score_a, score_b)
            static = True
            time.sleep(1)
            reset_screen()
            
        if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50):
            ball.setx(340)
            ball.dx *= -1
            init_playsoun()

        if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50):
            ball.setx(-340)
            ball.dx *= -1        
            init_playsoun()

    except:
        break
