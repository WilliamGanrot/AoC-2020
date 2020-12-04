
def part1(rows):
    c = 0
    for passport in rows:
        flags = [flag.split(':')[0] for flag in passport]
        
        validPassport = all(x in flags for x in requiredFields)
        
        if validPassport:
            c += 1
      
    return c

rows = []
requiredFields = ['byr','iyr','eyr','hgt','hcl','ecl','pid']

with open('input.txt') as f:
    rows = f.read().split('\n\n')
    rows = [row.replace('\n', ' ').split(' ') for row in rows]
 
print(part1(rows))