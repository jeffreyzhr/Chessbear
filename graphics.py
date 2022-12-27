import pygame as p
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
    screen = p.display.set_mode((WIDTH, HEIGHT))
    clock = p.time.Clock()
    screen.fill(p.Color("white"))
    gamestate = Engine.GameState()
    load_images()
    running = True
    drawboard(screen)
    
    while running:
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False
        drawpieces(screen, gamestate.board)
        clock.tick(MAX_FPS)
        p.display.flip()

def drawpieces(screen, board):
    for y in range(BOARD_DIMENSION):
        for x in range(BOARD_DIMENSION):
            piece = board[y][x]
            if piece != '-':
                screen.blit(IMAGE_DICT[piece], p.Rect(x*SQ_SIZE, y*SQ_SIZE, SQ_SIZE, SQ_SIZE))
    
def drawboard(screen):
        col = [p.Color(196, 137, 26), p.Color('white')]
        for y in range(BOARD_DIMENSION):
            for x in range(BOARD_DIMENSION):
                c = col[(y+x)%2]
                print((y,x,c))
                p.draw.rect(screen, c, p.Rect(x*SQ_SIZE, y*SQ_SIZE, SQ_SIZE, SQ_SIZE))
    
    

if __name__ == "__main__":
    main()

        