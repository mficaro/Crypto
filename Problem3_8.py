from CryptoHelpers import *
import math

dic1 = {
    "A" : "S",
    "B" : "A",
    "C" : "H",
    "D" : "V",
    "E" : "P",
    "F" : "B",
    "G" : "J",
    "H" : "W",
    "I" : "U",
    "J" : None,
    "K" : None,
    "L" : "X",
    "M" : "T",
    "N" : "D",
    "O" : "M",
    "P" : "Y",
    "Q" : None,
    "R" : "E",
    "S" : "O",
    "T" : "Z",
    "U" : "I",
    "V" : "F",
    "W" : "Q",
    "X" : None,
    "Y" : "G",
    "Z" : None
}
dic2 = {
    0 : "S",
    1 : "A",
    2 : "H",
    3 : "V",
    4 : "P",
    5 : "B",
    6 : "J",
    7 : "W",
    8 : "U",
    9 : "?",
    10 : "?",
    11 : "X",
    12 : "T",
    13 : "D",
    14 : "M",
    15 : "Y",
    16 : "?",
    17 : "E",
    18 : "O",
    19 : "Z",
    20 : "I",
    21 : "F",
    22 : "Q",
    23 : "?",
    24 : "G",
    25 : "?",
}

for i in range(1,27):
    row_size = i
    col_size = math.ceil(26/i)
    table = [None]*col_size
    for i in range(col_size):
        row = [None]*row_size
        table[i] = row

    i = 0
    for x in range(row_size):
        for y in range(col_size):
            if y is col_size - 1:
                if (26 - i) <= (((row_size - 1) - x) * (col_size - 1)):
                    table[y][x] = "-"
                    continue
            table[y][x] = dic2[i]
            i += 1
    for col in range(col_size):
        for row in range(row_size):
            print(" {} ".format(table[col][row]), end="")
        print()
    print()



