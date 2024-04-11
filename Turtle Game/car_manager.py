import random
import turtle

COLORS = ["red", "orange", "yellow", "blue", "pink"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5
LEVEL_BOTH_SIDES = 2
LEVEL_MORE_SPEED = 3
LEVEL_MORE_CARS = 4
LEVEL_FINAL = 5


class CarManager:
    def __init__(self, scoreboard):
        self.cars = []
        self.car_speed = STARTING_MOVE_DISTANCE
        self.level = 1
        self.scoreboard = scoreboard
        
    def create_car(self):
        new_car = turtle.Turtle("square")
        new_car.shapesize(stretch_wid=1, stretch_len=2)
        new_car.penup()
        new_car.color(random.choice(COLORS))
        new_car.pencolor("black")
        if self.level >= LEVEL_BOTH_SIDES:
            direction = random.choice(["left", "right"])
        else:
            direction = "right"

        if direction == "right":
            new_car.goto(300, random.randint(-250, 250))
            new_car.setheading(0)
        else:
            new_car.goto(-300, random.randint(-250, 250))
            new_car.setheading(180)

        self.cars.append(new_car)
            
    def move_car(self):
        for car in self.cars:
            car.backward(self.car_speed)
            
    def level_up(self):
        self.level += 1
        if self.level == LEVEL_MORE_SPEED:
            self.car_speed += MOVE_INCREMENT
        elif self.level == LEVEL_FINAL:
            self.car_speed += MOVE_INCREMENT
        elif self.level > LEVEL_FINAL:
            self.scoreboard.victory()
        
    def collision(self, player):
        for car in self.cars:
            if car.distance(player) < 20:
                return True
        return False
    
    def reset(self):
        for car in self.cars:
            car.hideturtle()
        self.cars.clear()
        self.car_speed = STARTING_MOVE_DISTANCE
        self.level = 1
