#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    x = [sum(arr) - arr[i] for i in range(len(arr))]
    print("%d %d" %(min(x), max(x)))

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
