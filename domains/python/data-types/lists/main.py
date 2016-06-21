commands = int(input())
array = []
for i in range(commands):
    command = input().strip()
    if len(command) > 0:
        command = command.split(' ')
        if command[0] == 'append':
            array.append(int(command[1]))
        elif command[0] == 'insert':
            array.insert(int(command[1]), int(command[2]))
        elif command[0] == 'remove':
            array.remove(int(command[1]))
        elif command[0] == 'pop':
            array.pop()
        elif command[0] == 'sort':
            array.sort()
        elif command[0] == 'reverse':
            array.reverse()
        elif command[0] == 'print':
            print(array)
        else:
            print('Unsupport command %s' % str(command))
