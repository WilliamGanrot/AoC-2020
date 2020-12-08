


def getAccAfterTermination(instuctions):
    i = 0
    acc = 0
    visitedInstructionIndexes = []
    while i not in visitedInstructionIndexes:

        visitedInstructionIndexes.append(i)

        instuction = instuctions[i][0]
        value = int(instuctions[i][1])
        
        if instuction == 'nop':

            i += 1
        elif instuction == 'acc':

            acc += value
            i=i+1
        elif instuction == 'jmp':

            i += value
         
        if i > len(instuctions) - 1:
            return (acc,True)
            
    return (acc,False)



def part2(instuctions):
    current_index = 0
    acc = 0
    for i, instuction in enumerate(instuctions):
        operation = instuction[0]

        if operation in ['jmp', 'nop']:
            modified_instructions = instuctions
            if operation == 'jmp':
                modified_instructions[i][0] = 'nop'
            elif operation == 'nop':
                modified_instructions[i][0] = 'jmp'
            
            acc, program_fixed = getAccAfterTermination(modified_instructions)
            print(acc)
            if program_fixed:
                
                break
    
        
        


with open('input.txt') as f:
    instuctions = f.readlines()
    instuctions = [instuction.replace('\n', '').split(' ') for instuction in instuctions]
    
    #print("part1: " + str(getAccAfterTermination(instuctions)))
    part2(instuctions)