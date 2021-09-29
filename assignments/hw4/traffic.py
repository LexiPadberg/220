"""
Name: Lexi Padberg
traffic.py

Problem: write a program that will help analyze traffic patterns

Certification of Authenticity: I certify that this assignment is entirely my own work
"""


def main():
    number_of_roads = eval(input("How many roads were surveyed? "))
    total_cars = 0
    for i in range(number_of_roads):
        day = str(1 + i)
        acc = 0
        number_of_days = eval(input("How many days was road " + day + " surveyed?"))
        for j in range(number_of_days):
            cars_per_road = eval(input("How many cars traveled on day " + str(j + 1)))
            acc = acc + cars_per_road
            average_cars = round(((acc) / number_of_days), 2)
            total_cars = cars_per_road + total_cars
            total_average = round(total_cars / number_of_roads, 2)
        print("Road", str(i+1), "average vehicles per day: ", float(average_cars))
    print("Total number of vehicles traveled on all roads: ", float(total_cars))
    print("Average number of vehicles per road: ", float(total_average, ))


if __name__ == '__main__':
    main()
