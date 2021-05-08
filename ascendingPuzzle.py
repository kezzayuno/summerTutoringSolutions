import random


class Board:
    """
    Creates a Board object where the game will be played

    Methods:
        Public:
            Move()
            Win()
            str() -
                |   #   |   #   |   #   |
                |   #   |   #   |   #   |
                |   #   |   #   |   #   |

        Private:
            __BuildBoard()

    Attributes:
        self.__boardSize - list of x (row) and y (col) values
        self.__board - list
        self.__moveTile - tile with no value ('Move')
        self.__movePositionRow - int representing the board row
        self.__movePosition - int representing the position in the board row
    """
    def __init__(self, boardSizeX, boardSizeY):
        """
        Initializes board via private method: __BuildBoard() (fills the board), board represented as a list
        :param boardSizeX: amount of rows to create
        :param boardSizeY: amount of col to create
        """
        self.__boardSize = [boardSizeX, boardSizeY]
        self.__board = []
        self.__moveTile = None
        self.__movePositionRow = 0
        self.__movePosition = 0
        self.__BuildBoard()

    def __BuildBoard(self):
        """
        Builds board by filling it with tile nodes that hold specific values (random-order)
            - Create the table with the given x and y (i.e., row and col) values
            - At each row till the end of the row, a Tile is initialized in its corresponding spot
            - Uses Random module to pick  the tile's value (which is within the range of the board (dictated by board
            size)
            - No unique tile values
            - Finds the max tile value (X * Y of the board) and replaces it with "Move" value
                - Caches row's position and the position in the row
        """
        unique = []
        for x in range(self.__boardSize[0]):
            for y in range(self.__boardSize[1]):
                newTile = Tile(random.randint(1, self.__boardSize[0] * self.__boardSize[1]))
                new = False
                while not new:
                    if newTile.getNode() in unique:
                        newTile = Tile(random.randint(1, self.__boardSize[0] * self.__boardSize[1]))
                    else:
                        new = True
                if y == 0:  # only add the head to the board
                    self.__board.append(newTile)
                else:  # in-between (will be the last row being made)
                    oldLast = self.__board[len(self.__board) - 1]
                    while oldLast.getNext() is not None:
                        oldLast = oldLast.getNext()
                    # after reaching the end and reaching the last node (which is saved as oldLast)
                    newTile.setPrevious(oldLast)
                    oldLast.setNext(newTile)
                unique.append(newTile.getNode())
        found = False
        n = 0
        while not found:
            current = self.__board[n]
            i = 0
            while current is not None and not found:
                if current.getNode() == self.__boardSize[0] * self.__boardSize[1]:
                    found = True
                    self.__moveTile = current
                    current.setValue('Move')
                    self.__movePositionRow = n  # row blank is located
                else:
                    current = current.getNext()
                    i += 1
            if not found:
                n += 1
            else:
                self.__movePosition = i  # position in the row where blank is located

    def Move(self, direction):
        """
        Moves the Move tile in order to move around the surrounding numbers
            Note: uses a WASD format to move the Move Tile
            Note: if player tries to go out of bounds of the board, an exception will be raised
        :param direction: player's choice for directional movement
        """
        try:
            if direction == 'a':
                prev = self.__moveTile.getPrev()
                self.__moveTile.setValue(prev.getNode())
                prev.setValue('Move')
                self.__moveTile = prev
                self.__movePosition -= 1
            elif direction == 'd':
                next = self.__moveTile.getNext()
                self.__moveTile.setValue(next.getNode())
                next.setValue('Move')
                self.__moveTile = next
                self.__movePosition += 1
            elif direction == 's':
                if self.__movePositionRow + 1 == len(self.__board):  # if on the bottom row, can't go down
                    raise IndexError
                i = 0
                current = self.__board[self.__movePositionRow + 1]
                while i != self.__movePosition:
                    current = current.getNext()
                    i += 1
                # when current is under the blank space
                self.__moveTile.setValue(current.getNode())
                current.setValue('Move')
                self.__moveTile = current
                self.__movePositionRow += 1
            elif direction == 'w':
                if self.__movePositionRow - 1 == -1:  # if on the top row, can't go up
                    raise IndexError
                i = 0
                current = self.__board[self.__movePositionRow - 1]
                while i != self.__movePosition:
                    current = current.getNext()
                    i += 1
                # when current is above the blank space
                self.__moveTile.setValue(current.getNode())
                current.setValue('Move')
                self.__moveTile = current
                self.__movePositionRow -= 1
        except (AttributeError, IndexError):
            print("Unfortunately you cannot go in this direction. Please pick a new choice.")

    def Win(self):
        """
        Checks if there is a win with a certain set of win conditions:
            - Checks if Move tile in the correct position (the most bottom right position)
            - Checks if the row is in ascending order
            - Checks if row's end value is in ascending order according to the first value of the next row
        :return: bool that indicates whether there is a win or not (False - Win Violated, True - Win Satisfied)
        """
        current = self.__board[len(self.__board) - 1]   # checks the last row, if Move is in the right position
        i = 0
        while current is not None:
            if i == self.__boardSize[1] - 1 and type(current.getNode()) != str:
                # if reached the end, and Move is not in place
                return False
            else:  # continue to check the whole row til the end
                current = current.getNext()
                i += 1
        endRow = None
        win = False
        for row in range(len(self.__board)):
            if endRow is not None:  # only occurs when going into the rows preceding the first row
                if type(self.__board[row].getNode()) == str:
                    return False
                elif endRow.getNode() != self.__board[row].getNode() - 1:
                    # checks if last row's last element is less than head of next
                    return False
            # if that is true, proceed to check the row
            current = self.__board[row]
            while current.getNext() is not None and not win:  # goes till out of bounds
                if not type(current.getNext().getNode()) == str:
                    if current.getNode() != current.getNext().getNode() - 1:
                        # checks if row is in ascending order
                        return False
                    else:
                        current = current.getNext()
                else:
                    if row == len(self.__board) - 1:
                        win = True
            endRow = current  # by the end of the row, this should be the last element of the row
        return win

    def __str__(self):
        """
        :return: str representation of the game board (row displayed as "|   #   |   #   |   #   |")
        """
        boardStr = ""
        for row in self.__board:
            boardStr += "|"
            current = row
            while current is not None:
                boardStr += '  {:^4} |'.format(str(current))
                current = current.getNext()
            boardStr += '\n'
        return boardStr


class Tile:
    """
    Tiles represented as nodes with links to its next and previous nodes

    Methods:
        Get Methods:
            getNext()
            getPrev()
            getNode()
        Set Methods:
            setValue(newValue)
            setNext(nextNode)
            setPrevious(prevNode)
        str() - node's value

    Attributes:
        self.__node - node initialized with a given value
        self.__previousNode - self node's previous node
        self.__nextNode - self node's next node
    """
    def __init__(self, numberNode):
        """
        Initializes tiles as nodes with a value (accompanied by previous and next nodes as None)
        :param numberNode: node's value
        """
        self.__node = numberNode
        self.__previousNode = None
        self.__nextNode = None

    # get methods
    def getNext(self):
        """
        :return: self node's next node's value
        """
        return self.__nextNode

    def getPrev(self):
        """
        :return: self node's previous node's value
        """
        return self.__previousNode

    def getNode(self):
        """
        :return: node's value
        """
        return self.__node

    # set methods
    def setValue(self, newValue):
        """
        :param newValue: new value that replaces old node value
        """
        self.__node = newValue

    def setNext(self, nextNode):
        """
        :param nextNode: new next node to the self node
        """
        self.__nextNode = nextNode

    def setPrevious(self, prevNode):
        """
        :param prevNode: new previous node to the self node
        """
        self.__previousNode = prevNode

    def __str__(self):
        """
        :return: str representation of the node (which is the node's value)
        """
        return str(self.__node)


def main():
    print("Welcome to the Number Sort Game!\nGoal: Please try to sort a given table in ascending order\n")
    scaleX = input('How many rows would you like to play on? > ')
    scaleY = input('How many columns would you like to play on? > ')
    game = Board(int(scaleX), int(scaleY))
    startLine = 'This is the starting condition of the game:'
    border = "{}".format('-' * len(startLine))
    print("\n{}\n{}{}".format(startLine, game, border))
    quit = False
    while not game.Win() and not quit:
        print("If you would like to quit, type in q (quit).")
        choice = input("Please move tiles by moving Move tile (w = up, a = left, s = down, d = right) > ")
        if choice == 'q':
            quit = True
        else:
            game.Move(choice)
            print(game)
    if not quit:
        print("Hooray! You won! Thank you for playing. Goodbye...")
        input("Press any key to quit")
    else:
        print("\nI'm sorry you had to go. Goodbye...")
        input("Press any key to quit")


main()
