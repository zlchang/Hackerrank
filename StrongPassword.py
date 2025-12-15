#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumNumber function below.
def minimumNumber(n, password):
    # Return the minimum number of characters to make the password strong
    numbers = "0123456789"
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    special_characters = "!@#$%^&*()-+"
    counter = 0
    nn = 0
    nl = 0
    nu = 0
    ns = 0
    for i in range(n):
        p = password[i]
        if numbers.find(p) != -1:
            nn = 1
        elif lower_case.find(p) != -1:
            nl = 1
        elif upper_case.find(p) != -1:
            nu = 1
        elif special_characters.find(p) != -1:
            ns = 1
    counter = nn + nl + nu + ns
    req = max(4-counter, 6 - n, 0)
    return req
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    password = input()

    answer = minimumNumber(n, password)

    fptr.write(str(answer) + '\n')

    fptr.close()
