"""
Name: <Lexi Padberg>
<lab3>.py

Problem: develop programs that do input, produce output, and do arithmetic using loops
"""


def average():
    x = eval(input("enter the amount of homework assignments"))
    acc = 0
    for i in range(x):
        score = eval(input("enter HW" + str(i + 1)))
        acc = acc + score / x
    print(acc)


def tip_jar():
    acc = 0
    for x in range(1, 5+1):
        donate = eval(input("enter amount of money you're donating"))
        acc = acc + donate
    print(acc)


def newton():
    x = eval(input("enter number to square root"))
    approx = x/2
    refine = eval(input("enter amount to improve approximation"))
    for i in range(refine):
        approx = (approx + x/approx) / 2
    print(approx)


def sequence():
   x = eval(input("enter number of terms "))
   for i in range(1, (x+1)):
      print(1 + (i//2 * 2))  # or (i + 1) % 2


def pi():
    n = eval(input("enter number of terms in the series"))
    acc = 1
    for x in range(n):
        numerator = 2 + (x//2 * 2)
        denom = 1 + ((x + 1)//2*2)
        acc = acc * (numerator/denom)
        print(numerator, denom)
    print(acc)
