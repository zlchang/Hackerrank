#!/bin/python3

import math
import os
import random
import re
import sys

sys.setrecursionlimit(10000)
#
# Complete the 'passwordCracker' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING_ARRAY passwords
#  2. STRING loginAttempt
#

def passwordCracker(passwords, loginAttempt):
    # Write your code here
    
    memo = {}
    def recursive(login):
        #arr = []
        if login in memo:
            return memo[login]
        if len(login) == 0:
            return []
        for pw in passwords:
            n = len(pw)
            s = login[:n]
            #print(pw, login)
            if s == pw:
                #arr.append(pw)
                r = recursive(login[n:])
                #print(s, login, r)
                if len(r) == 0 or r[0] != 'WRONG PASSWORD':
                    memo[login] = [pw]+r
                    return [pw] + r
        memo[login] = ['WRONG PASSWORD']
        return ['WRONG PASSWORD']
        
    return recursive(loginAttempt)
    
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        passwords = input().rstrip().split()

        loginAttempt = input()

        result = passwordCracker(passwords, loginAttempt)

        fptr.write(' '.join(result) + '\n')

    fptr.close()
