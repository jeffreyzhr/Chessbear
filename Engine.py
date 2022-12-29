
""" 
Stores gamestate and move logs of current game. Retrieves moves from evaluation. 

"""
import numpy as np
import chess

FEN_translation = {}

class GameState():
    height = 8
    width = 8
    
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
    
    def get_valid(piece, coord, gamestate):
        valid_moves = []
        colour = piece[0]
        piece = piece[1]
        y,x = coord
        
        if piece == 'R':
            include = True
            for i in range(y, GameState.height):
                curr = (i,x)
                if curr == coord or not include:
                    continue
                if gamestate.board[i][x] != '-':
                    include = False
                    if gamestate.board[i][x][0] != colour:
                        valid_moves.append(curr)
                    continue
                valid_moves.append(curr)
            include = True
            for i in range(y, -1, -1):
                curr = (i,x)
                if curr == coord or not include:
                    continue
                if gamestate.board[i][x] != '-':
                    include = False
                    if gamestate.board[i][x][0] != colour:
                        valid_moves.append(curr)
                    continue
                
                valid_moves.append(curr)
                
                
            
            include = True
            for j in range(x, GameState.width):
                curr = (y,j)
                if curr == coord or not include:
                    continue
                if gamestate.board[y][j] != '-':
                    include = False
                    if gamestate.board[y][j][0] != colour:
                        valid_moves.append(curr)
                    continue
                valid_moves.append(curr)
            include = True
            for j in range(x, -1, -1):
                curr = (y,j)
                if curr == coord or not include:
                    continue
                if gamestate.board[y][j] != '-':
                    include = False
                    if gamestate.board[y][j][0] != colour:
                        valid_moves.append(curr)
                    continue
                valid_moves.append(curr)
            
        
        
        return valid_moves
    
    def linearmoves(coord, max_dist):
        moves = []
        
        

        
            
        
    
    
        
        

class Evaluate():
    pass
        
        