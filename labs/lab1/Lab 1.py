"""
name:<Lexi Padberg>
lab_1.py

problem,:this function calculates the area of a rectangle
"""
def main():
    print("I look forward to learning to control this computer through programming!")

def calc_area():
    length = 20
    width = 5
    area = length * width
    print("Area=", area)


def calc_rec_area():
    length = eval(input("enter the length"))
    width = eval(input("enter the width"))
    area = length * width
    print("Area =", area)


def calc_volume():
    length = eval(input("enter the length"))
    width = eval(input("enter the width"))
    height = eval(input("enter the height"))
    volume = length * width * height
    print("Volume", volume)


def shooting_percentage():
    total_shots = eval(input("enter total_shots"))
    shots_made = eval(input("enter shots_made"))
    percentage = shots_made/total_shots
    print("percentage", percentage)


def coffee():
    pounds = eval(input("enter pounds"))
    pound_cost = 10.50
    shipping_cost = .86
    overhead = 1.50
    coffee_price = pounds * pound_cost + pounds * shipping_cost + overhead
    print("coffee_price", coffee_price)


def kilometers_to_miles():
    kilometers = eval(input("enter kilometers"))
    miles_to_kilometer = 1.61
    miles_traveled = kilometers/miles_to_kilometer
    print("miles_traveled", miles_traveled)
