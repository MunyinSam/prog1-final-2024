import turtle
import ball
import random

num_balls = 5
turtle.speed(0)
turtle.tracer(0)
turtle.hideturtle()
canvas_width = turtle.screensize()[0]
canvas_height = turtle.screensize()[1]
print(canvas_width, canvas_height)
ball_radius = 0.05 * canvas_width
turtle.colormode(255)
xpos = []
ypos = []
vx = []
vy = []
ball_color = []

class DrawNumber:
    def __init__(self):
        pass

    def initialize(self, my_turtle, color):

        turtle.speed(0)
        turtle.tracer(0)
        turtle.hideturtle()
        turtle.colormode(255)

        my_turtle.color(color)
        my_turtle.penup()
        my_turtle.setheading(0)
        my_turtle.goto(0, 0)
        my_turtle.pensize(10)

    def draw(self, my_turtle, digit):

        if digit == 0:
            my_turtle.goto(-50, 100)
            my_turtle.pendown()
            my_turtle.forward(100)
            my_turtle.right(90)
            my_turtle.forward(100)
            my_turtle.forward(100)
            my_turtle.right(90)
            my_turtle.forward(100)
            my_turtle.right(90)
            my_turtle.forward(100)
            my_turtle.forward(100)
            my_turtle.right(90)
            my_turtle.penup()

        if digit == 1:
            my_turtle.goto(50, 100)
            my_turtle.pendown()
            my_turtle.right(90)
            my_turtle.forward(100)
            my_turtle.forward(100)
            my_turtle.left(90)
            my_turtle.penup()

        if digit == 2:
            my_turtle.goto(-50, 100)
            my_turtle.pendown()
            my_turtle.forward(100)
            my_turtle.right(90)
            my_turtle.forward(100)
            my_turtle.right(90)
            my_turtle.forward(100)
            my_turtle.left(90)
            my_turtle.forward(100)
            my_turtle.left(90)
            my_turtle.forward(100)
            my_turtle.penup()

        if digit == 3:
            my_turtle.goto(-50, 100)
            my_turtle.pendown()
            my_turtle.forward(100)
            my_turtle.right(90)
            my_turtle.forward(100)
            my_turtle.right(90)
            my_turtle.forward(100)
            my_turtle.forward(-100)
            my_turtle.left(90)
            my_turtle.forward(100)
            my_turtle.right(90)
            my_turtle.forward(100)
            my_turtle.left(90)
            my_turtle.left(90)
            my_turtle.penup()

        if digit == 4:
            my_turtle.goto(-50, 100)
            my_turtle.pendown()
            my_turtle.right(90)
            my_turtle.forward(100)
            my_turtle.left(90)
            my_turtle.forward(100)
            my_turtle.left(90)
            my_turtle.forward(100)
            my_turtle.forward(-100)
            my_turtle.forward(-100)
            my_turtle.right(90)
            my_turtle.penup()

        if digit == 5:
            my_turtle.goto(-50, 100)
            my_turtle.pendown()
            my_turtle.forward(100)
            my_turtle.forward(-100)
            my_turtle.right(90)
            my_turtle.forward(100)
            my_turtle.left(90)
            my_turtle.forward(100)
            my_turtle.right(90)
            my_turtle.forward(100)
            my_turtle.right(90)
            my_turtle.forward(100)
            my_turtle.left(90)
            my_turtle.left(90)
            my_turtle.penup()

        if digit == 6:
            self.draw(my_turtle, 5)
            my_turtle.goto(-50, 0)
            my_turtle.pendown()
            my_turtle.right(90)
            my_turtle.forward(100)
            my_turtle.left(90)
            my_turtle.penup()
        
        if digit == 7:
            my_turtle.goto(-50, 100)
            my_turtle.pendown()
            my_turtle.forward(100)
            my_turtle.forward(-100)
            self.draw(my_turtle, 1)

        if digit == 8:
            self.draw(my_turtle, 0)
            my_turtle.goto(-50, 0)
            my_turtle.pendown()
            my_turtle.forward(100)
            my_turtle.penup()

        if digit == 9:
            self.draw(my_turtle, 5)
            my_turtle.goto(50, 100)
            my_turtle.pendown()
            my_turtle.right(90)
            my_turtle.forward(100)
            my_turtle.left(90)
            my_turtle.penup()

    def clear(self, my_turtle):
        my_turtle.clear()

    def my_delay(self, dt):
        import time
        start =  time.time()
        while time.time() - start < dt:
            pass

class BallScene:
    def __init__(self, xpos, ypos, vx, vy, ball_color, dt, canvas_width, canvas_height, ball_radius):
        self.xpos = xpos
        self.ypos = ypos
        self.vx = vx
        self.vy = vy
        self.ball_color = ball_color
        self.dt = dt
        self.canvas_width = canvas_width
        self.canvas_height = canvas_height
        self.ball_radius = ball_radius

    def draw_border(self):
        turtle.penup()
        turtle.goto(-self.canvas_width, -self.canvas_height)
        turtle.pensize(10)
        turtle.pendown()
        turtle.color((0, 0, 0))
        for i in range(2):
            turtle.forward(2*canvas_width)
            turtle.left(90)
            turtle.forward(2*canvas_height)
            turtle.left(90)
    
    def draw_ball(self, color, size, x, y):
        # draw a circle of radius equals to size at x, y coordinates and paint it with color
        turtle.penup()
        turtle.color(color)
        turtle.fillcolor(color)
        turtle.goto(x,y-size)
        turtle.pendown()
        turtle.begin_fill()
        turtle.circle(size)
        turtle.end_fill()

    def move_ball(self, i, xpos, ypos, vx, vy, dt):
        # update the x, y coordinates of ball i with velocity in the x (vx) and y (vy) components
        xpos[i] += vx[i]*dt
        ypos[i] += vy[i]*dt

    def update_ball_velocity(self, i, xpos, ypos, vx, vy, canvas_width, canvas_height, ball_radius):
        # if the ball hits the side walls, reverse the vx velocity
        if abs(xpos[i]) > (canvas_width - ball_radius):
            vx[i] = -vx[i]

        # if the ball hits the ceiling or the floor, reverse the vy velocity
        if abs(ypos[i]) > (canvas_height - ball_radius):
            vy[i] = -vy[i]
    
    def run(self):
        while (True):

            Tom = turtle.Turtle()
            numbers = DrawNumber()
            tom_color = (255, 0, 0)
            numbers.initialize(Tom, tom_color)
            for i in range(0, 10):
                numbers.clear(Tom)
                numbers.draw(Tom, i)
                numbers.my_delay(self.dt)
                turtle.update()

                turtle.clear()
                self.draw_border()
                for i in range(num_balls):
                    self.draw_ball(self.ball_color[i], self.ball_radius, self.xpos[i], self.ypos[i])
                    self.move_ball(i, self.xpos, self.ypos, self.vx, self.vy, self.dt)
                    self.update_ball_velocity(i, self.xpos, self.ypos
                                            , self.vx, self.vy
                                            , self.canvas_width, self.canvas_height
                                            , self.ball_radius)
                    turtle.update()
                numbers.clear(Tom)

    
for i in range(num_balls):
    xpos.append(random.uniform(-1*canvas_width + ball_radius, canvas_width - ball_radius))
    ypos.append(random.uniform(-1*canvas_height + ball_radius, canvas_height - ball_radius))
    vx.append(10*random.uniform(-1.0, 1.0))
    vy.append(10*random.uniform(-1.0, 1.0))
    ball_color.append((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))

dt = 0.2
ball = BallScene(xpos, ypos, vx, vy, ball_color, dt, canvas_width, canvas_height, ball_radius)
ball.run()