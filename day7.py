def getCrabSubs() -> list[int]:
  return list(map(lambda x: int(x),open("day7input.txt", "r").readline().replace('\n', '').split(',')))

def calcCost(spaces: int) -> int:
  if spaces == 0:
    return 0
  sum:int = 0
  for i in range(spaces + 1):
    sum += i 
  return sum

crabSubs = getCrabSubs()

crabSubs.sort()

max = crabSubs[-1]

results:list[int] = []
costs:dict[int:int] = {}

for subPosition in range(max + 1):
  sum = 0
  for sub in crabSubs:
    spaces = abs(sub - subPosition)
    if spaces in costs:
      sum += costs[spaces]
    else:
      costs[spaces] = calcCost(spaces)
      sum = costs[spaces] + sum
  results.append(sum)


results.sort()

print(results[0])
