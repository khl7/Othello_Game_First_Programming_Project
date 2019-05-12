from board import Board
from stone import Stone
from game_controller import GameController

WIDTH = 600
HEIGHT = 600
board = Board()
stone = Stone(WIDTH)
gc = GameController(WIDTH, stone)
SPACING = WIDTH/8
DELAY = 40
POP_DELAY = 50

def setup():
    '''Set up the game'''
    size(WIDTH, HEIGHT)
    colorMode(RGB, 1)
    background(0, 0.7, 0)
    board.display(WIDTH)
    stone.start_stone()
    print('Player goes first')

def draw():
    '''While True loop that draws when conditions are met'''
    global DELAY
    global POP_DELAY

    if gc.counter % 2 != 0 and gc.double_move_counter != 2 and gc.double_move_counter !=3:
        DELAY -= 1
        if DELAY == 0:
            gc.ai_make_move()
            DELAY = 40
    if gc.double_move_counter == 2 and gc.double_move_counter != 3:
        POP_DELAY -= 1
        if POP_DELAY == 0:
            name = gc.get_player_name()
            gc.read_file('scores.txt')
            gc.save_to_txt(name)
            gc.double_move_counter == 3

def mousePressed():
    '''Get mouse's x and y coordinate'''
    for i in range(8):
        for j in range(8):
            if i == (mouseY//SPACING) and j == (mouseX//SPACING):
                gc.start_game(i,j)


