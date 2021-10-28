from turtle import *
import random
from random import randint
colors = ["red","green","yellow","blue","orange","purple"]
class Food(Turtle):
    def __init__(self) -> None:
       super().__init__()

       self.shape("circle")
       self.penup()
       self.shapesize(stretch_len=0.5,stretch_wid=0.5)
       self.color("blue")
       self.speed("fastest")
       self.goto((randint(-280,280),randint(-280,280)))
    
    def refresh(self):
        self.clear()
        self.color(random.choice(colors))
        self.goto((randint(-280,280),randint(-280,280)))

       
