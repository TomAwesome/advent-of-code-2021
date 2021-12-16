
def getLines() -> list[str]:
  return list(map(lambda x: x.replace('\n', ''), open("day10input.txt").readlines()))

closingMappings:dict[str:str] = {')':'(', '}':'{', ']':'[', '>':'<'}

finishingPoints:dict[str:int] = {'(':1, '[':2, '{':3, '<': 4}

def checkLine(line:str) -> int:
  syntax:list = []
  for character in line:
    if character == '(' or character == '[' or character == '{' or character == '<':
      syntax.append(character)
    else:
      openingChar = syntax.pop()
      if openingChar != closingMappings[character]:
        print(f'found {character} needed closing for {openingChar}')
        return None
  score:int = 0
  syntax.reverse()
  for point in list(map(lambda x: finishingPoints[x], syntax)):
    score = (score * 5) + point
  return score

scores:list[int] = []
for line in getLines():
  score = checkLine(line)
  if score:
    scores.append(score)

scores.sort()

print(scores)

print(scores[int((len(scores) - 1) / 2)])