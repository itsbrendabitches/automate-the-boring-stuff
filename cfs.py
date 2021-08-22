#! /usr/bin/env python3

import random

numberOfStreaks = 0
coinFlips = []
hCount = 0
tCount = 0

for experimentNumber in range(10000):
    coin = random.randint(0, 1)
    if coin == 0:
        coinFlips.append('h')
        hCount += 1
        tCount = 0
    elif coin == 1:
        coinFlips.append('t')
        tCount += 1
        hCount = 0

    if hCount >= 6:
        numberOfStreaks += 1
        hCount = 0
    elif tCount >= 6:
        numberOfStreaks += 1
        tCount = 0

print('Chance of streak: %s%%' % (numberOfStreaks / 100))
print(numberOfStreaks)




    

