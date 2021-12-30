#!/usr/bin/python2
from copy import deepcopy

wins = {"X": 0, "O": 0, "cats": 0}
nextPlayer = {"X": "O", "O": "X"}


def main():
    board = [
        ["-", "-", "-"],
        ["-", "-", "-"],
        ["-", "-", "-"],
    ]
    takeTurn(board, "X")
    printResults()
    return


def printResults():
    print "Total possible tic-tac-toe games: %d" % sum(wins.values())
    print "Games won by %s" % str(wins).strip("{}")
    print
    return


# A Tic Tac Toe board is passed in along with whose turn it is. That player then takes a move in every
# open square, checking each one to see if it ends the game. If it doesn't, the player then passes each
# possible board state to their opponent to go through the same process.


def takeTurn(oldBoard, activePlayer):
    board = deepcopy(oldBoard)

    # Clear out the last player's memory of where they've played
    for row in board:
        for spot in row:
            if spot == "P":
                spot = "-"

    # Iterate through the board. For each square, place a mark
    # if it's empty. Check to see if that ends the game. If it
    # does, score it appropriately and mark that square played.
    # If it doesn't, initiate the next move. Upon returning from
    # the recursed play, mark that square played.

    for row in range(3):
        for column in range(3):
            if board[row][column] not in "XO":
                board[row][column] = activePlayer
                gameOver = checkGame(board, activePlayer)
                if not gameOver:
                    takeTurn(board, nextPlayer[activePlayer])
                board[row][column] = "P"
    return


# Check to see if the game is over. If it is, return whether the current player won
# or if it's a cat's game.
def checkGame(board, activePlayer):
    victor = None

    # Check to see if the current player has won in rows or columns
    for row in range(3):
        if (
            activePlayer == board[row][0] == board[row][1] == board[row][2]
            or activePlayer == board[0][row] == board[1][row] == board[2][row]
        ):
            victor = activePlayer
        if (
            activePlayer == board[0][0] == board[1][1] == board[2][2]
            or activePlayer == board[0][2] == board[1][1] == board[2][0]
        ):
            victor = activePlayer

    if not victor:
        victor = "cats"
        for row in board:
            for spot in row:
                if spot not in "XO":
                    victor = None

    if victor:
        wins[victor] += 1

    return victor


if __name__ == "__main__":
    main()
