"""
Name: Lexi Padberg
convert.py

practicing software development process

Problem: Convert Celsius to Fahrenheit

certification of authenticity:
I certify that this assignment is entirely my own work
"""
# indentifiers: names of variables, modules, etc. Need to start with a letter or an underscore
# test data, 0 -> 32
# 100 -> 212
def main():
   celsius = eval(input("enter the temperature in celsius"))  # take user input in degrees celsius and call it celsius
   fahrenheit = ((9/5) * celsius + 32)   # convert input to F using the equation (9/5) X celsius + 32
   print("Hey that's", fahrenheit, "degrees Fahrenheit!")  # print the output


main()
