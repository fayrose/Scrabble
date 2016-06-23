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
    """
    Class that allows for the creation of a tile. Initializes using an uppercase string of one letter,
    and an integer representing that letter's score.
    """
    def __init__(self, letter, score):
        self.letter = letter.upper()
        self.score = score

    def __str__(self):
        return self.letter

    def get_score():
        #Returns the tile's score value.
        return self.score

class Bag:
    """
    Creates the bag of all tiles that will be available during the game. Contains 98 letters and two blank tiles.
    Takes no arguments to initialize.
    """
    def __init__(self):
        self.bag = []
        self.initialize_bag()

    def __str__(self):
        for line in self.bag:
            "\n"

    def add_to_bag(self, tile, quantity):
        #Adds a certain quantity of a certain tile to the bag. Takes a tile and an integer quantity as arguments.
        for i in range(quantity):
            self.bag.append(tile)

    def initialize_bag(self):
        #Adds the intiial 100 tiles to the bag.
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
        #Removes a tile from the bag and returns it to the user. This is used for replenishing the rack.
        return self.bag.pop()

    def get_remaining_tiles(self):
        #Returns the number of tiles left in the bag.
        return len(self.bag)

class Rack:
    """
    Creates each player's 'dock', or 'hand'. Allows players to add, remove and replenish the number of tiles in their hand.
    """
    def __init__(self, bag):
        self.rack = []
        self.initialize(bag)

    def add_to_rack(self, bag):
        #Takes a tile from the bag and adds it to the player's rack.
        self.rack.append(bag.take_from_bag())

    def initialize(self, bag):
        #Adds the initial 7 tiles to the player's hand.
        for i in range(7):
            self.add_to_rack(bag)

    def get_rack_str(self):
        #Displays the user's rack in string form.
        return ", ".join(str(item) for item in self.rack)

    def get_rack_arr(self):
        #Returns the rack in the form of an array.
        return self.rack

    def remove_from_rack(self, tile):
        #Removes a tile from the rack (for example, when a tile is being played).
        self.rack.remove(tile)

    def get_rack_length(self):
        #Returns the number of tiles left in the rack.
        return len(self.rack)

    def replenish_rack(self):
        #Adds tiles to the rack after a turn such that the rack will have 7 tiles (assuming a proper number of tiles in the bag).
        while self.get_rack_length < 7:
            self.add_to_rack(bag)

class Player:
    """
    Creates an instance of a player. Initializes the player's rack, and allows you to set/get a player name.
    """
    def __init__(self, bag):
        self.name = ""
        self.rack = Rack(bag)

    def set_name(self, name):
        #Sets the player's name.
        self.name = name

    def get_name(self):
        #Gets the player's name.
        return self.name

    def get_rack(self):
        #Returns the player's rack.
        return self.rack.get_rack_str()

class Board:
    """
    Creates the scrabble board.
    """
    def __init__(self):
        self.board = [[" 0 " for i in range(15)] for j in range(15)]
        self.add_premium_squares()
        self.board[7][7] = " * "

    def get_board(self):
        #Returns the board in string form.
        board_str = "_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _\n"
        board = list(self.board)
        for i in range(len(board)):
            board[i] ="| " + " | ".join(str(item) for item in board[i]) + " |"
        board_str += "\n|_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _|\n".join(board)
        board_str += "\n_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _"
        return board_str

    def add_premium_squares(self):
        #Adds all of the premium squares that influence the word's score.
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
        #Allows you to play words, assuming that they have already been confirmed as valid.
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
        #Remove letters from rack

def check_word(word, location, player):
    #Checks the word to make sure that it is in the dictionary, and that the location falls within bounds.
    word = word.upper()
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
    #Begins a turn, by displaying the current board, getting the information to play a turn, and creates a recursive loop to allow the next person to play.
    global round_number, player1, player2
    print("Round " + str(round_number) + ": " + player.get_name() + "'s turn \n")
    print(board.get_board())
    print("\n" + player.get_name() + "'s Letter Rack: " + player.rack.get_rack_str())
    word_to_play = raw_input("Word to play: ")
    location = []
    location.append(int(raw_input("Column number: "))
    location.append(int(raw_input("Row number: ")))
    direction = raw_input("Direction of word (right or down): ")
    while (check_word(word_to_play, location, player)) != True:
        print (check_word(word_to_play, location, player))
        word_to_play = raw_input("Word to play: ")
        location = []
        location.append(int(raw_input("Column number: "))
        location.append(int(raw_input("Row number: ")))
        direction = raw_input("Direction of word (right or down): ")
    board.play_word(word_to_play, tuple(map(int,location.split(','))), direction)
    print(board.get_board())
    if player == player1:
        player = player2
        turn(player, board)
    elif player == player2:
        player = player1
        round_number += 1
        turn(player, board)
    #Implement scoring system

def start_game():
    #Begins the game and calls the turn function.
    global round_number, player1, player2
    board = Board()

    bag = Bag()

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
