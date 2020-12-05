import re

def hasAllFlags(fields):
    flags = [x[0] for x in fields]
    return all(x in flags for x in requiredFields)

def validateFlags(fields):
    for field in fields:        
        flag, value = field[0], field[1]
        print(field)

        if flag == 'byr':
            if not (value.isdigit() and len(value) == 4 and int(value) >= 1920 and int(value) <= 2002):
                return False
        elif flag == 'iyr':
            if not (value.isdigit() and len(value) == 4 and int(value) >= 2010 and int(value) <= 2020):
                return False
        elif flag == 'eyr':
            if not (value.isdigit() and len(value) == 4 and int(value) >= 2020 and int(value) <= 2030):
                return False
        elif flag == 'hgt':
            if not (value[:-2].isdigit() and ((value[-2:] == "cm" and 150 <= int(value[:-2]) <= 193) or(value[-2:] == "in" and 59 <= int(value[:-2]) <= 76))):
                return False       
        elif flag == 'hcl':
            if not (value[0] == '#' and len(value[1:]) == 6 and re.compile("[a-f0-9]+").fullmatch(value[1:]) != None):
                return False
        elif flag == 'ecl':
            if not (value in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']):
                return False
        elif flag == 'pid':
            if not (value.isdigit() and len(value) == 9):
                return False
        elif flag == 'cid':
            pass
           
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

        if hasAllFlags(fields) and validateFlags(fields):
            validPassports += 1

    return validPassports

rows = []
requiredFields = ['byr','iyr','eyr','hgt','hcl','ecl','pid']

with open('input.txt') as f:
    rows = f.read().split('\n\n')
    rows = [row.replace('\n', ' ').split(' ') for row in rows]
 
print("part1: " + str(part1(rows)))
print("part2: " + str(part2(rows)))