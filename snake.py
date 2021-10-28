from turtle import *
import random
class Snake:

    def __init__(self) -> None:
        self.segs = []
        self.positions = [(-240, 0), (-260, 0), (-280, 0)]

        for pos in self.positions:
            self.create_snake(pos)
        self.head = self.segs[0]

    def create_snake(self,pos):
        new = Turtle()
        new.speed("fastest")
        new.color("white")
        new.penup()
        new.shape("square")
        new.goto(pos)
        self.segs.append(new)
    
    def extend(self):
        self.create_snake(self.segs[-1].position())
        
    def move_forward(self):
        for seg_num in range(len(self.segs) - 1, 0, -1):
            new_x = self.segs[seg_num - 1].xcor()
            new_y = self.segs[seg_num - 1].ycor()
            self.segs[seg_num].goto(new_x, new_y)

        self.segs[0].forward(20)

    def move_right(self):
        if self.segs[0].heading() == 90:
            self.segs[0].right(90)
        elif self.segs[0].heading() == 270:
            self.segs[0].left(90)
        
    def move_up(self):
        if self.segs[0].heading() == 180:
            self.segs[0].right(90)
        elif self.segs[0].heading() == 0:
            self.segs[0].left(90)

    def move_down(self):
        if self.segs[0].heading() == 0:
            self.segs[0].right(90)
        elif self.segs[0].heading() == 180:
            self.segs[0].left(90)

    def move_left(self):
        if self.segs[0].heading() == 270:
            self.segs[0].right(90)
        elif self.segs[0].heading() == 90:
            self.segs[0].left(90)
        
