rows = []
with open('input') as f:
    rows = f.read().splitlines() 
length = len(rows[0])
    
def getX(y,right):
    '''
    x = right*y
    while x >= length:
        x = x - length
    '''
    print(str(right) + ' ' + str(y) + ' ' + str(((right*y)%length)))
    x=((right*y)%length)
    return x
        
def part1():
    right = 3
    c = 0

    #trees = [for y, row in enumerate(rows) if str(rows[y][getX(y)]) == '#']
    for y, row in enumerate(rows):
        print(((right*y)%3))
        if(str(rows[y][((right*y)%length)]) == '#'):
            c += 1

    print(c)

def part2():
    paths = [[1,1], [3,1], [5,1], [7,1], [1,2]]
    s = 1
    for path in paths:
        right = path[0]
        height = path[1]
        ctr = 0
        y=0
        x=0
        while y < len(rows):
            
            if rows[y][x] == '#':
                ctr += 1
            x = (x + right)% length
            y += height

        s *= ctr

    print(str(s))

    

  

#part1()
part2()