#!/usr/bin/env python

def checkio(amounts):
    sofia, rise, oldman, reduction = amounts
    while sofia < oldman:
        sofia += rise
        if sofia > oldman:
            return oldman
        oldman -= reduction
    return sofia

print(checkio([150, 50, 1000, 100]))
print(checkio([500, 300, 700, 100]))