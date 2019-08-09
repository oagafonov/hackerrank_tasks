task_list = []

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