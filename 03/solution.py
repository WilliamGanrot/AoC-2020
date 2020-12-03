rows = []
with open('input') as f:
    rows = f.read().splitlines() 



def getChatacterAtXY(x,y):
    return(rows[y][x]) #change possition of x, y to flip map

def calcRest():
    

for y, row in enumerate(rows):
    r = []
    for x, c in enumerate(row):
        r.append(getChatacterAtXY(x,y))

    print(r)
