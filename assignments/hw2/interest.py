"""
Name: Lexi Padberg
interest.py

Problems: calculate the value of an investment after ten years

Certification of Authenticity: I certify that this assignment is entirely my own work
"""


def main():
      #    print("this program will calculate the value of an investment after ten years")
    apr = eval((input("input the annual interest")))
    apr = (apr/100)
    billing_cycle = eval((input("enter number of days in billing cycle")))
    net_balance = eval((input("enter the previous net balance")))
    payment = eval((input("enter the payment amount")))
    cycle_day = eval((input("enter the day the payment was made")))
    step1 = (billing_cycle * net_balance)
    step2 = payment * (billing_cycle - cycle_day)
    monthly_interest = (step1 - step2)
    daily_balance = monthly_interest / billing_cycle

    monthly_rate = daily_balance * (apr / 12)
    monthly_rate = round(monthly_rate, 2)
    print(monthly_rate)


if __name__ == '__main__':

    main()
