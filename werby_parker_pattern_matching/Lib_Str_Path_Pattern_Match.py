#!/usr/bin/python
"""
This library prints best matched pattern against a path. 
"""

import os
import collections


class PathStringPatternMatch(object):
    """
        Class to string pattern match
    """

    def __init__(self, input_file):
        if not os.path.isfile(input_file):
            raise Exception("Please provide input file.")
        self.input_file = input_file
        self.patterns = []
        self.paths = []
        self.position_weight = []
        self.match_weight = 0
        self.exact_match = 2
        self.wildcard = 1

    def find_matches(self):
        match = collections.defaultdict(list)
        with open(self.input_file, "r") as fh:
            no_of_patterns = int(fh.readline())
            self.patterns = [fh.readline() for _ in range(no_of_patterns)]
            try:
                no_of_paths = int(fh.readline())
            except Exception, read_err:
                read_err = "Expecting no of path integer value. Error : " + str(read_err)
                raise Exception(read_err)

            self.paths = [fh.readline() for _ in range(no_of_paths)]

            for pattern in self.patterns:
                pattern = pattern.rstrip()
                patterns_len = len(pattern.replace(',', '').replace('*', ''))
                for paths in self.paths:
                    paths = paths.rstrip()
                    self.position_weight = list(reversed(range(1, len(paths.replace('/', '')) + 1)))
                    self.match_weight = len(paths.replace('/', '')) + patterns_len
                    match[paths].append({self.match_string_pattern(path=paths, pattern=pattern): pattern})

    def match_string_pattern(self, path='', pattern=''):
        path = path.split("/")
        pattern = pattern.split(",")

        i = 0
        sum = 0
        atleast_one_match = 0
        for s in path:
            j = 0
            for y in pattern:
                if s == y:
                    atleast_one_match += 1
                    if i == j:
                        sum += self.position_weight[i] + self.exact_match
                    else:
                        sum += self.exact_match
                elif y == '*':
                    if i == j:
                        sum += self.wildcard
                    else:
                        sum += self.wildcard
                j += 1
            i += 1
        return (sum + atleast_one_match) if atleast_one_match else 0
