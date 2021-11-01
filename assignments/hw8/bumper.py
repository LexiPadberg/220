"""
Name: Lexi Padberg
bumper.py

Problem: write a program that moves two balls

Certification of Authenticity: I certify that this assignment is entirely my own work
"""
import math
import time
from random import randint
from graphics import GraphWin, color_rgb, Circle, Point


def get_random(move_amount):
    return randint(-move_amount, move_amount)


def get_random_color():
    return color_rgb(randint(0, 255), randint(0, 255), randint(0, 255))


def main():
    result = get_random(10)
    print(result)
    win = GraphWin("bumper", 400, 400)
    win.setBackground("LightCoral")

    point1 = Point(randint(30, 370), randint(30,370))
    point2 = Point(randint(30, 370), randint(30, 370))
    ball = Circle(point1, 30)
    ball.setFill(get_random_color())
    ball.draw(win)
    ball2 = Circle(point2, 30)
    ball2.setFill(get_random_color())
    ball2.draw(win)

    c1x = get_random(10)
    c1y = get_random(10)
    c2x = get_random(10)
    c2y = get_random(10)

    while not win.checkMouse():
        ball.move(c1x, c1y)
        ball2.move(c2x, c2y)
        if hit_vertical(ball,win):
            c1x = -c1x
        if hit_vertical(ball2, win):
            c2x = -c2x
        if hit_horizontal(ball, win):
            c1y = -c1y
        if hit_horizontal(ball2, win):
            c2y = -c2y
        if did_collide(ball,ball2):
            c1x = -c1x
            c2x = -c2x
            c1y = -c1y
            c2y = -c2y

        time.sleep(.1)

    win.getMouse()
    win.close()


def did_collide(ball, ball2):
    distance = math.sqrt((ball.getCenter().getX() - ball2.getCenter().getX()) ** 2
                   + (ball.getCenter().getY() - ball2.getCenter().getY()) ** 2)
    totalradius = ball.getRadius() + ball2.getRadius()
    if distance <= totalradius:
        return True
    return False


def hit_vertical(ball, win):
    if ball.getCenter().getX() + ball.getRadius() >= win.getWidth() or \
            (ball.getCenter().getX() - ball.getRadius()) <= 0:
        return True
    return False


def hit_horizontal(ball, win):
    if ball.getCenter().getY() + ball.getRadius() >= win.getHeight() or \
            (ball.getCenter().getY() - ball.getRadius()) <= 0:
        return True
    return False


if __name__ == '__main__':
    main()
