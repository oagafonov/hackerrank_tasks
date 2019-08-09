def text_sort(c):
    print(c)
    if ord('a') <= ord(c) <= ord('z'):
        return ord(c)
    elif ord('A') <= ord(c) <= ord('Z'):
        return ord(c)*100

    if c.isdigit():
        number = int(c)
        if number % 2 != 0:
            return ord(c)*1000
        else:
            return ord(c)*10000

    return ord(c)


text = input()
print(''.join(sorted(text, key=text_sort)))
