import turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.color("green")
        self.pencolor("black")
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.goto(STARTING_POSITION)
        self.setheading(90)
        self.is_moving = True
        
    def move_up(self):
        if self.is_moving:
            self.goto(self.xcor(), self.ycor() + MOVE_DISTANCE)
    
    def move_down(self):
        if self.is_moving and self.ycor() > -280:
            self.goto(self.xcor(), self.ycor() - MOVE_DISTANCE)
    
    def move_left(self):
        if self.is_moving and self.xcor() > -290:
            self.goto(self.xcor() - MOVE_DISTANCE, self.ycor())
    
    def move_right(self):
        if self.is_moving and self.xcor() < 280:
            self.goto(self.xcor() + MOVE_DISTANCE, self.ycor())

            
    def stop(self):
        self.is_moving = False
        
    def start(self):
        self.is_moving = True
        
    def reset_position(self):
        self.goto(STARTING_POSITION)  
    
        
