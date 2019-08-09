#!/bin/python3

import math
import os
import random
import re
import sys

def solve(text):
    template = r"(\b[A-Za-z]{1})"
    zip_reg = re.compile(template)
    find_result = zip_reg.findall(text)
    print (find_result)
    print(re.sub(template, lambda g: g.group(1).upper(), text))

if __name__ == '__main__':
    text = input()
    solve(text)