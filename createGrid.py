board = []
for row in range(4):
    rowBoard = []
    for col in range(3):
        rowBoard.append(col)
    board.append(rowBoard)

for row in board:
    for col in row:
        print('  '  + str(col) + '  ', end='')
    print()