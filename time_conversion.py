#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    h = int(s[0:2])
    if s == '12:00:00PM':
        return '12:00:00'
    elif s == '12:00:00AM':
        return '00:00:00'
    elif str(s[-2:]) == 'PM':
        h += 12
        return ("%d%s" %(h,s[2:-2]))
    else:
        return s
    

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
