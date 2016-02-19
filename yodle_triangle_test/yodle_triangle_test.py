#!/usr/bin/python


def calculate_sum(data=''):
    if len(data) == 0:
        return 0

    for i in sorted(data):
        if i == 0:
            continue
        for k in range(len(data[i])):
            if k == 0:
                data[i][k] += data[i - 1][k]
            elif k == (len(data[i]) - 1):
                data[i][k] += data[i - 1][k - 1]
            else:
                data[i][k] = max((data[i - 1][k - 1] + data[i][k]), (data[i - 1][k] + data[i][k]))
    return max(data[i])


triangle_file = open("triangle_test.txt_orig", "rb")
triangle_data = {}
i = 0
for row in triangle_file:
    triangle_data[i] = map(int, row.split())
    i += 1

print calculate_sum(data=triangle_data)
