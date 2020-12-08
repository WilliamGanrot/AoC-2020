


def getAccAfterTermination(instructions):
    accumulator = 0
    pointer = 0
    visited = []

    while pointer not in visited and pointer != len(instructions):
        visited.append(pointer)

        if instructions[pointer][0] == "acc":
            accumulator += int(instructions[pointer][1])
            pointer += 1
        elif instructions[pointer][0] == "jmp":
            pointer += int(instructions[pointer][1])
        elif instructions[pointer][0] == "nop":
            pointer += 1
    
    return (accumulator, (pointer == len(instructions)))


        
    

def part2(instructions):
    current_index = 0

    for i, instruction in enumerate(instructions):
        operation = instruction[0]
        
        if operation in ['jmp', 'nop']:

            if instructions[i][0] == "jmp":
                instructions[i][0] = "nop"
                acc, res = getAccAfterTermination(instructions)
                instructions[i][0] = "jmp"
                if res:
                    return acc
            elif instructions[i][0] == "nop":
                instructions[i][0] = "jmp"
                acc, res = getAccAfterTermination(instructions)
                instructions[i][0] = "nop"
                if res:
                    return acc





with open('input.txt') as f:
    instuctions = f.readlines()
    instuctions = [instuction.replace('\n', '').split(' ') for instuction in instuctions]
    
    print("part1: " + str(getAccAfterTermination(instuctions)))
    print("part2: " + str(part2(instuctions)))