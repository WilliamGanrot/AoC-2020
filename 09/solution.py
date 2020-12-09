

def SumIsInCollection(targetSum, collection):
    for c1 in collection:
        for c2 in collection:
            if (c1 + c2) == targetSum and c1 != c2:
                return True
    return False

def findInvalidNumber(numbers, preamble):

    allNumbersAfterFirstPreamble = numbers[preamble:]
    for i, num in enumerate(allNumbersAfterFirstPreamble):
    
        numbersToLookIn = numbers[i:preamble+i]
        if not SumIsInCollection(num, numbersToLookIn):
            return num
    

def part2(numbers, invalidNumber):

    for i in range(len(numbers)):
        for j in range(i,len(numbers)):
            
            rangeToCheck = numbers[i:j]
            if sum(rangeToCheck) == invalidNumber:
                return min(rangeToCheck) + max(rangeToCheck)

with open('input.txt') as f:
    numbers = f.readlines()
    numbers = [int(number.replace('\n', '')) for number in numbers]
    preamble = 25
    
    invalidNumber = findInvalidNumber(numbers, preamble)
    print("part1 " + str(invalidNumber))
    print("part2 " + str(part2(numbers, invalidNumber)))