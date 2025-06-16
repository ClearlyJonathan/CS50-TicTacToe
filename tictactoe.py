"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None

isXTurn = True

def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """

    xAmount = 0
    yAmount = 0
    for row in board:
        for col in row:
            if col == "X":
                xAmount += 1
            elif col == "O":
                yAmount += 1
    
    if xAmount == yAmount:
        return X
    if xAmount > yAmount:
        return O
    

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actionsThatCanBeTaken = set()
    for row in range(0,3):
        for col in range(0,3):
            if board[row][col] == None:
                actionsThatCanBeTaken.add((row, col))
    return actionsThatCanBeTaken


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    #print(action)
    #print(board)
    if action is None:
        print(f"Invalid action: {action}, board at that spot: {board}")
        raise NameError("Invalid Board")

    row = action[0]
    col = action[1]

    if row >= 3 or col >= 3 or row < 0 or col < 0:
        raise NameError("Out of bounds")
    modifiedBoard = copy.deepcopy(board)
    if action is None or modifiedBoard[row][col] is not None:
        print(f"Invalid action: {action}, board at that spot: {modifiedBoard[row][col]}")
        raise NameError("Invalid Board")
    
    modifiedBoard[row][col] = player(board)
    #print(modifiedBoard)
    return modifiedBoard


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # Check winner horizontal
    for row in board:
        if [row[0], row[1], row[2]] == ["X", "X", "X"]:
            return X
        elif [row[0], row[1], row[2]] == ["O", "O", "O"]:
            return O
    # Check winner vertical
    for col in range(3):
        if [board[0][col], board[1][col], board[2][col]] == ["X", "X", "X"]:
            return X
        elif [board[0][col], board[1][col], board[2][col]] == ["O", "O", "O"]:
            return O
        
    # Check diagonal
    if [board[0][0], board[1][1], board[2][2]] == ["X", "X", "X"]:
        return X
    elif [board[0][0], board[1][1], board[2][2]] == ["O", "O", "O"]:
        return O
    elif [board[0][2], board[1][1], board[2][0]] == ["X", "X", "X"]:
        return X
    elif [board[0][2], board[1][1], board[2][0]] ==["O", "O", "O"]:
        return O
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    # Someone has won
    if winner(board) is not None:
        return True
    # If there's no more possible actions then it's a tie and game is over
    if len(actions(board)) == 0:
        return True
    return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    elif winner(board) == None:
        return 0

def minimax(board):
    # Maximiziing player - Call minim to know what they will do
    # - If I take this action, what action can the minimizing player do to take the lowest value"
    if terminal(board):
        return None

    currentPlayer = player(board) # X max , O Min
    currentMax = -2
    currentMin = 2

    worstAction = None
    bestAction = None

    if currentPlayer == X:
        for action in actions(board):
            if MaxValue(result(board, action)) > currentMax:
                currentMax = MinValue(result(board, action))
                bestAction = action
        return bestAction
    elif currentPlayer == O:
        for action in actions(board):
            if MinValue(result(board, action)) < currentMin:
                currentMin = MaxValue(result(board, action))
                worstAction = action
        return worstAction



def MaxValue(board):
    v = -math.inf
    if terminal(board):
        return utility(board)
    
    for action in actions(board):
        v = max(v, MinValue(result(board, action)))
    return v

def MinValue(board):
    v = math.inf
    if terminal(board):
        return utility(board)
    
    for action in actions(board):
        v = min(v, MaxValue(result(board, action)))
    return v