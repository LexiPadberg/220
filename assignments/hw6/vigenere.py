"""
Name: Lexi Padberg
greeting.py

Problem: write a program that displays a heart

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



    #   keyword1 = str(keyword1)
    message1 = str(message1)
    for ch in message1:
        message1 = message1.replace(" ", "")
        message1 = message1.upper()
        print(ord(ch), end=" ")



    result = encode.replace()
    result.getMouse()


    inst_pt = Point(200, 390)
    instructions = Text(inst_pt, "click again to quit")
    instructions.setFill("black")
    instructions.draw(win)

    win.getMouse()
    win.close()




def encrypt():
    message = input("please enter the message to encode:")
    message = message.replace(" ", "")
    message = message.upper()
    print(message)
 #   key = input("enter keyboard")
    for character in message:
      x = (ord(message))
      print(x)


   #     print(x, end=" ")


def encode(message):    # will print out a bunch of numbers that represent how each letter is stored in the program
    for s in message:
       x = ord(s)
       print(x, end=" ")

def decode(message):
    num_list = message.split()
    acc = ' '
    for num in num_list:   # s is a string, need to convert it to an integer (strings have the '' around them)
        acc = acc + chr(eval(num))
    print(acc)






if __name__ == '__main__':
    main()
