#!/usr/bin/python


from Lib_Str_Path_Pattern_Match import PathStringPatternMatch


def main():
    obj = PathStringPatternMatch(input_file='test.txt')
    obj.find_matches()


if __name__ == '__main__':
    main()
