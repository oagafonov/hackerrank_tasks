#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    test = 'agafonov   oleg 12db 1b'
    template = r"(\b[A-Za-z])[a-z]"
    template = r"(\b[A-Za-z]{1})"

    zip_reg = re.compile(template)
    # zip_reg = re.compile(r"(1\d{1}1)(5\d{1}5)")
    # find_result = zip_reg.findall('agafonov oleg 12db 1b')
    find_result = zip_reg.findall(test)
    print (find_result)
    print(re.sub(template, lambda g: g.group(1).upper(), test))

if __name__ == '__main__':
    #s = input()
    solve("")