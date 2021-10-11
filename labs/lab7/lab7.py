"""
Name: <Lexi Padberg>
Partner: <your partner's name goes here – first and last>
<Lab7>.py
"""


def cash_conversion():
    dollar = eval(input("enter a dollar a dollar amount"))
    print("the amount of money you have is ${0:1.2f}".format(dollar))

def encode():
    x = input("enter a string")
    k = eval(input("input a number"))
    acc = ""
    for c in x:
        i = (ord(c))
        add = i + k
        new = chr(add)
        acc = acc + new
    print(acc)

def sphere_area(radius):
    area = 4 * 3.14 * radius ** 2
    return area

def sphere_volume(radius):
    volume = (4/3) * 3.14 * radius**3
    return volume

def sum_n(n):
    acc = 0
    for i in range(n +1):
       acc += i
    return acc

def sum_n_cubes(n):
    acc = 0
    for i in range(n+1):
        acc += i**3
    return acc

def encode_better():
    x = input("enter string 1: ")
    y = input("enter string 2: ")
    acc = ""
    for i in range(len(x)):
        c = ord(x[i])
        key = ord(y[i])
        add = c + key - 97
        acc += chr(add)
    print(acc)


def main():
    cash_conversion()
    encode()
    print(sphere_area(5))
    print(sphere_volume(5))
    print(sum_n(3))
    print(sum_n_cubes(3))
    encode_better()


main()
