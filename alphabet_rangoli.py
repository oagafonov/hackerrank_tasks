def get_char(index):
    return chr(ord('a') + index)


def print_rangoli(size):
    alphabet_nubmers = list(range(size))
    strings = []
    alphabet_nubmers.reverse()

    if size == 1:
        print (get_char(0))
        return

    string = ""

    for char_index in alphabet_nubmers:
        char = get_char(char_index)
        total_string = "{0:-^{1}}".format("{0}-{1}-{2}".format(string, char, string[::-1]), 2*size-1+2*size - 2)
        string = "{0}-{1}".format(string, char).strip('-')
        print(total_string)
        strings.insert(0, total_string)

    for i, string in enumerate(strings):
        if i > 0:
            print(string)


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
