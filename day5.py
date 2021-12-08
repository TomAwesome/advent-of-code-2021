class point:
  x:int
  y:int
  
  def __init__(self, x:int, y:int):
    self.x = x
    self.y = y
  
  def __repr__(self) -> str:
      return f'{self.x},{self.y}'
  
  def __hash__(self):
    return hash(self.x) ^ hash(self.y)
  
  def __eq__(self, other):
    return self.x == other.x and self.y == other.y

  def __ne__(self, other):
    return not(self == other)
  
  def toNextPoint(self, other):
    x:int
    if other.x < self.x:
      x = self.x - 1
    elif other.x > self.x:
      x = self.x + 1
    else:
      x = self.x
    y:int
    if other.y < self.y:
      y = self.y - 1
    elif other.y > self.y:
      y = self.y + 1
    else:
      y = self.y
    return point(x,y)


class line:
  pointOne:point
  pointTwo:point

  def __init__(self, pointOne:point, pointTwo:point):
    self.pointOne = pointOne
    self.pointTwo = pointTwo

  def isOrthogonal(self) -> bool:
    return self.pointOne.x == self.pointTwo.x or self.pointOne.y  == self.pointTwo.y
  
  def getPoints(self) -> list[point]:
    points:list[point] = []
    
    currentPoint = self.pointOne
    while currentPoint != self.pointTwo:
      points.append(currentPoint)
      currentPoint = currentPoint.toNextPoint(self.pointTwo)
    
    points.append(currentPoint)
    return points
  


def buildLines() -> list[line]:
  linesTxt = open("day5input.txt").readlines()
  allLines:list[line] = []
  for lineTxt in linesTxt:
    parts = lineTxt.replace('\n', '').split(' -> ')

    point1Parts = parts[0].split(',')
    point1:point = point(int(point1Parts[0]), int(point1Parts[1]))
    point2Parts = parts[1].split(',')
    point2:point = point(int(point2Parts[0]), int(point2Parts[1]))
    allLines.append(line(point1, point2))
      
  return allLines

waterMap:dict[point, int] = {}

allLines = buildLines()

#orthogonalLines = list(filter(lambda x: x.isOrthogonal(), allLines))

for orthogonalLine in allLines:
  for linePoint in orthogonalLine.getPoints():
    if linePoint in waterMap:
      waterMap[linePoint] += 1
    else:
      waterMap[linePoint] = 1

print(waterMap)

intersectingPoints:int = 0

for(key, value) in waterMap.items():
  if value > 1:
    intersectingPoints += 1

print(intersectingPoints)
