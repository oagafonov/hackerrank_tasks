if __name__=="__main__":
    n = int(input())
    i = 0
    contries = set()
    while i < n:
        contries.add(input())
        i+=1
    print(len(contries))