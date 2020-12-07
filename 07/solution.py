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




def count_contained(src):
	tot = 0
	for rule in ruleMap[src]:
        
		tot = int(tot) +  int(rule[0]) * (1 + count_contained(rule[1]))

	return tot



def part2(color):
    t = 0

    for rule in ruleMap[color]:
        t = int(t) + int(rule[0]) * (1 + part2(rule[1]))

    return t

print("part1: " + str(part1()))
print("part2: " + str(part2('shiny gold bag')))
