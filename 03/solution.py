rows = []
with open('input') as f:
    rows = f.read().splitlines() 
length = len(rows[0])


def slope(paths):
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



  
slope([[3,1]])
slope([[1,1], [3,1], [5,1], [7,1], [1,2]])

 