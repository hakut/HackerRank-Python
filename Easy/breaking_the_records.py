#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the breakingRecords function below.
def breakingRecords(scores):
    res = []
    minc,maxc = 0,0
    minv,maxv = scores[0],scores[0]
    for i in range(len(scores)):
        if i == len(scores)-1:
            break
        elif minv>scores[i+1]:
            minc += 1
            minv = scores[i+1]
        elif maxv<scores[i+1]:
            maxc += 1
            maxv = scores[i+1]
    

    res = maxc,minc
    return res



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
