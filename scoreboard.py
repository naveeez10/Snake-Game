from turtle import *

class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(-10,270)
        self.write(f"Score: {self.score}",align="center",font=("Arial",20,"normal"))
        self.hideturtle()

    def ref(self):
        self.clear()
        self.write(f"Score: {self.score}",align="center",font=("Arial",20,"normal"))