passwordWithPolicy = []
with open('input') as f:
    passwordWithPolicy = f.read().splitlines() 

passwordWithPolicy = [i.split(':') for i in passwordWithPolicy]


result = []
for pair in passwordWithPolicy:
    policy = pair[0]
    password = pair[1]
    
    character = policy[len(policy) - 1]
    minApperance = int(policy[0 : policy.find('-')])
    maxApperance = int(policy[policy.find('-')+1 : policy.find(' ')])

    #print(policy + ' ' + str(minApperance) + ' ' + str(maxApperance))


    apperances = password.count(character)
    if(apperances <= maxApperance and apperances >= minApperance):
        result.append(password)

print(len(result))