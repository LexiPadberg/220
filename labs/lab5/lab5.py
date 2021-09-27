"""
Name: <Lexi Padberg>
<lab5>.py
"""

from graphics import *
import math


def target():
    win_width = 500
    win_height = 500
    win = GraphWin("Archery Target", win_width, win_height)

    # Add code here to get the dimensions and draw the target

    # Wait for another click to exit
    win.getMouse()
    win.close()


def triangle():
    win_width = 500
    win_height = 500
    win = GraphWin("Draw a Triangle", win_width, win_height)

    message = Text(Point(200, 10), "Click on three points to create a triangle")
    message.draw(win)

    # Add code here to accept the mouse clicks, draw the triangle.
    point1 = win.getMouse()
    point1.draw(win)
    point2 = win.getMouse()
    point2.draw(win)
    point3 = win.getMouse()
    point3.draw(win)
    l1 = math.sqrt((point2.getX()-point1.getX())**2 + (point2.getY()-point1.getY())**2)
    l2 = math.sqrt((point3.getX()-point1.getX())**2 +(point3.getY()-point1.getY())**2)
    l3 = math.sqrt((point3.getX()-point2.getX())**2 +(point3.getY()-point2.getY())**2)
    perimeter = l1 + l2 + l3
    s = (l1 + l2 + l3) / 2
    area = math.sqrt(s*(s-l1)*(s-l2)*(s-l3))

    message = Text(Point(150, 300), "the perimeter is: " + str(perimeter))
    message.draw(win)
    message = Text(Point(400, 200), "the area is: " + str(area))
    message.draw(win)
    message = Text(Point(300, 100), "Click to end the program")
    message.draw(win)

    tri = Polygon(point1, point2, point3)
    tri.setFill("red")
    tri.draw(win)

    # and display its area in the graphics window.

    # Wait for another click to exit
    win.getMouse()
    win.close()


def color_shape():
    '''Create code to allow a user to color a shape by entering rgb amounts'''

    # create window
    win_width = 400
    win_height = 400
    win = GraphWin("Color Shape", win_width, win_height)
    win.setBackground("white")

    # create text instructions
    msg = "Enter color values between 0 - 255\nClick window to color shape"
    inst = Text(Point(win_width / 2, win_height - 20), msg)
    inst.draw(win)

    # create circle in window's center
    shape = Circle(Point(win_width / 2, win_height / 2 - 30), 50)
    shape.draw(win)

    # redTexPt is 50 pixels to the left and forty pixels down from center
    red_text_pt = Point(win_width / 2 - 50, win_height / 2 + 40)
    red_text = Text(red_text_pt, "Red: ")
    red_text.setTextColor("red")

    # green_text_pt is 30 pixels down from red
    green_text_pt = red_text_pt.clone()
    green_text_pt.move(0, 30)
    green_text = Text(green_text_pt, "Green: ")
    green_text.setTextColor("green")

    # blue_text_pt is 60 pixels down from red
    blue_text_pt = red_text_pt.clone()
    blue_text_pt.move(0, 60)
    blue_text = Text(blue_text_pt, "Blue: ")
    blue_text.setTextColor("blue")

    # display rgb text


    red_box = Entry(Point(300, 300), 5)
    red_box.draw(win)
    green_box = Entry(Point(300, 100), 5)
    green_box.draw(win)
    blue_box = Entry(Point(300, 200), 5)
    blue_box.draw(win)
    for i in range(5):
        win.getMouse()
        red_text = int(red_box.getText())
        green_text = int(green_box.getText())
        blue_text = int(blue_box.getText())
        color = color_rgb(red_text, green_text, blue_text)
        shape.setFill(color)

    # Wait for another click to exit
    win.getMouse()
    win.close()

def main():
    # target()
    triangle()
    color_shape()
pass


main()
def process_string():
    string = input("enter a word with at least 5 letters: ")
    first = string[0]
    print(first)
    last = string[-1]
    print(last)
    first_half = string[1:5]
    print(first_half)
    first_last = string[0] + string[-1]
    print(first_last)
    mult_10 = string[0:3] *10
    print(mult_10)
    for i in string:
        print(i)
    length = len(string)
    print(length)




def process_list():
    pt = Point(5, 10)
    values = [5, "hi", 2.5, "there", pt, "7.2"]
    x = values[1] + values[3]
    print(x)
    x = values[0] + values[2]
    print(x)
    x = values[1] * 5
    print(x)
    x = values[2:5]
    print(x)
    x = [values[2], values[3], values[0]]
    print(x)
    x = [values[2], values[0], float(values[5])]
    print(x)
    x = values[0] + values[2] + float(values[5])
    print(x)
    x = len(values)
    print(x)

def another_series():
    n = eval(input("enter number of terms: "))
    acc = 0
    for i in range(n):
        y = 2 + (2 * (i % 3))
        acc = y + acc
        print(y, end=" ")
    print()
    print("sum = ", acc)


def target():
    width = 400
    height = 400
    win = GraphWin("Lab r circle", width, height)

#width = height = number = z
# radius of white circle = 1/2 * z
# each width is the radius of the yellow circle
# draw white circle first
#point1 = (height/2, width,2)
#CircleA = (point1, r )


if __name__ == '__main__':
    main()
