"""
Name: Lexi Padberg
mean.py

Problems: calculate the value of the different types of averages

Certification of Authenticity: I certify that this assignment is entirely my own work
"""
import math


def main():
    value_amt = eval(input("enter the values to be entered:"))
    acc = 0
    acc2 = 0
    acc3 = 1
    for i in range(value_amt):
        value = eval(input("enter value: " + str(i + 1)))
        acc = value**2 + acc
        rms_average = math.sqrt(acc/value_amt)
        acc2 = (1/value) + acc2
        harmonic_mean = value_amt / acc2
        acc3 = value * acc3
        geometric_mean = (acc3) ** (1 / value_amt)
    print(round(rms_average, 3))
    print(round(harmonic_mean, 3))
    print(round(geometric_mean, 3))


if __name__ == '__main__':
    main()
