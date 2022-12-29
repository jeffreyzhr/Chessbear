
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
                               ['-', '-', '-', '-', 'wK', '-', '-', '-'],
                               ['-', '-', '-', '-', '-', '-', '-', '-'],
                               ['wP', 'wP', 'wP', 'wP', '-', 'wP', 'wP', 'wP'],
                               ['wR', 'wN', 'wB', 'wQ', '-', 'wB', 'wN', 'wR']])
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

        if piece == 'R':
            valid_moves.extend(Movement.linearmoves(coord, colour, GameState.height, gamestate))
        
        if piece == 'K':
            valid_moves.extend(Movement.linearmoves(coord, colour, 2, gamestate))
        
        if piece == 'Q':
            valid_moves.extend(Movement.linearmoves(coord, colour, GameState.height, gamestate))
                   
            
        
        
        return valid_moves
    

    """
    This method calculates valid moves on a linear (rook movement) direction for chess pieces. Used for Rooks, Queens and Kings.
    Max_dist dictates maximum movement distance for each piece - 8 for R and Q, 1 for K
    """    
    def linearmoves(coord, colour, max_dist, gamestate): 
        y,x = coord
        valid_moves = []
        include = True
        for i in range(y, y+max_dist):
            curr = (i,x)
            if not Movement.withinboundaries(curr, gamestate):
                break
            if curr == coord or not include:
                continue
            if gamestate.board[i][x] != '-':
                include = False
                if gamestate.board[i][x][0] != colour: #this check, along with the 3 similar ones later, checks for possible captures
                    valid_moves.append(curr)
                continue
            valid_moves.append(curr)
        include = True
        for i in range(y, y-max_dist, -1):
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
        for j in range(x, x+max_dist):
            curr = (y,j)
            if not Movement.withinboundaries(curr, gamestate):
                break
            if curr == coord or not include:
                continue
            if gamestate.board[y][j] != '-':
                include = False
                if gamestate.board[y][j][0] != colour:
                    valid_moves.append(curr)
                continue
            valid_moves.append(curr)
        include = True
        for j in range(x, x-max_dist, -1):
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
    
    """
    This method calculates valid moves on a diagonal (bishop movement) direction for chess pieces. Used for bishops, Queens and Kings.
    Max_dist dictates maximum movement distance for each piece - 8 for B and Q, 1 for K
    """ 
    def diagonalmoves(coord, colour, max_dist, gamestate): 
        pass
    
    def withinboundaries(coord, gamestate):
        y,x = coord
        if y >= gamestate.height or x >= gamestate.width or y < 0 or x < 0:
            return False
        return True
        
        

        
            
        
    
    
        
        

class Evaluate():
    pass
        
        