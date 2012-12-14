#!/usr/bin/env python

from math import ceil

def divisible(amount):
    return amount % 5 == 0

def commission(amount):
    return 0.5 + (.01 * amount)

def checkio(amounts):
    total = amounts[0]
    withdrawals = amounts[1]
    for i in withdrawals:
        if (not i >= total) and divisible(i):
            total -= ceil(i + commission(i))
    return total

print(checkio([120, [10, 20, 30]])) #57
print(checkio([120, [200, 119]]))   #120
print(checkio([120, [3, 10]]))      #109
print(checkio([120, [120, 10, 122, 2, 10, 10, 30, 1]])) #56