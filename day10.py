
def getLines() -> list[str]:
  return list(map(lambda x: x.replace('\n', ''), open("day10input.txt").readlines()))

closingMappings:dict[str:str] = {')':'(', '}':'{', ']':'[', '>':'<'}

def checkLine(line:str) -> int:
  syntax:list = []
  for character in line:
    if character == '(' or character == '[' or character == '{' or character == '<':
      syntax.append(character)
    else:
      openingChar = syntax.pop()
      if openingChar != closingMappings[character]:
        print(f'found {character} needed closing for {openingChar}')
        if character == ')':
          return 3
        elif character == ']':
          return 57
        elif character == '}':
          return 1197
        else:
          return 25137
  return 0

scores:list[int] = []
for line in getLines():
  scores.append(checkLine(line))

print(sum(scores))
