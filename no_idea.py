def contains(A, c):
    return c in A

if __name__ == "__main__":
    n, m = input().rstrip().split()
    C = [int(c) for c in input().rstrip().split()]
    A = set([int(c) for c in input().rstrip().split()])
    B = set([int(c) for c in input().rstrip().split()])

    # n, m = 3, 2
    # C = [1, 5, 3]
    # A = set([3, 1])
    # B = set([5, 7])

    happiness = 0
    for c in C:
        if contains(A, c):
            happiness += 1
        if contains(B, c):
            happiness -= 1

    print(happiness)
