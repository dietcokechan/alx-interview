#!/usr/bin/python3
""" module defining isWinner function """


def isWinner(x, numbers):
    """ function to get who has won in prime game """
    mariaWinsCount = 0
    benWinsCount = 0

    for num in numbers:
        roundSet = list(range(1, num + 1))
        primeSet = primes_in_range(1, num)

        if not primeSet:
            benWinsCount += 1
            continue

        isMariaTurn = True

        while (True):
            if not primeSet:
                if isMariaTurn:
                    benWinsCount += 1
                else:
                    mariaWinsCount += 1
                break

            minPrime = primeSet.pop(0)
            roundSet.remove(minPrime)

            roundSet = [x for x in roundSet if x % minPrime != 0]

            isMariaTurn = not isMariaTurn

    if mariaWinsCount > benWinsCount:
        return "Winner: Maria"

    if mariaWinsCount < benWinsCount:
        return "Winner: Ben"

    return None


def is_prime(n):
    """ returns true if n is prime, else false """
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def primes_in_range(start, end):
    """ returns a list of prime numbers between start and end (inclusive) """
    primes = [n for n in range(start, end+1) if is_prime(n)]
    return primes
