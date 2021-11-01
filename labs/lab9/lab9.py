"""
Name: <Lexi Padberg>
<Lab8>.py
"""

def addTen(nums):
    for i in range(len(nums)):
       nums[i] = nums[i] + 10


def squareEach(nums):
    for i in range(len(nums)):
        nums[i] = nums[i] ** 2


def sumList(nums):
    acc = 0
    for i in range(len(nums)):
        acc+= float(nums[i])
    return acc


def toNumbers(strList):
    for i in range(len(strList)):
        strList[i] = float(strList[i])



def writeSumofSquares():
    infile = input("enter a file name")
    outfile = input("enter a file name")
    readfile= open(infile, 'r')
    writefile= open(outfile, 'w+')
    for line in readfile:
        nums = line.split(" ")
        toNumbers(nums)
        squareEach(nums)
        summation = sumList(nums)
        writefile.write("sum of squares = " + str(summation) + "\n")

def starter():
    weight = eval(input("enter the weight"))
    wins = eval(input("enter your wins"))
    if weight >= 150 and weight <= 160 and wins>= 5:
        print("starter")
    if weight > 199 or wins > 20:
        print("starter")
    else:
        print("not a starter")



def leapyear(year):
    if year % 4 == 0 and (year %100 or year %400 == 0):
        print(year, " is a leap year!")
    else:
        print(year, " is not a leap year")

from graphics import *
import math

def circleOverlap():
    win = GraphWin("circles", 400, 400)
    p1 = win.getMouse()
    p2 = win.getMouse()
    r1 = math.sqrt((p1.getX()-p2.getX()) ** 2 + (p1.getY() - p2.getY()))
    c1 = Circle(p1,r1)
    c1.draw(win)

    p3 = win.getMouse()
    p4 = win.getMouse()
    r2 = math.sqrt((p3.getX() - p4.getX()) ** 2 + (p3.getY() - p4.getY()))
    c2 = Circle(p3, r2)
    c2.draw(win)
    r3 = math.sqrt((p1.getX() - p3.getX()) ** 2 + (p1.getY() - p3.getY()))

    if r3 <= r1 + r2:
       x = Text(Point(200,200), "the circles overlap")
       x.draw(win)

    if r3 >= r1 + r2:
        y =Text(Point(200,200), "the circles do not overlap")
        y.draw(win)


    win.getMouse()
    win.close()



def main():
    toNumbers(["3", "4"])
    writeSumofSquares()
    starter()
    leapyear(2001)
    circleOverlap()
    pass


main()
