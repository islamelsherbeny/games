import turtle

wind = turtle.Screen()
wind.title("ping pong by islam")
wind.bgcolor("#333")
wind.setup(width=800, height=600)
wind.tracer(0)

score1 = 0
score2 = 0
score = turtle.Turtle()
score.speed(0)
score.color("white")
score.penup()
score.hideturtle()
score.goto(0, 260)
score.write("player 1:0 player2:0", align="center",
            font=("courier", 24, "normal"))

mad1 = turtle.Turtle()
mad1.speed(0)
mad1.shape("square")
mad1.color("blue")
mad1.shapesize(stretch_wid=5, stretch_len=1)
mad1.penup()
mad1.goto(-350, 0)

mad2 = turtle.Turtle()
mad2.speed(0)
mad2.shape("square")
mad2.color("red")
mad2.shapesize(stretch_wid=5, stretch_len=1)
mad2.penup()
mad2.goto(350, 0)

ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = .25
ball.dy = .35


def mad1_up():
    y = mad1.ycor()
    if y < 260:
        y += 20
        mad1.sety(y)


def mad1_down():
    y = mad1.ycor()
    if y > -260:
        y -= 20
        mad1.sety(y)


def mad2_up():
    y = mad2.ycor()
    if y < 260:
        y += 20
        mad2.sety(y)


def mad2_down():
    y = mad2.ycor()
    if y > -260:
        y -= 20
        mad2.sety(y)


wind.listen()
wind.onkeypress(mad1_up, "w")
wind.onkeypress(mad1_down, "s")
wind.onkeypress(mad2_up, "Up")
wind.onkeypress(mad2_down, "Down")

while True:
    wind.update()
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score1 += 1
        score.clear()
        score.write("player 1:{} player2:{}".format(score1, score2), align="center",
                    font=("courier", 24, "normal"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score2 += 1
        score.clear()
        score.write("player 1:{} player2:{}".format(score1, score2), align="center",
                    font=("courier", 24, "normal"))

    if (ball.xcor() > 340 and ball.xcor() < 350 and ball.ycor() < mad2.ycor() + 40 and ball.ycor() > mad2.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1

    if (ball.xcor() < -340 and ball.xcor() > -350 and ball.ycor() < mad1.ycor() + 40 and ball.ycor() > mad1.ycor() - 40):

        ball.setx(-340)
        ball.dx *= -1
