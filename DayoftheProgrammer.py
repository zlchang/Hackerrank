#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the dayOfProgrammer function below.
def dayOfProgrammer(year):
    day = 256
    days = [31, 0, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    mm = 0
    counter = 1
    while counter < day:    
        if mm == 1:
            days[mm] = 28
            if year < 1918:
                if year % 4 == 0:
                    days[mm] = 29
            elif year == 1918:
                days[mm] = 15
            else:
                if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
                    days[mm] = 29
        counter += days[mm]

        mm += 1
    dd =  days[mm] - (counter - day)
    
    return '{:2d}.{:02d}.{:d}'.format(dd, mm, year)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    year = int(input().strip())

    result = dayOfProgrammer(year)

    fptr.write(result + '\n')

    fptr.close()
