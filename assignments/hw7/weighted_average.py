"""
Name: Lexi Padberg
weighted_average.py

Problem: write a program that averages grades together

Certification of Authenticity: I certify that this assignment is entirely my own work
"""


def main():
    weighted_average("grades.txt", "avg.txt")


def weighted_average(in_file, out_file):
    in_file = open(in_file, 'r')
    out_file = open(out_file, 'w')
    class_size = 0
    class_acc = 0
    for line in in_file:
        avg_acc = 0
        weight_acc = 0
        newline = line.split(": ")
        name_list = newline[0].split(" ")
        score_list = newline[1].split(" ")
        name= name_list[0]
        for i in range(1, len(name_list)):
            name+= " " + name_list[i]
        for i in range(0, len(score_list), 2):
            weight = score_list[i]
            weight_acc += int(weight)
        if weight_acc > 100:
            out_file.write(name +  "'s" + " average: " + "Error: The weights are more than 100." + "\n")
        elif (weight_acc < 100):
            out_file.write(name +  "'s" + " average: " + "Error: The weights are less than 100." + "\n")
        else:
            for i in range(0, len(score_list), 2):
                average = int(score_list[i]) * int(score_list[i + 1]) / 100
                avg_acc = avg_acc + average
            out_file.write(name + "'s" + " average: " + str(round(avg_acc, 1)) + "\n")
            class_size += 1
            class_acc = class_acc + round(avg_acc,1)

    if class_size == 0:
        class_avg = 0
    else:
        class_avg = class_acc / class_size
    out_file.write("Class average: " + str(round(class_avg,1)))







if __name__ == '__main__':
    main()
