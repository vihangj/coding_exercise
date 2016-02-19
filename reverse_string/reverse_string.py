#!/usr/bin/python


from optparse import OptionParser


def main(s=''):
    print reverse_string(s)


def reverse_string(text):
    if len(text) <= 1:
        return text
    return reverse_string(text[1:]) + text[0]


if __name__ == '__main__':
    parser = OptionParser()
    parser.add_option('-s', '--string', dest='s', help='Reverse string')
    (options, args) = parser.parse_args()
    try:
        main(s=options.s)
    except Exception, er:
        raise Exception(er)
