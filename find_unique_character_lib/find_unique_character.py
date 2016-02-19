#!/usr/bin/python

"""
This script will find unique character in a string.
e.g. r is unique character in teeter
"""

from optparse import OptionParser


def main(s=''):
    t = get_unique_character(s=s)
    print t


def get_unique_character(s=''):
    # Check if string has onlt one character
    if len(s) <= 1:
        return s
    # Iterate through the string
    for i in range(0, len(s)):
        if s[i] in s[(i + 1):]:
            # If a matching character found replace it with blank
            s = s.replace(s[i], "")
            # Iterate recursively
            return get_unique_character(s)
        else:
            # If no matching character found then display unique character
            return s[i]


if __name__ == '__main__':
    parser = OptionParser()
    parser.add_option('-s', '--string', dest='s', help='String')
    (options, args) = parser.parse_args()
    try:
        main(options.s)
    except Exception, err:
        raise Exception(err)
