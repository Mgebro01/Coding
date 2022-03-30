import turtle as t
PlayerAscore=0
PlayerBscore=0

window=t.Screen()
window.title('ping-pong game')
window.bgcolor('green')
window.setup(width=800,height=600)
window.tracer(0)

#creating left paddle
leftpaddle=t.Turtle()
leftpaddle.speed(0)
leftpaddle.shape('square')
leftpaddle.color('white')
leftpaddle.shapesize(stretch_wid=5,stretch_len=1)
leftpaddle.penup()
leftpaddle.goto(-350.0)

#right paddle
rightpaddle=t.Turtle()
rightpaddle.speed(0)
rightpaddle.shape('square')
rightpaddle.color('white')
rightpaddle.shapesize(stretch_wid=5,stretch_len=1)
rightpaddle.penup()
rightpaddle.goto(350.0)

#ball

ball=t.Turtle()
ball.speed(0)
ball.shape('circle')
ball.color('red')
ball.penup()
ball.goto(5,5)
ballxdrection=0.2
ballydrection=0.2

#pen scoreboard update

pen=t.Turtle
pen.speed(0)
pen.color('blue')
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write('score', align='center', font=('arial',24,'normal'))



#moving leftpaddle

def leftpaddleup():
    y=leftpaddle.ycor()
    y=y+90
    leftpaddle.sety(y)


def leftpaddledown():
    y=leftpaddle.ycor()
    y=y-90
    leftpaddle.sety(y)

#moving rightpaddle

def rightpaddleup():
    y=rightpaddle.ycor()
    y=y+90
    rightpaddle.sety(y)


def rightpaddledown():
    y = rightpaddle.ycor()
    y = y-90
    rightpaddle.sety(y)

# Assign keys to play

window.listen()
window.onkeypress(leftpaddleup, 'w')
window.onkeypress(leftpaddledown, 's')
window.onkeypress(rightpaddleup, 'Up')
window.onkeypress(rightpaddledown, 'Down')

while True:
    window.update()

#Moving the ball
ball.setx(ball.xcor()+ballxdirection)
ball.sety(ball.ycor()+ballydirection)

#settingup border
    if ball.ycor()>290:
        ball.sety(290)
        ballydirection=ballxdirection*-1
    if ball.ycor()>-290:
        ball.sety(-290)
        ballydirection=ballxdirection*-1

    if ball.xcor()>390:
        ball.goto(0,0)
        ballxdirection=ballxdirection
        PlayerAscore=PlayerAscore+1
        pen.clear()
        pen.write("Player A:{}    Player B:{}".format(PlayerAscore,PlayerBscore),align='center',font=('Arial',24,'normal'))

    if(ball.xcor())<-390:
        ball.goto(0,0)
        ballxdirection=ballxdirection*-1
        PlayerBscore=PlayerBscore+1
        pen.clear()
        pen.write("Player A:{}    Player B:{}".format(PlayerAscore,PlayerBscore),align='center',font=('Arial',24,'normal'))


    #handing the collisions

    if (ball.xcor()>340)and(ball.xcor()<350)and(ball.ycor()<rightpaddle.ycor()+40 and ball.ycor()>rightpaddle.ycor()-40)
        ball.setx(340)
        ballxdirection=ballxdirection*-1

    if (ball.xcor()>-340)and(ball.xcor()<-350)and(ball.ycor() <leftpaddle.ycor()+40 and ball.ycor()>leftpaddle.ycor()-40)
        ball.setx(-340)
        ballxdirection=ballxdirection*-1
