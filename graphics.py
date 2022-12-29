import pygame as p
import numpy as np
import Engine


"""
    Graphics driver for pygame. 
"""


WIDTH = HEIGHT = 512
BOARD_DIMENSION = 8
SQ_SIZE = HEIGHT // BOARD_DIMENSION
MAX_FPS = 15
IMAGE_DICT = {}

def load_images():
    pieces = ['wK', 'wQ', 'wB', 'wN', 'wR', 'wP', 'bK', 'bQ', 'bB', 'bN', 'bR', 'bP']
    for item in pieces:
        IMAGE_DICT[item] = p.transform.scale(p.image.load("images/" + item + ".png"), (SQ_SIZE, SQ_SIZE))

def main():
    p.init()
    window = p.display.set_mode((WIDTH, HEIGHT))
    p.display.set_caption('Chess Bear AI')
    clock = p.time.Clock()
    window.fill(p.Color("white"))
    repr = Engine.GameState()
    load_images()
    running = True
    drawboard(window)
    print(repr.board[0][0])
    
    
    while running:
        for event in p.event.get():
            if event.type == p.QUIT:
                running = False
        
            if event.type == p.MOUSEBUTTONDOWN:
                pos = p.mouse.get_pos()
                piece, coord = getpieceatpos(pos, repr.board)
                if piece != '-':
                    valid_moves = Engine.Movement.get_valid(piece, coord) #this should return a list of tuples (y,x)
                    
                    for move in valid_moves:
                        y,x = move
                        p.draw.circle(window, p.Color(250, 70, 130), (x*SQ_SIZE + SQ_SIZE//2,y*SQ_SIZE+ SQ_SIZE//2), SQ_SIZE//2, 7)
                
                
                
                
        drawpieces(window, repr.board)
        clock.tick(MAX_FPS)
        p.display.flip()




def drawpieces(screen, board):
    for y in range(BOARD_DIMENSION):
        for x in range(BOARD_DIMENSION):
            piece = board[y][x]
            if piece != '-':
                screen.blit(IMAGE_DICT[piece], p.Rect(x*SQ_SIZE, y*SQ_SIZE, SQ_SIZE, SQ_SIZE))
    
def drawboard(screen):
        col = [p.Color(240, 216, 192), p.Color(168, 121, 101)] # 1 = dark, 0 = light
        for y in range(BOARD_DIMENSION):
            for x in range(BOARD_DIMENSION):
                c = col[(y+x)%2]
                p.draw.rect(screen, c, p.Rect(x*SQ_SIZE, y*SQ_SIZE, SQ_SIZE, SQ_SIZE))

# returns type of piece (str) and board location (y,x)
def getpieceatpos(pos, board):
    x,y = pos
    row = x//SQ_SIZE
    col = y//SQ_SIZE
    return (board[col][row], (col, row))
    
    

if __name__ == "__main__":
    main()

        