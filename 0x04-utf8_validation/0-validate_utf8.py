#!/usr/bin/python3
"""UTF-8 Validation"""


def get_leading_set_bits(num):
    """returns the number of leading set bits"""
    bits = 0
    shift = 1 << 7
    while shift & num:
        bits += 1
        shift = shift >> 1
    return bits


def validUTF8(data):
    """determines if a given data set represents a valid UTF-8 encoding"""
    count = 0
    for i in range(len(data)):
        if count == 0:
            count = get_leading_set_bits(data[i])
            '''1-byte (format: 0xxxxxxx)'''
            if count == 0:
                continue
            '''a character in UTF-8 can be 1 to 4 bytes long'''
            if count == 1 or count > 4:
                return False
        else:
            '''checks if current byte has format 10xxxxxx'''
            if not (data[i] & (1 << 7) and not (data[i] & (1 << 6))):
                return False
        count -= 1
    return count == 0
