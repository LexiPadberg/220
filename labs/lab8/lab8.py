"""
Name: <Lexi Padberg>
<Lab8>.py
"""

from encryption import encode, encode_better


def number_words(in_file_name, out_file_name):
    in_file = open(in_file_name, 'r')
    out_file = open(out_file_name, 'w+')
    i = 1
    for line in in_file:
        words = line.split(" ")
        for word in words:
            print(i, " ", word, file=out_file)
            i += 1
    in_file.close()
    out_file.close()

def hourly_wages(in_file_name, out_file_name):
    in_file = open(in_file_name, 'r')
    out_file = open (out_file_name, 'w+')
    for lines in in_file:
        parts = lines.split(" ")
        wage = float(parts[2])
        wage += 1.65
        wage = wage * int(parts[3])
        print(parts[:1], wage, file=out_file)
    in_file.close()
    out_file.close()

def checksum(isbn_str):
    acc = 0
    for i in range(10):
        pos = 10-i
        acc += int(isbn_str[0 + i]) * pos
    return acc

def send_message(file, friend):
    in_file = open(file, 'r')
    out_file = open(friend + ".txt", 'w+')
    for line in in_file:
        out_file.write(line)
    in_file.close()
    out_file.close()


def ssm(file, friend, key):
    in_file = open(file, 'r')
    out_file = open(friend + ".txt", 'w+')
    for line in in_file:
        out_file.write(encode(line, key))
    in_file.close()
    out_file.close()


def sum(file, friend, pad):
    in_file = open(file, 'r')
    out_file = open(friend + ".txt", 'w+')
    pad_file = open(pad, 'r')
    key = pad_file.read()
    for line in in_file:
        out_file.write(encode_better(line, key))
    in_file.close()
    out_file.close()


def main():
    number_words("Walrus.txt", "Wal_out.txt")
    hourly_wages("hourly_wages.txt", "wage_out.txt")
    checksum("0072946520")
    send_message("message.txt", "bob")
    ssm("secret_message.txt", "bob2", 3)
    sum("safest_message.txt", "bob3", "pad.txt")


main()
