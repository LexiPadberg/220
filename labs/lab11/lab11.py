"""
Name: <Lexi Padberg>
<Lab 11>.py
"""
from random import randint


def words(infile):
    infile = open(infile, "r")
    content = infile.read()
    return content.split("\n")


def rand_word(lists):
    return lists[randint(0, len(lists)-1)]


def fill(word, letters):
    secret = ["_"] * len(word)
    for letter in letters:
       for i in range(len(word)):
        if letter == word[i]:
            secret[i] = letter
    return "".join(secret)


def won(word, letters):
    x = fill(word, letters)
    if x == word:
        return True
    else:
        return False

def play():
    w = words("wordlist.txt")
    secret = rand_word(w)
    current = "_" * len(secret)
    incorrect = 0
    guesses = []
    while incorrect <= 7 and won(secret, guesses) != True:
        display = fill(secret, guesses)
        print(display)
        print(guesses)
        letter = input(" enter a letter to guess: ")
        while letter in guesses:
            letter = input("enter a letter to guess: ")
        guesses.append(letter)
        display = fill(secret, guesses)
        if display != current:
           incorrect += 1
        else:
            current = display



def main():
    play()
    pass


main()
