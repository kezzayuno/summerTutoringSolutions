board = []
for row in range(4):
    row = []
    for col in range(3):
        row.append(col)
    board.append(row)

for row in board:
    for col in row:
        print('  '  + str(col) + '  ', end='')
    print()