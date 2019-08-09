def merge_the_tools(string, k):
    string_len = len(string)
    count = int(string_len/k)

    for step in range(0, count):
        text = string[step*k:(step+1)*k]
        result_string = ""

        for c in text:
            if result_string.count(c) == 0:
                result_string += c
        
        print(result_string)


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
