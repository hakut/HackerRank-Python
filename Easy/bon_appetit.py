#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the bonAppetit function below.
def bonAppetit(bill, k, b):
    b_ac = 0
    for i in range(len(bill)):
        if i != k:
            b_ac += bill[i]
    b_ac = b_ac//2
    if b_ac == b:
        print("Bon Appetit")
    else:
        print(b-b_ac)

if __name__ == '__main__':
    nk = input().rstrip().split()

    n = int(nk[0])

    k = int(nk[1])

    bill = list(map(int, input().rstrip().split()))

    b = int(input().strip())

    bonAppetit(bill, k, b)
