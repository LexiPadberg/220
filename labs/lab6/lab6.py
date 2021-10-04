"""
Name: <Lexi Padberg>
lab6.py
"""


def name_reverse():
    """
    Read a name in first-last order and display it in last-comma-first order.
    """
    first_last = input("enter first and last name separated by a space: ")
    x = first_last.split(' ')
    print(x[1], ",",  x[0])


def company_name():
    website = input("enter the website of your company: ")
    company = website.split(".")
    print(company[1])


def initials():
     name_amount = input("enter the amount of students: ")
     for i in range(int(name_amount)):
        first = input("enter the first name of student " + str(i+1) + " : ")
        last = input("enter " + first + "'s last name: ")
        print(first[0].upper() + last[0].upper())


def names():
    names = input("Enter people's names, separated by commas: ")
    name = names.split(", ")
    for i in name:
        x = i.split(" ")
        print("the initials are", (x[0][0] + x[1][0]))


def thirds():
    sentences = eval(input("enter how many sentences will be input: "))
    for i in range(sentences):
        sent = input("enter sentence " + str(i+1) + " here: ")
        print(sent[2::3])


def word_average():
    sentence = input("enter a sentence: ")
    word = sentence.split(" ")
    acc = 0
    for i in word:
        acc = acc + len(i)
    print((acc)/len(word))



def pig_latin():
    sentence = input("enter a sentence: ")
    lower_sentence = sentence.lower()
    words = lower_sentence.split(" ")
    for i in words:
        pig_lat = i[1:] + i[0] + 'ay'
        print(pig_lat, end=" ")






def main():

 name_reverse()
 company_name()
 initials()
 names()
 thirds()
 word_average()
 pig_latin()

main()
