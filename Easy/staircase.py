#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the staircase function below.
def staircase(n):
    ret = []
    for i in range(1,n+1):
        ret.append(' '*(n-i)+'#'*i)
    sys.stdout.write('\n'.join(ret))

        

if __name__ == '__main__':
    n = int(input())

    staircase(n)
