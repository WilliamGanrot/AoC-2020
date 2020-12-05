tickets = []
with open('input') as f:
    tickets = f.read().splitlines() 

def getTicketId(ticket):
    binaryRow = ticket[0:7].replace('F','0'). replace('B','1')
    binaryCol = ticket[7:10].replace('R','1'). replace('L','0')

    row = int(binaryRow, 2)
    col = int(binaryCol, 2) 

    return (row*8)+col

def part2(tickets):
    allSeats = list(range(0, 128*8))
    missingSeats = list(set(allSeats) - set(tickets))

    mySeat = [seat for seat in missingSeats if seat-1 not in missingSeats and seat+1 not in missingSeats]
    return mySeat[0]

print("part1: " + str(max([getTicketId(ticket) for ticket in tickets])))
print("part2: " + str(part2([getTicketId(ticket) for ticket in tickets])))
