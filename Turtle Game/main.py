import time
from turtle import Screen
from player import *
from car_manager import *
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("SCHILDKROETE")
screen.tracer(0)

# Initialisierung
player = Player()
scoreboard = Scoreboard()
starting_screen = scoreboard.starting_screen()
game_start = False

# Car Creation
car_manager = CarManager(scoreboard)
def generate_cars():
    if game_start:
        car_manager.create_car()
        if car_manager.level == 1:
            screen.ontimer(generate_cars, 800)
        elif car_manager.level == LEVEL_BOTH_SIDES:
            screen.ontimer(generate_cars, 400)
        elif car_manager.level == LEVEL_MORE_SPEED:
            screen.ontimer(generate_cars, 400)
        elif car_manager.level == LEVEL_MORE_CARS:
            screen.ontimer(generate_cars, 200)
        elif car_manager.level == LEVEL_FINAL:
            screen.ontimer(generate_cars, 120)

# Start
def start():
    global game_start
    if not game_start:
        game_start = True
        player.reset_position()
        player.start()
        car_manager.reset()
        scoreboard.reset()
        generate_cars()
    
# Reset
def reset():
    player.reset_position()
    player.start()
    car_manager.reset()
    scoreboard.reset()
    scoreboard.starting_screen()

# Game Over
def game_over():
    global game_start
    if car_manager.collision(player):
        scoreboard.game_over()
        player.stop()
        game_start = False

# Victory  
def victory():
    global game_start
    if car_manager.level > LEVEL_FINAL:
        scoreboard.victory()
        player.stop()
        game_start = False

#Tastenbelegung
screen.listen()
screen.onkey(start, "Return")
screen.onkey(player.move_up, "Up")
screen.onkey(player.move_down, "Down")
screen.onkey(player.move_left, "Left")
screen.onkey(player.move_right, "Right")
screen.onkey(reset, "space")
screen.onkey(screen.bye, "Escape")

# Hauptschleife
while True:
    screen.update()
    time.sleep(0.1)
    
    car_manager.move_car()
    
    # Level Up
    if player.ycor() > FINISH_LINE_Y:
        player.reset_position()
        car_manager.level_up()
        scoreboard.increase_score()
        
    # Kollision
    if car_manager.collision(player):
        game_over()
    
    # Victory
    if scoreboard.score > LEVEL_FINAL:
        scoreboard.victory()
        victory()

    
    


