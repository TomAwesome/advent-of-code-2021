inputs = list(map(lambda x: x.replace('\n', ''), open("day3input.txt").readlines()))

zeroCounts = []
oneCounts = []

for i in range(len(inputs[0])):
    zeroCounts.append(0)
    oneCounts.append(0)

for bits in inputs:
    for i in range(len(bits)):
        if bits[i] == '0':
            zeroCounts[i] += 1
        else:
            oneCounts[i] += 1

gamaRateStr = ''
epsilonRateStr = ''

for i in range(len(zeroCounts)):
    if zeroCounts[i] > oneCounts[i]:
        gamaRateStr += '0'
        epsilonRateStr += '1'
    else:
        gamaRateStr += '1'
        epsilonRateStr += '0'

gamaRate = int(gamaRateStr, 2)
epsilonRate = int(epsilonRateStr, 2)

print(gamaRateStr)
print(epsilonRateStr)
print(gamaRate)
print(epsilonRate)

print(gamaRate * epsilonRate)

oxygenNumberOptions = inputs.copy()
co2NumberOptions = inputs.copy()

oxygenNumberStr = None
co2NumberStr = None
for i in range(len(oneCounts)):
    tempValues = []
    zeroCount = 0
    oneCount = 0
    for value in oxygenNumberOptions:
        if value[i] == '0':
            zeroCount += 1
        else:
            oneCount += 1
    for oxygenOption in oxygenNumberOptions:
        if oneCount >= zeroCount and oxygenOption[i] == '1':
            tempValues.append(oxygenOption)
        elif zeroCount> oneCount and oxygenOption[i] == '0':
            tempValues.append(oxygenOption)
    
    oxygenNumberOptions = tempValues.copy()

    if len(oxygenNumberOptions) == 1:
        oxygenNumberStr = oxygenNumberOptions[0]
        break

for i in range(len(zeroCounts)):
    tempValues = []
    tempValues = []
    zeroCount = 0
    oneCount = 0
    for value in co2NumberOptions:
        if value[i] == '0':
            zeroCount += 1
        else:
            oneCount += 1
    for co2Option in co2NumberOptions:
        if zeroCount <= oneCount and co2Option[i] == '0':
            tempValues.append(co2Option)
        elif oneCount < zeroCount and co2Option[i] == '1':
            tempValues.append(co2Option)

    co2NumberOptions = tempValues.copy()
    if len(co2NumberOptions) == 1:
        co2NumberStr = co2NumberOptions[0]
        break


oxygen = int(oxygenNumberStr, 2)
co2 = int(co2NumberStr, 2)
print("\n\n")
print(oxygenNumberStr)
print(co2NumberStr)
print(oxygen)
print(co2)
print(co2 * oxygen)