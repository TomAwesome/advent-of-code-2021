class SevenSegment:
  numbersStates:dict[str:int]
  originalLookUp:dict[str:str]
  reverseLookUp:dict[str:str]
  reverseDigitLookUp:dict[int:str] = {}
  numbers:list[str]

  def __init__(self, input:str):
    parts:list[str] = input.replace('\n', '').split(' | ')
    self.numbers = list(map(lambda x: ''.join(sorted(x)), parts[1].split()))
    self.numbersStates = {''.join(sorted(value)): -1 for value in parts[0].split()}
    self.originalLookUp = {value: ''.join(sorted(value)) for value in parts[0].split()}
    self.reverseLookUp = {''.join(sorted(value)): value for value in parts[0].split()}


    self.findTheUnqiueDigits()

  def SetDigit(self, key, sortedKey, value):
    self.numbersStates[sortedKey] = value
    self.originalLookUp[key] = sortedKey
    self.reverseDigitLookUp[value] = sortedKey
    self.reverseLookUp[sortedKey] = key

  def findTheUnqiueDigits(self):
    for (key, value) in self.originalLookUp.items():
      if len(key) == 2:
        self.SetDigit(key, value, 1)
      elif len(key) == 3:
        self.SetDigit(key, value, 7)
      elif len(key) == 4:
        self.SetDigit(key, value, 4)
      elif len(key) == 7:
        self.SetDigit(key, value, 8)
    
    self.FindThe6SegmentDigits()
    self.FindThe5SegmentDigits()
  
  def FindThe5SegmentDigits(self):
    seg5s:list[str] = []
    for key in self.originalLookUp.keys():
      if len(key) == 5:
        seg5s.append(key)
    one = self.reverseLookUp[self.reverseDigitLookUp[1]]
    for possible3 in seg5s:
      if one[0] in possible3 and one[1] in possible3:
        self.SetDigit(possible3, ''.join(sorted(possible3)), 3)
        seg5s.remove(possible3)
        break
    four = self.reverseLookUp[self.reverseDigitLookUp[4]]
    for possible5 in seg5s:
      if len(set(four).intersection(possible5)) == 3:
        self.SetDigit(possible5, ''.join(sorted(possible5)), 5)
        seg5s.remove(possible5)
        break
    self.SetDigit(seg5s[0], ''.join(sorted(seg5s[0])), 2)
    
  
  def FindThe6SegmentDigits(self):
    seg6s:list[str] = []
    for key in self.originalLookUp.keys():
      if len(key) == 6:
        seg6s.append(key)
    one = self.reverseLookUp[self.reverseDigitLookUp[1]]
    for possible6 in seg6s:
      if len(set(one).intersection(possible6)) == 1:
        self.SetDigit(possible6, ''.join(sorted(possible6)), 6)
        seg6s.remove(possible6)
        break
    four = self.reverseDigitLookUp[4]
    for possible9 in seg6s:
      if len(set(four).intersection(possible9)) == 4:
        self.SetDigit(possible9, ''.join(sorted(possible9)), 9)
        seg6s.remove(possible9)
        break
    
    self.SetDigit(seg6s[0], ''.join(sorted(seg6s[0])), 0)
  
  def getCountOfUnqiueDigits(self):
    sum:int = 0
    for number in self.numbers:
      if self.numbersStates[number] in self.reverseDigitLookUp:
        sum += 1
    return sum

  def GetCode(self) -> int:
    code:str= ''
    for number in self.numbers:
      code += self.numbersStates[number].__str__()
    return int(code)

        
def GetSevenSegments() -> list[SevenSegment]:
  with open("day8input.txt", "r") as file:
    return list(map(lambda x: SevenSegment(x), file.readlines()))


segments = GetSevenSegments()
codes:list[int] = []
for segment in segments:
  codes.append(segment.GetCode())

print(sum(codes))
