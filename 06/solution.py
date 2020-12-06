import string

groups = []
with open('input') as f:
    groups = f.read().split('\n\n')
    groups = [group.split('\n') for group in groups]

def part1(group):
    yesAnswers = [answer for person in group for answer in person]
    distinctYesAnswers = list(''.join(set(yesAnswers)))
    return distinctYesAnswers

def part2(group):
    membersYesAnswers = [list(person) for person in group]
    commonYesAnswers = list(set(membersYesAnswers[0]).intersection(*membersYesAnswers))
    return commonYesAnswers

print("part1: " + str(sum([len(part1(group)) for group in groups])))
print("part2: " + str(sum([len(part2(group)) for group in groups])))
