from itertools import product

def char_to_int_list(char_list):
    int_list = []

    for char in char_list:
        int_list.append(int(char))
    
    return int_list

A = char_to_int_list(input().rstrip().split())
B = char_to_int_list(input().rstrip().split())

for r in product(A, B):
    print(r, end=" ")
