#########  using OOP Write another program to draw n number of sqares at random locations. The squares are to have arbitrary colors also
import turtle
from random import randint


class Squares:
    def __init__(self, turtle):
        self.t = turtle

    def random_squares(self):
        r = randint(0, 255)
        g = randint(0, 255)
        b = randint(0, 255)
        colors = (r / 255, g / 255, b / 255)
        x = randint(-200, 200)
        y = randint(-200, 200)

        self.t.up()
        self.t.goto(x, y)
        self.t.down()

        self.t.color(colors)
        self.t.begin_fill()
        for _ in range(4):
            self.t.forward(100)
            self.t.left(90)
        self.t.end_fill()


def main():
    t = turtle.Turtle()
    square = Squares(t)
    for _ in range(10):
        square.random_squares()
    turtle.done()


if __name__ == "__main__":
    main()


import turtle
from random import randint


class Square:
    def __init__(self, turtle):
        self.t = turtle

    def draw_random_square(self):
        r = randint(0, 255)
        g = randint(0, 255)
        b = randint(0, 255)
        color = (r / 255, g / 255, b / 255)

        x = randint(-200, 200)
        y = randint(-200, 200)

        self.t.penup()
        self.t.goto(x, y)
        self.t.pendown()

        self.t.color(color)
        self.t.begin_fill()
        for _ in range(4):
            self.t.forward(100)
            self.t.right(90)
        self.t.end_fill()


def main():
    t = turtle.Turtle()
    square = Square(t)

    for _ in range(10):
        square.draw_random_square()

    turtle.done()


if __name__ == "__main__":
    main()