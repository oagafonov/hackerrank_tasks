from functools import reduce

if __name__ == "__main__":
    n = int(input())
    s = set(map(int, input().split()))
    command_count = int(input())

    for i in range(0, command_count):
        command_args = input().rstrip().split()
        args = ""
        command = command_args[0]
        if len(command_args) > 1:
            args = int(command_args[1])

        eval_value = f's.{command}({args})'
        eval(eval_value)

    print(reduce(lambda a, b: a+b, s, 0))
