class Fish:
    interval:int = 6
    timer:int
    newFish:bool = False
    def __init__(self, timer:int, newFish:bool) -> None:
        self.timer = timer
        self.newFish = newFish


def buildFish() -> list[int]:
    fishInput = open("day6input.txt").readline().replace('\n', '')
    return list(map(lambda x: int(x), fishInput.split(',')))


fishMap = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0}

fishies = buildFish()

for fish in fishies:
    fishMap[fish] += 1

for day in range(255):
    
    old8 = fishMap[8]
    fishMap[8] = fishMap[9]
    old7 = fishMap[7]
    fishMap[7] = old8
    old6 = fishMap[6]
    fishMap[6] = old7
    old5 = fishMap[5]
    fishMap[5] = old6
    old4 = fishMap[4]
    fishMap[4] = old5
    old3 = fishMap[3]
    fishMap[3] = old4
    old2 = fishMap[2]
    fishMap[2] = old3
    old1 = fishMap[1]
    fishMap[1] = old2

    fishMap[9] = old1
    fishMap[7] += old1

    print(fishMap)

sum = 0
for (key, value) in fishMap.items():
    if key != 0:
        sum += value
print(sum)