from turtle import Turtle
import time

FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.level = 1
        self.penup()
        self.hideturtle()
        self.goto(0, 280)
        self.write(f"Level: {self.level} Score: {self.score}", FONT)

    def add_score(self):
        self.clear()
        self.score += 100
        self.goto(0, 280)
        self.write(f"Level: {self.level} Score: {self.score}", FONT)

    def gameover(self):
        self.clear()
        self.goto(0,0)
        self.write(f"GAME OVER\n YOU LOST!!!\n Score: {self.score}", FONT)

    def next_level(self):
        self.level += 1
        self.add_score()
        self.clear()
        self.goto(0, 280)
        self.write(f"Level :{self.level} Score: {self.score}", FONT)

