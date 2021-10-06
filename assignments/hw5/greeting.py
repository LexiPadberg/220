"""
Name: Lexi Padberg
greeting.py

Problem: write a program that displays a heart

Certification of Authenticity: I certify that this assignment is entirely my own work
"""


from graphics import GraphWin, Point, Circle, Polygon, Text, Image, time


def main():
    width = 400
    height = 400
    win = GraphWin("greeting", width, height)
    win.setBackground("LightCoral")

    point1 = Point(240, 100)
    circle = Circle(point1, 53)
    circle.setFill("cyan")
    circle.setOutline("cyan")
    circle.draw(win)

    point1 = Point(140, 100)
    circle = Circle(point1, 53)
    circle.setFill("cyan")
    circle.setOutline("cyan")
    circle.draw(win)

    point1 = Point(89.5, 120)
    point1.draw(win)
    point2 = Point(290, 120)
    point1.setFill("LightCoral")
    point2.draw(win)
    point2.setFill("LightCoral")
    point3 = Point(197, 260)
    point3.setFill("LightCoral")
    point3.draw(win)
    tri = Polygon(point1, point2, point3)
    tri.setOutline("cyan")
    tri.setFill("cyan")
    tri.draw(win)

    message = Text(Point(200, 350), "Happy Valentines Day!")
    message.setFace("arial")
    message.setSize(27)
    message.setStyle("bold")
    message.setFill("DeepPink")
    message.draw(win)
    for _ in range(46):
        message.move(2, 0)
        time.sleep(.02)

    for _ in range(46):
        message.move(-4, 0)
        time.sleep(.02)

    for _ in range(46):
        message.move(2, 0)
        time.sleep(.02)

    arrow = 'arrow_2.gif'
    arrow_image = Image(Point(0, 200), arrow)

    arrow_image.draw(win)
    for _ in range(46):
        arrow_image.move(40, -20)
        time.sleep(.1)

    inst_pt = Point(200, 390)
    instructions = Text(inst_pt, "click again to quit")
    instructions.setFill("pink")
    instructions.draw(win)

    win.getMouse()
    win.close()


if __name__ == '__main__':
    main()
