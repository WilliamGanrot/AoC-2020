passwordWithPolicy = []
with open('input') as f:
    passwordWithPolicy = f.read().splitlines() 


result = []
for pair in passwordWithPolicy:
    
    policy, password = pair.strip().replace(" ", "").split(':')
    targetCharacter = policy[len(policy) - 1]
    
    minApperance = int(policy[0 : policy.find('-')])
    maxApperance = int(policy[policy.find('-')+1 : policy.find(' ')])

    apperances = password.count(targetCharacter)
    if(apperances <= maxApperance and apperances >= minApperance):
        result.append(password)

print("Part1: " + str(len(result)))

result = []
for pair in passwordWithPolicy:  
    
    policy, password = pair.strip().replace(" ", "").split(':')
    targetCharacter = policy[len(policy) - 1]
    
    lowIndex = int(policy[0 : policy.find('-')]) - 1
    highIndex = int(policy[policy.find('-')+1 : policy.find(' ')]) - 1

    if((password[lowIndex] == targetCharacter or password[highIndex] == targetCharacter) and password[lowIndex] is not password[highIndex]):
        result.append(password)

print("Part2: " + str(len(result)))