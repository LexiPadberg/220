"""
Name: <Lexi Padberg>
<Lab12>.py
"""

from random import randint


def find_and_remove_first(list, value):
    try:
        i = list.index(value)
        list[i] = "lexi"
    except:
        pass


def read_data(filename):
    file = open(filename, 'r')
    data = file.read()
    data = data.split()
    return data


def is_in_linear(search_val, val):
    i = 0
    while i < len(val):
        if val[i] == search_val:
            return True
        i += 1
        return False


def good_input():
    x = eval(input("enter a number: "))
    while 1 > x or x > 10:
        print("enter a number between 1-10")
        x = eval(input("enter a number: "))
    return x


def num_digits():
    x = eval(input("enter a number: "))
    while x >= 1:
        digits = 1
        while x != 0:
            x //= 10
            digits += 1
        print("number of digits:", digits)
        x = eval(input("enter a number: "))


def hi_lo_game():
    rand_num = randint(1, 100)
    guesses = 1
    num = eval(input("enter a number between 1-100:"))
    while num != rand_num and guesses != 7:
        guesses += 1
        if num < rand_num:
            print("too low")
        else:
            print("too high")
        num = eval(input("enter a number between 1-100: "))
    if num == rand_num:
            print("you win with", guesses, "guesses")
    else:
            print("you lose!", str(rand_num), "was the correct answer")


def main():
    good_input()
    num_digits()
    hi_lo_game()
    pass


main()
