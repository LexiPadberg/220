"""
Name: Lexi Padberg
vigeneere.py

Problem: write a program that uses the vigenere cipher

Certification of Authenticity: I certify that this assignment is entirely my own work
"""
from graphics import*

def main():
    width = 400
    height = 400
    win = GraphWin("Vigenere", width, height)

    message = "message to encode:"
    message1 = Entry(Point(250, 150), 20)
    message1.draw(win)

    inst = Text(Point(75,150), message)
    inst.draw(win)

    keyword = "enter keyword"
    key = Text(Point(75, 180), keyword)
    key.draw(win)
    keyword1 = Entry(Point(250, 180), 20)
    keyword1.draw(win)


    button = Rectangle(Point(160,210),Point(240, 250))
    encode = Text(Point(200, 230 ), "Encode")
    button.draw(win)
    encode.draw(win)
    win.getMouse()

    message1 = message1.getText()
    keyword1 = keyword1.getText()


    encrypted = code(message1, keyword1)
    button.undraw()
    encode.undraw()
    result = Text(Point(200, 230), "Resulting Message\n" + encrypted)
    result.draw(win)

    inst_pt = Point(200, 390)
    instructions = Text(inst_pt, "click again to quit")
    instructions.setFill("black")
    instructions.draw(win)

    win.getMouse()
    win.close()

def code(message, keyword):
    acc = ""
    message = message.upper()
    keyword = keyword.upper()
    message = message.replace(" ", "")
    keyword = keyword.replace(" ", "")
    for i in range(len(message)):
        m = ord(message[i]) - 65
        k = ord(keyword[i % len(keyword)]) - 65
        nc = m + k
        nc = nc % 26
        nc = chr(65 + nc)
        acc += nc
    return acc


if __name__ == '__main__':
    main()
