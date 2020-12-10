
def part1(adapters):
    maxJoltage = max(adapters) + 3
    adapters.append(maxJoltage)
    diffrences = [0,0,0]
    currentRating = 0
    
    for adapter in adapters:
        #candidats = [a for a in adapters if a <= currentRating + 3 and a >= currentRating + 1]

        if adapter <= currentRating + 3 and adapter >= currentRating + 1:
            diffrences[adapter-currentRating-1] += 1
            currentRating = adapter

            
    return(diffrences[0]* diffrences[2])



def part2(adapters, rating, i):
    
    maxJoltage = max(adapters) + 3
    adapters.append(maxJoltage)
    candidats = [a for a in adapters if a <= rating + 3 and a >= rating + 1]
    
    if len(candidats) == 0:
        return adapters
    for candidat in candidats:
        i += 1
        adapters[i] = candidat
        x = part2(adapters[i:],candidat,i)
        print(adapters[:i] + x)
    
with open('input.txt') as f:
    adapters = f.readlines()
    adapters = sorted([int(adapter.replace('\n', '')) for adapter in adapters])
    part2(adapters, 0, 0)
    
 