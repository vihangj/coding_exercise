#!/usr/bin/python

"""
This script calculates binary number
"""

from optparse import OptionParser


def calculate_binary_number(number=0, binary_string=''):
    if number <= 0:
        return binary_string

    binary_string += str(number % 2)
    number = number // 2
    return calculate_binary_number(number=number, binary_string=binary_string)


def main(number=0):
    print calculate_binary_number(number=number)[::-1]


if __name__ == '__main__':
    parser = OptionParser()
    parser.add_option('-n', '--number', dest='number', help='Number to find binary quivalent for')
    (options, args) = parser.parse_args()
    try:
        main(number=int(options.number))
    except Exception, err:
        raise Exception(err)
