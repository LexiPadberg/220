"""
Name: <Lexi Padberg>
<Lab 13>.py
"""


def is_in_binary(search_val, value):
    mid = search_val[len(search_val)//2]
    while mid != value and len(search_val) != 1:
        if mid > value:
            search_val = search_val[:mid]
        if mid < value:
            search_val = search_val[mid:]
        mid = search_val[len(search_val)//2]
    if len(search_val) == 1 and search_val[0] != value:
        return False
    return True


def selection_sort(values):
    for i in range(len(values)):
        lowest = values[i]
        pos = i
        for j in range(1+i, len(values)):
            if values[j] < lowest:
                lowest = values[j]
                pos = j
        values[i], values[pos] = values[pos], values[i]


def calc_area(rect):
    p1 = rect.getP1()
    p2 = rect.getP2()
    dx = p1.getX - p2.getX
    dy = p2.getY - p2.getY
    return dx*dy


def rect_sort(rects):
    dict = {}
    areas = []
    for rect in rects:
        dict[calc_area(rect)] = rect
        areas.append(calc_area(rects))
    selection_sort(areas)
    for i in range(len(areas)):
        rects[i] = dict[areas[i]]


def star_find(filename):
    infile = open(filename, "r")
    signals = infile.read().split()
    found = []
    for i in range(len(signals)):
        if 4000 <= int(signals[i]) <= 5000:
            found.append(int(signals[i]))
        if len(found) == 5:
            break
    print(len(found))
    print(found)
    if len(found) < 5:
        print("we didn't find 5")
    else:
        print(i)


def main():
    is_in_binary([1, 2, 3, 4], 3)
    selection_sort([2, 4, 1, 3])
    star_find("signals.txt")
    pass


main()
