ruleMap = {}
with open('input.txt') as f:
    rules = f.readlines()
    rules = [rule.replace('contain',',').replace('bags', 'bag').replace('.', '').strip().split(', ') for rule in rules]

    for rule in rules:
        key, definition = rule[0].rstrip(),rule[1:]
        ruleMap[key] = [d.lstrip().split(" ",1) for d in definition if d != 'no other bag']
        
        
def getBagHiarchy(rules, l):
    rulesWithoutNumber = [d[1] for d in rules]
    l.append(rulesWithoutNumber)
    
    for r in rulesWithoutNumber:
        getBagHiarchy(ruleMap[r], l)
    
    return l

def part1():
    c = 0
    for key in ruleMap:
        bagHiarchy = getBagHiarchy(ruleMap[key], [])
        flattenBagHiarchy = [item for sublist in bagHiarchy for item in sublist]
        if 'shiny gold bag' in flattenBagHiarchy:
            c += 1
    return c


def x(color):
    if not ruleMap[color]:
        return 1
    else:
        return sum([int(number)*x(bag) for number, bag in ruleMap[color]]) + 1 

    return 
def part2():
    #print(getGoldBagHiarchy('shiny gold bag'))
    print(x('shiny gold bag'))

#print("part1: " + str(part1()))
str(part2())
