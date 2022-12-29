
""" 
Stores gamestate and move logs of current game. Retrieves moves from evaluation. 

"""
import numpy as np

FEN_translation = {}

class GameState():
    def __init__(self):
        # board[y][x] where y is the vertical axis of the chess board 0-7 and x is the horizontal axis A-H (0-7)
        self.board = np.array([['bR', 'bN', 'bB', 'bQ', 'bK', 'bB', 'bN', 'bR'],
                               ['bP', 'bP', 'bP', 'bP', 'bP', 'bP', 'bP', 'bP'],
                               ['-', '-', '-', '-', '-', '-', '-', '-'],
                               ['-', '-', '-', '-', '-', '-', '-', '-'],
                               ['-', '-', '-', '-', '-', '-', '-', '-'],
                               ['-', '-', '-', '-', '-', '-', '-', '-'],
                               ['wP', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP'],
                               ['wR', 'wN', 'wB', 'wQ', 'wK', 'wB', 'wN', 'wR']])
        #self.board = np.empty([8,8])
        
        self.log = {'White':[], 'Black':[]}
        
    
    def update():
        pass
    
    def updateboardfromFen(input = str):
        pass


class Movement():
    
    def get_valid(piece, coord):
        valid_moves = [(0,1), (7,7), (0,3)]
        
        
        return valid_moves
    
    
        
        

class Evaluate():
    pass
        
        