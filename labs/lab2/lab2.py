"""
Name: <Lexi Padberg>
<Lab 2>.py

Problem: develop functions that do input, produce output, and do arithmetic
"""
import math

def sum_of_threes():
    acc = 0
    x = eval(input("enter the max"))
    for x in range(0, x+1, 3):
        acc = acc + x
    print(acc)


def multiplication_table():
    for h in range(1, 11):
        for L in range(1, 11):
           print(h * L, end=" ")
        print()


def triangle_area():
    a = (eval(input("enter side a")))
    b = (eval(input("enter side b")))
    c = (eval(input("enter side c")))
    s = ((a + b +c)/2)
    A = math.sqrt(s * (s-a) * (s-b) * (s-c))
    print(A)



def sum_of_squares():
    start = (eval(input("enter start")))
    end = (eval(input("enter end")))
    acc = 0
    for x in range(start, end +1):
            acc += (x * x)
    print(acc)


def power():
    base = eval(input("enter base"))
    exp = eval(input("enter exponent"))
    acc = 1
    for x in range (0, exp, 1):
        acc =4 * 4
        acc = acc * 4
    print (acc)