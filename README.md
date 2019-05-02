# Scrabble
Command line scrabble game written in python. 

## In order to run the game:
Please navigate to the correct folder in your file system, and run `python scrabble.py`.
Please ensure that you have `python` in your `PATH`, and that it refers to Python 3.5. This file will not run in Python 2.7.

## How to play:

The game is a multiplayer one, designed to be played by between 2 and 4 players on the computer.
At the game's initialization, you will be asked to designate a number of players within this range, as well as name each of the players.

From here, you will be able to see the scrabble board. The board has 15 rows, and 15 columns, each numbered from 0 to 14. 
The round number, current player's turn and the current player's rack of letters (each player's rack is made up of 7 tiles) will be displayed. You will then be able to create a word from these tiles and place it upon the board. There will also be a bag of 100 starter tiles in the background, which will replenish each player's rack of tiles as you use them. The first turn made by the first player *must* place their word on the center of the board: 7, 7. Afterwards, the player will be asked whether they would like their word to go down or right. Finally, assuming that all information was inputted correctly, and that the word is in the official scrabble dictionary, the user's total score will be displayed, as well as the new board, commencing the next player's turn.

Note: After the first turn, all plays must have at least one letter that interlock with previous words. 

If there are no words that you can think to create using your current tile rack, simply submit a blank word, and the computer will ask if you would like to skip your turn. However, after 6 skipped turns in a row (as a whole, not by one particular player), the game will come to an end. The game will also end if the bag runs out of tiles and a player has run out of tiles. 

When the game ends, all player's scores will be compared, and whomever has the most points will win!
