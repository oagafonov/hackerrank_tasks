def print_formatted(number):
    max_len = len(f"{number:b}")
    for i in range(1, number+1):
        print("{0: >#{1}d} {0: >{1}o} {0: >{1}X} {0: >{1}b}".format(i, max_len))

# {i: >{max_len}#b}
if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
