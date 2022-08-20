import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 35
MOVE_INCREMENT = 10
import time


class CarManager:
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_cars(self):
        random_y = random.randint(-260, 260)
        car = Turtle()
        car.shape("square")
        car.shapesize(1, 2)
        car.color(random.choice(COLORS))
        car.penup()
        car.setheading(180)
        car.goto(300, random_y)
        self.all_cars.append(car)

    def move_car(self):
        for car in self.all_cars:
            car.forward(STARTING_MOVE_DISTANCE)

    def increase_speed(self):
        self.car_speed *= 3
        for car in self.all_cars:
            print(self.car_speed)
            car.forward(self.car_speed)