import turtle

FONT = ("Arial", 24, "normal")


class Scoreboard(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.score = 1
        self.color("black")
        self.penup()
        self.hideturtle()
        self.goto(-280, 260)
        self.update_scoreboard()
    
    def starting_screen(self):
        self.update_scoreboard()
        self.goto(0, 0)
        self.write("Press ENTER to start", align="center", font=FONT)
        
    def update_scoreboard(self):
        self.clear()
        self.write(f"Level: {self.score}", align="left", font=FONT)
    
    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
    
    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER\nFinal Level: {self.score}\n", align="center", font=FONT)
        self.write("Press Space to restart", align="center", font="arial 12")
        
    def reset(self):
        self.score = 1
        self.goto(-280, 260)
        self.update_scoreboard()
        
    def victory(self):
        if self.score > 5:
            self.goto(0, 0)
            self.clear()
            self.write("VICTORY\n", align="center", font=FONT)
            self.write("Press Space to restart", align="center", font="arial 12")
        
        
