
def part2(inputs): 
    numberOfIncreases = 0
    slidingWindows = []
    for i in range(len(inputs)):
        window = int(inputs[i].replace('\n', ''))
        if i + 1 < len(inputs):
            window += int(inputs[i + 1].replace('\n', ''))
        else:
            continue
        if i + 2 < len(inputs):
            window += int(inputs[i + 2].replace('\n', ''))
        else:
            continue
        slidingWindows.append(window)

    numberOfIncreases = 0
    previousSlidingWindow = slidingWindows.pop(0)

    for slidingWindow in slidingWindows:

        if slidingWindow > previousSlidingWindow:
            numberOfIncreases += 1
        
        previousSlidingWindow = slidingWindow
    return numberOfIncreases
        


def part1(inputs):
    numberOfIncreases = 0
    previousInput = -1

    for input in inputs:
        intInput = int(input.replace('\n', ''))

        if previousInput != -1 and intInput > previousInput:
            numberOfIncreases += 1
        
        previousInput = intInput
    return numberOfIncreases



inputsfile = open("day1input.txt", "r")

inputs = inputsfile.readlines()


print(part2(inputs))
