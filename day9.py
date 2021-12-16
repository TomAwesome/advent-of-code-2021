from enum import Enum
class direction(Enum):
  Start = 0
  Up = 1
  Right = 2
  Down = 3
  Left = 4
def getMap() -> list[list[int]]:
  input = open("day9input.txt").readlines()
  map:list[list[int]] = []
  for line in input:
    row:list[int] = []
    for location in line.replace('\n', ''):
      row.append(int(location))
    map.append(row)
  return map



def getBasin(map:list[list[int]], point:tuple[int, int], previousPoints:set ) -> set:
  if map[point[0]][point[1]] == 9:
    return previousPoints
  
  newPoint:tuple = (point[0] - 1, point[1])
  if newPoint[0] >= 0 and (not newPoint in previousPoints):
    previousPoints.add(newPoint)
    getBasin(map, newPoint, previousPoints)

  newPoint = (point[0] + 1, point[1])
  if newPoint[0] <= len(map) - 1 and (not newPoint in previousPoints):
    previousPoints.add(newPoint)
    getBasin(map, newPoint, previousPoints)

  newPoint = (point[0], point[1] - 1)
  if newPoint[1] >= 0 and (not newPoint in previousPoints):
    previousPoints.add(newPoint)
    getBasin(map, newPoint, previousPoints)

  newPoint = (point[0], point[1] + 1)
  if newPoint[1] <= len(map[newPoint[0]]) - 1 and (not newPoint in previousPoints):
    previousPoints.add(newPoint)
    getBasin(map, newPoint, previousPoints)

  return previousPoints

basins:list[int] = []  

def isLowPoint(map:list[list:int], y:int, x:int) -> bool:
  point:int = map[y][x]
  lessThan = True
  if x > 0:
    lessThan = lessThan and point < map[y][x - 1]

  if x < len(map[y]) - 1 : #right:
    lessThan = lessThan and point < map[y][x + 1]
  if y > 0 : #up:
    lessThan = lessThan and point < map[y - 1][x]

  if y < len(map) - 1 : #down:
    lessThan = lessThan and point < map[y + 1][x]
  if lessThan:
    point = (y, x)
    basin = getBasin(map, point, {point})
    score:int = 0
    for point in basin:
      if map[point[0]][point[1]] != 9:
        score = score + 1 
    print(basin)
    basins.append(score)
  return lessThan

map = getMap()
lowPoints:list[int] = []


for y in range(len(map)):
  for x in range(len(map[y])):
    if isLowPoint(map, y, x):
      lowPoints.append(map[y][x] + 1)


print(basins)

basins.sort()

print(basins[-1] * basins[-2] * basins[-3])