"""
Scrabble Game
Classes:
Tile - keeps track of the tile letter and value
Rack - keeps track of the tiles in a player's letter rack
Bag - keeps track of the remaining tiles in the bag
Word - checks the validity of a word and its placement
Board - keeps track of the tiles' location on the board
"""

class Tile:
    def __init__(self, letter, score):
        self.letter = letter
        self.score = score

class Bag:
    def __init__(self):
        self.bag = []

    def add_to_bag(self, tile, quantity=1):
        for i in range(quantity):
            self.bag.append(tile)

    def initialize_bag(self):
        self.add_to_bag(Tile("A", 1, 9))
        self.add_to_bag(Tile("B", 3, 2))
        self.add_to_bag(Tile("C", 3, 2))
        self.add_to_bag(Tile("D", 2, 4))
        self.add_to_bag(Tile("E", 1, 12))
        self.add_to_bag(Tile("F", 4, 2))
        self.add_to_bag(Tile("G", 2, 3))
        self.add_to_bag(Tile("H", 4, 2))
        self.add_to_bag(Tile("I", 1, 9))
        self.add_to_bag(Tile("J", 1, 9))
        self.add_to_bag(Tile("K", 5, 1))
        self.add_to_bag(Tile("L", 1, 4))
        self.add_to_bag(Tile("M", 3, 2))
        self.add_to_bag(Tile("N", 1, 6))
        self.add_to_bag(Tile("O", 1, 8))
        self.add_to_bag(Tile("P", 3, 2))
        self.add_to_bag(Tile("Q", 10, 1))
        self.add_to_bag(Tile("R", 1, 6))
        self.add_to_bag(Tile("S", 1, 4))
        self.add_to_bag(Tile("T", 1, 6))
        self.add_to_bag(Tile("U", 1, 4))
        self.add_to_bag(Tile("V", 4, 2))
        self.add_to_bag(Tile("W", 4, 2))
        self.add_to_bag(Tile("X", 8, 1))
        self.add_to_bag(Tile("Y", 4, 2))
        self.add_to_bag(Tile("Z", 10, 1))

    def take_from_bag(self):
        return self.bag.pop()

class Rack:
    def __init__(self, bag):
        self.rack = []
        self.initialize(bag)

    def add_to_rack(self, bag):
        self.rack.append(bag.take_from_bag())

    def initialize(self, bag):
        for i in range(7):
            self.add_to_rack(bag)

class Board:
    def __init__(self):
        self.board = [[0 for i in range(15)] for j in range(15)]
        self.add_premium_squares()

    def print_board(self):
        for line in self.board:
            print(line)

    def add_premium_squares(self):
        TRIPLE_WORD_SCORE = ((0,0), (7, 0), (14,0), (0, 7), (14, 7), (0, 14), (7, 14), (14,14))
        DOUBLE_WORD_SCORE = ((1,1), (2,2), (3,3), (4,4), (1, 13), (2, 12), (3, 11), (4, 10), (13, 1), (12, 2), (11, 3), (10, 4), (13,13), (12, 12), (11,11), (10,10))
        TRIPLE_LETTER_SCORE = ((1,5), (1, 9), (5,1), (5,5), (5,9), (5,13), (9,1), (9,5), (9,9), (9,13), (13, 5), (13,9))
        DOUBLE_LETTER_SCORE = ((0, 3), (0,11), (2,6), (2,8), (3,0), (3,7), (3,14), (6,2), (6,6), (6,8), (6,12), (7,3), (7,11), (8,2), (8,6), (8,8), (8, 12), (11,0), (11,7), (11,14), (12,6), (12,8), (14, 3), (14, 11))

        for coordinate in TRIPLE_WORD_SCORE:
            self.board[coordinate[0]][coordinate[1]] = "TWS"
        for coordinate in TRIPLE_LETTER_SCORE:
            self.board[coordinate[0]][coordinate[1]] = "TLS"
        for coordinate in DOUBLE_WORD_SCORE:
            self.board[coordinate[0]][coordinate[1]] = "DWS"
        for coordinate in DOUBLE_LETTER_SCORE:
            self.board[coordinate[0]][coordinate[1]] = "DLS"
