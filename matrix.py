#!/bin/python3

import math
import os
import random
import re
import sys

# first_multiple_input = input().rstrip().split()

# n = int(first_multiple_input[0])

# m = int(first_multiple_input[1])

tr = {
    '!': ' ',
    '@': ' ',
    '#': ' ',
    '$': ' ',
    '%': ' ',
    '&': ' '
}


def translate_text(text):
    result = ""
    for i in range(len(text)):
        try:
            result += tr[text[i]]
        except:
            result += text[i]
    return result


n = 7
m = 3

matrix = []

matrix = [
    'Tsi',
    'h%x',
    'i #',
    'sM ',
    '$a ',
    '#t%',
    'ir!',
]

# for _ in range(n):
#     matrix_item = input()
#     matrix.append(matrix_item)

print(matrix)

matrix_string = ""

# matrix to string
for i in range(m):
    for j in range(n):
        matrix_string += matrix[j][i]

print(matrix_string)
print(translate_text(matrix_string))

#reg = re.compile(r"(\d)(?=1)")
#reg = re.compile(r"\s\s+")
# reg = re.compile(r"[\w\d]([!@#$%&\s]+)[\w\d]")
#print(reg.sub(" ", translate_text(matrix_string)))
# ХЗ так и не понял почему он в sub как группу рассматривает еще и предшествующий и следующий за группой символы
# и удаляет их тоже. 
# из-за этого приходится их выделать в собственные группы и делать комбинацих из них и пробела
template = r"(?P<first>[\w\d])(?P<second>[!@#$%&\s]+)(?P<third>[\w\d])"
print(re.sub(template, r"\g<first> \g<third>", matrix_string))
print(re.findall(template, matrix_string))
# print(re.match(r"[\w\d](<first>[!@#$%&\s]+)[\w\d]",  matrix_string))
#print(reg.sub(" ", matrix_string))
# print(reg.findall(matrix_string))
