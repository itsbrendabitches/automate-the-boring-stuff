#! /usr/bin/env python3

def collatz(number):
    if number % 2 == 0:
        return number // 2
    if number % 2 == 1:
        return 3 * number + 1

print('Enter a number.')

while True:
    userNumber = int(input())
    print(collatz(userNumber))
    if collatz(userNumber) == 1:
        break 
    
