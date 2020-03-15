#!/usr/bin/python
from copy import deepcopy
import sys

# A dear friend of mine posted a puzzle: how many possible games of tic tac toe are there?
# I figured there are probably mathematical ways of calculating them, but why not just
# count them? I took the opportunity to play around with recursion.

# By the time we're counting tic tac toe games, we might as well count the results.
# A global doesn't carry much risk in 50 lines of code and it keeps recursion clean
wins = { "X" : 0, "O" : 0, "cats" : 0 }

def main():
	board = [ [0,0,0], [0,0,0] , [0,0,0] ] #A 3x3 array represents a Tic Tac Toe board nicely.
	takeTurn (board,"X") #X moves first. This function recurses through all possible games.

	#Print the results.
	print "Possible tic-tac-toe games: " + str(wins["X"] + wins["O"] + wins["cats"])	
	print "Won by " + str(wins)
	print	

# A Tic Tac Toe board is passed in along with whose turn it is. That player then takes a move in every
# open square, checking each one to see if it ends the game. If it doesn't, the player then passes each
# possible board state to their opponent to go through the same process. 	
def takeTurn(oldBoard,activePlayer):
	# I want to pass the new board in by value so as to allow the calling function to contiue from its
	# board state. Passing in 2D arrays by value doesn't really work, but this does.
	board=deepcopy(oldBoard)

	# Clear out the last player's memory of where they've played
	for row in range(3):
		for col in range(3):
			if board[row][col] == "P":
				board[row][col] = 0
	
	# Iterate through the board. For each square, place a mark
	# if it's empty. Check to see if that ends the game. If it
	# does, score it appropriately and mark that square played.
	# If it doesn't, initiate the next move. Upon returning from
	# the recursed play, mark that square played.

	for row in range(3):
		for column in range(3):
#			if not board[row][column]:
			if board[row][column] != "X" and board[row][column] != "O":
				board[row][column] = activePlayer
				status = checkGame(board,activePlayer)
				if status == "victory":					
					wins[activePlayer] += 1
					board[row][column] = "P"
				elif status == "cats":
					wins["cats"] += 1
				else:
					if activePlayer == "X":
						takeTurn(board,"O")
					else:
						takeTurn(board,"X")
					board[row][column] = "P"					

# Check to see if the game is over. If it is, return whether the current player won
# or if it's a cat's game.
def checkGame(board,activePlayer):
	status=0	# Assume the game isn't over until proven otherwise
	
	# Check to see if the current player has won in rows or columns 
	for row in range(3):
		if ( activePlayer 	== board[row][0]			\
									== board[row][1]			\
									== board[row][2]  or 	\

				activePlayer	== board[0][row]			\
									== board[1][row]			\
									== board[2][row] ):
			status = "victory"
	
	# Check to see if the current player has won on a diagonal
	if (	activePlayer == board[0][0] == board[1][1] == board[2][2] or \
			activePlayer == board[0][2] == board[1][1] == board[2][0]  ):
		status = "victory"
	
	# If the current player hasn't won, look through the board for a square that doesn't have an X
	# or an O on it. If you find one, the game continues, otherwise it's a cats game.
	if not status:
		status = "cats"
		for row in range(3):
			for column in range(3):
				if board[row][column] != "X" and board[row][column] != "O":
					status = 0
	
	return status
	
main()
