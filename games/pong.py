import turtle

wn = turtle.Screen()
wn.title("Pong by Andre Filho")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)


# Score
score_a = 0
score_b = 0


#Jogador A
play_a = turtle.Turtle()
play_a.speed(0)
play_a.shape("square")
play_a.color("white")
play_a.shapesize(stretch_wid=5, stretch_len=1)
play_a.penup()
play_a.goto(-350, 0)

#Jogador B
play_b = turtle.Turtle()
play_b.speed(0)
play_b.shape("square")
play_b.color("white")
play_b.shapesize(stretch_wid=5, stretch_len=1)
play_b.penup()
play_b.goto(350, 0)

#Ball
ball = turtle.Turtle()
ball.speed(1)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.5
ball.dy = 0.5


# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
#pen.write("Player A: 0 Player B: 0", align="center", font=("Courier", 24, "normal"))


#Function Jogador A
def play_a_up():
	y = play_a.ycor()
	y += 20
	play_a.sety(y)


def play_a_down():
	y = play_a.ycor()
	y -= 20
	play_a.sety(y)


#Function Jogador B
def play_b_up():
	y = play_b.ycor()
	y += 20
	play_b.sety(y)

def play_b_down():
	y = play_b.ycor()
	y -= 20
	play_b.sety(y)


wn.listen()

wn.onkeypress(play_a_up, "w")
wn.onkeypress(play_a_down, "s")

wn.onkeypress(play_b_up, "Up")
wn.onkeypress(play_b_down, "Down")



#Main Loop
while True:
	wn.update()

	# Move the ball
	ball.setx(ball.xcor() + ball.dx)
	ball.sety(ball.ycor() + ball.dy)

	# Border Checking
	if ball.ycor() > 290:
		ball.sety(290)
		ball.dy *= -1

	if ball.ycor() < -290:
		ball.sety(-290)
		ball.dy *= -1

	if ball.xcor() > 390:
		ball.goto(0, 0)
		ball.dx *= -1
		score_a += 1

	if ball.xcor() < -390:
		ball.goto(0, 0)
		ball.dx *= -1
		score_b += 1

	pen.clear()
	pen.write(f"Player A: {score_a} Player B: {score_b}", align="center", font=("Courier", 24, "normal"))


	# PLay and ball collisions
	if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < play_b.ycor() + 40 and ball.ycor() > play_b.ycor() -40):
		ball.setx(340)
		ball.dx *= -1

	if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < play_a.ycor() + 40 and ball.ycor() > play_a.ycor() -40):
		ball.setx(-340)
		ball.dx *= -1
