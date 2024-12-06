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
    
for i in range(num_balls):
    xpos.append(random.uniform(-1*canvas_width + ball_radius, canvas_width - ball_radius))
    ypos.append(random.uniform(-1*canvas_height + ball_radius, canvas_height - ball_radius))
    vx.append(10*random.uniform(-1.0, 1.0))
    vy.append(10*random.uniform(-1.0, 1.0))
    ball_color.append((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))

dt = 0.2
ball = BallScene(xpos, ypos, vx, vy, ball_color, dt, canvas_width, canvas_height, ball_radius)
ball.run()