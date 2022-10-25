#!/#!usr/bin/python3
import random
import math

randlist = ["string", 1.234, 28]

oneToTen = list(range(10))

randList = randlist + oneToTen

print(randList[0])

print("List length:", len(randList))

first3 = randlist[0:3]

for i in first3:
    print("{} : {}".format(first3.index(i), i))

print(first3[0] * 3)

print("Index of string:", first3.count("string"))


first3[0] = "new string"
for i in first3:
    print("{} : {}".format(first3.index(i), i))



