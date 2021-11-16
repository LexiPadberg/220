"""
Name: Lexi Padberg
three_door_game.py

Problem: this problem creates a list of objects from a user_defined class

Certification of Authenticity: I certify that this assignment is entirely my own work
"""

from random import randint
from graphics import GraphWin, Point, Rectangle, Text
from button import Button


def main():
    width, height = 400, 400
    win = GraphWin("Three Doors", width, height)

    button1 = Button(Rectangle(Point(60,210),Point(140, 250)), "Door 1")
    button1.draw(win)

    button2 = Button(Rectangle(Point(160, 210), Point(240, 250)), "Door 2")
    button2.draw(win)

    button3 = Button(Rectangle(Point(260, 210), Point(340, 250)), "Door 3")
    button3.draw(win)

    message = Text(Point(200, 100), "I have a secret door")
    message.draw(win)

    message2 = Text(Point(200, 350), "click to chose my door")
    message2.draw(win)


    door_list = [button1, button2, button3]
    secret_door = door_list[randint(0, 2)]
    click = win.getMouse()
    if secret_door.is_clicked(click):
        secret_door.color_button("Green")
        winner = Text(Point(200,100), "you win!")
        message.undraw()
        message2.undraw()
        winner.draw(win)
        close = Text(Point(200, 350), "click to close")
        close.draw(win)
    else:
        if button1.is_clicked(click):
            button1.color_button("Red")
            lose = Text(Point(200,100), "You lose!")
            message.undraw()
            message2.undraw()
            close = Text(Point(200, 350), "click to close")
            close.draw(win)
            lose.draw(win)
        elif button2.is_clicked(click):
            button2.color_button("Red")
            lose = Text(Point(200, 100), "You lose!")
            message.undraw()
            message2.undraw()
            close = Text(Point(200, 350), "click to close")
            close.draw(win)
            lose.draw(win)
        elif button3.is_clicked(click):
            button3.color_button("Red")
            lose = Text(Point(200, 100), "You lose!")
            message.undraw()
            close = Text(Point(200, 350), "click to close")
            close.draw(win)
            message2.undraw()
            lose.draw(win)
            print("button 3")

    win.getMouse()
    win.close()


if __name__ == '__main__':
    main()
