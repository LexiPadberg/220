"""
name Lexi Padberg
chaos.py

problem: this problem illustrates a chaotic function
"""


def main():
    print("This program illustrates a chaotic function")
    # this line takes user input
    x = eval(input("enter a number between 0 and 1:"))
    for i in range(10):
        x = 3.9 * x * (1-x)
        print(x)

main()

