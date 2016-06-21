try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
    simplegui.Frame._hide_status = True
from random import shuffle

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
    def __str__(self):
        return self.letter
class Bag:
    def __init__(self):
        self.bag = []

    def __str__(self):
        for line in self.bag:
            "\n"

    def add_to_bag(self, tile, quantity):
        for i in range(quantity):
            self.bag.append(tile)

    def initialize_bag(self):
        self.add_to_bag(Tile("A", 1), 9)
        self.add_to_bag(Tile("B", 3), 2)
        self.add_to_bag(Tile("C", 3), 2)
        self.add_to_bag(Tile("D", 2), 4)
        self.add_to_bag(Tile("E", 1), 12)
        self.add_to_bag(Tile("F", 4), 2)
        self.add_to_bag(Tile("G", 2), 3)
        self.add_to_bag(Tile("H", 4), 2)
        self.add_to_bag(Tile("I", 1), 9)
        self.add_to_bag(Tile("J", 1), 9)
        self.add_to_bag(Tile("K", 5), 1)
        self.add_to_bag(Tile("L", 1), 4)
        self.add_to_bag(Tile("M", 3), 2)
        self.add_to_bag(Tile("N", 1), 6)
        self.add_to_bag(Tile("O", 1), 8)
        self.add_to_bag(Tile("P", 3), 2)
        self.add_to_bag(Tile("Q", 10), 1)
        self.add_to_bag(Tile("R", 1), 6)
        self.add_to_bag(Tile("S", 1), 4)
        self.add_to_bag(Tile("T", 1), 6)
        self.add_to_bag(Tile("U", 1), 4)
        self.add_to_bag(Tile("V", 4), 2)
        self.add_to_bag(Tile("W", 4), 2)
        self.add_to_bag(Tile("X", 8), 1)
        self.add_to_bag(Tile("Y", 4), 2)
        self.add_to_bag(Tile("Z", 10), 1)
        shuffle(self.bag)
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

    def get_rack_str(self):
        return ", ".join(str(item) for item in self.rack)

    def get_rack_arr(self):
        return self.rack
class Player:
    def __init__(self, bag):
        self.name = ""
        self.rack = Rack(bag)

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def get_rack(self):
        return self.rack.get_rack_str()

class Board:
    def __init__(self):
        self.board = [[" 0 " for i in range(15)] for j in range(15)]
        self.add_premium_squares()
        self.board[7][7] = " * "

    def get_board(self):
        #Create evenly spaced table!
        board_str = ""
        board = list(self.board)
        for i in range(len(board)):
            board[i] ="| " + " | ".join(str(item) for item in board[i]) + " |"
        board_str = "\n|_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _|\n".join(board)

        return board_str

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

    def play_word(self, word, location, direction):
        direction.lower()
        word = word.upper()
        if direction == "right":
            for i in range(len(word)):
                self.board[location[0]][location[1]+i] = " " + word[i] + " "
        elif direction == "down":
            for i in range(len(word)):
                self.board[location[0]+i][location[1]] = " " + word[i] + " "
        else:
            print("Error: please enter a valid direction.")

def check_word(word, location, player):
    word = word.upper()
    #Check that the word is in the dictionary
    dictionary = open("dic.txt").read()
    if word not in dictionary:
        return "Please enter a valid dictionary word."
    for letter in word:
        if letter not in player.get_rack():
            return "You do not have the tiles for this word."
    if location[0] > 14 or location[1] > 14 or location[0] < 0 or location[1] < 0:
        return "Location out of bounds."
    return True

def turn(player, board):
    global round_number
    print("Round " + str(round_number) + ": " + player.get_name() + "'s turn \n")
    print(board.get_board())
    print("\n" + player.get_name() + "'s Letter Rack: " + player.rack.get_rack_str())
    word_to_play = raw_input("Word to play: ")
    location = raw_input("Location of first letter: (Please separate coordinates with a comma)")
    direction = raw_input("Direction of word (right or down): ")
    while (check_word(word_to_play, location, player)) != True:
        word_to_play = raw_input("Word to play: ")
        location = raw_input("Location of first letter: ")
        direction = raw_input("Direction of word (right or down): ")
        print (check_word(word_to_play, location, player))
    board.play_word(word_to_play, tuple(map(int,location.split(','))), direction)
    print(board.get_board())

def start_game():
    global round_number
    board = Board()

    bag = Bag()
    bag.initialize_bag()

    player1 = Player(bag)
    player2 = Player(bag)
    current_player = player1
    round_number = 1

    print("Welcome to Scrabble! Please enter the names of the players below.")
    player1.set_name(raw_input("Player 1: "))
    player2.set_name(raw_input("Player 2: "))
    print("Welcome " + player1.get_name() + " and " + player2.get_name() + "! Let's begin!")

    turn(current_player, board)
start_game()
