
""" 
Stores gamestate and move logs of current game. Retrieves moves from evaluation. 

"""

import numpy as np


class GameState():
    def __init__(self):
        # board[y][x] where x is the vertical axis of the chess board 0-7 and y is the horizontal axis A-H (0-7)
        self.board = np.array([['wR', 'wN', 'wB', 'wQ', 'wK', 'wB', 'wN', 'wR'],
                               ['wP', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP'],
                               ['-', '-', '-', '-', '-', '-', '-', '-'],
                               ['-', '-', '-', '-', '-', '-', '-', '-'],
                               ['-', '-', '-', '-', '-', '-', '-', '-'],
                               ['-', '-', '-', '-', '-', '-', '-', '-'],
                               ['bP', 'bP', 'bP', 'bP', 'bP', 'bP', 'bP', 'bP'],
                               ['bR', 'bN', 'bB', 'bQ', 'bK', 'bB', 'bN', 'bR']])
        
        self.log = {'White':[], 'Black':[]}
        
        
        