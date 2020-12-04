import re

def hasAllFlags(fields):
    flags = [x[0] for x in fields]
    return all(x in flags for x in requiredFields)

def validateFlag(fields):
    for field in fields:
        
        flag, value = field[0], field[1]

        if flag == 'byr':
            return value.isdigit() and len(value) == 4 and int(value) >= 1920 and int(value) <= 2020
        elif flag == 'iyr':
            return value.isdigit() and len(value) == 4 and int(value) >= 2010 and int(value) <= 2020
        elif flag == 'eyr':
            return value.isdigit() and len(value) == 4 and int(value) >= 2020 and int(value) <= 2030
        elif flag == 'hgt':
            if value.endswith('cm'):
                h = int(value[:-len('cm')])
                return h >= 150 and h <= 193 
            elif value.endswith('inc'): 
                h = int(value[:-len('cm')])
                return h >= 59 and h <= 76
            else:  
                return False
        elif flag == 'hcl':
            return value[0] == '#' and len(value[1:]) == 6 and re.compile("[a-f0-9]+").fullmatch(value[1:]) != None
        elif flag == 'ecl':
            return value in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
        elif flag == 'pid':
            return value[0] == 0 and len(value) == 9
        elif flag == 'cid':
            return True
           
    return True   

def part1(rows):
    validPassports = 0
    for passport in rows:
        flags = [field.split(':')[0] for field in passport]
        
        if all(x in flags for x in requiredFields):
            validPassports += 1
    return validPassports


def part2(rows):
    validPassports = 0
    for passport in rows:
        fields = [field.split(':') for field in passport]
       
        if hasAllFlags(fields) and validateFlag(fields):
            validPassports += 1
    return validPassports

rows = []
requiredFields = ['byr','iyr','eyr','hgt','hcl','ecl','pid']

with open('input.txt') as f:
    rows = f.read().split('\n\n')
    rows = [row.replace('\n', ' ').split(' ') for row in rows]
 
print(part2(rows))