vowels = ['A', 'E', 'I', 'O', 'U']


def count_substring(string, predicate):
    count = 0
    chart_count = len(string)

    for position, c in enumerate(string):
        if predicate(c):
            count += chart_count - position

    return count


def minion_game(string):
    count_kevin = count_substring(string, lambda c: c in vowels)
    count_stuart = count_substring(string, lambda c: c not in vowels)

    if count_kevin > count_stuart:
        print(f"Kevin {count_kevin}")
    elif count_stuart > count_kevin:
        print(f"Stuart {count_stuart}")
    else:
        print("Draw")


if __name__ == '__main__':
    s = input()
    minion_game(s)
