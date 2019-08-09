# if __name__ == '__main__':
#     N = int(input())

task_list = []

# for n in range(N):
#     command_parts = input().rstrip().split()
#     if (command_parts[0] == "print"):
#         print(n)

N = 12
commands = [
    ['insert', '0', '5'],
    ['insert', '1', '10'],
    ['insert', '0', '6'],
    ['print'],
    ['remove', '6'],
    ['append', '9'],
    ['append', '1'],
    ['sort'],
    ['print'],
    ['pop'],
    ['reverse'],
    ['print'],
]

for n in range(N):
    command_parts = commands[n]
    command = command_parts[0]

    command_args = []

    for index, part in enumerate(command_parts):
        if index == 0:
            command = part
        else:
            command_args.append(int(part))
    if command == "print":
        print(task_list)
    else:
        eval(f'task_list.{command}(*{command_args})')

    # if len(command_parts) > 1:
    #     a = int(command_parts[1])
    # if len(command_parts) > 2:
    #     b = int(command_parts[2])

    # ar

    #eval('task_list.insert(*[0, 1])')

    # if command == "print":
    #     print(task_list)
    # elif command == "insert":
    #     task_list.insert(a, b)
    # elif command == "remove":
    #     task_list.remove(a)
    # elif command == "append":
    #     task_list.append(a)
    # elif command == "sort":
    #     task_list.sort()
    # elif command == "pop":
    #     task_list.pop()
    # elif command == "reverse":
    #     task_list.reverse()
