#!/usr/bin/python3
""" making changes """


def makeChange(coins, total):
    """ determine the fewest number of coins needed to meet a given amount """
    if total <= 0:
        return 0
    count = 0
    temp = 0
    coins.sort(reverse=True)
    for i in coins:
        while count < total:
            count += i
            temp += 1
        if count == total:
            return temp
        count -= i
        temp -= 1
    return -1
