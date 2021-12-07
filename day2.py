
commands = open("day2input.txt", "r").readlines()

xPostion = 0
yPostion = 0
aim = 0

for command in commands:
    commandParts = command.replace('\n', '').split(' ')
    if commandParts[0] == 'forward':
        value = int(commandParts[1])
        xPostion += value
        yPostion += value * aim
    elif commandParts[0]  == 'down':
        aim += int(commandParts[1])
    elif commandParts[0]  == 'up':
        aim -= int(commandParts[1])

print (xPostion)
print (yPostion)
print (xPostion * yPostion)