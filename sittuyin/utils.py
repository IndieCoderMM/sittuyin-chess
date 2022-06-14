import pygame
import random
import enum

class PieceValue(enum.Enum):
    PAWN = 1
    KNIGHT = 5
    ELEPHANT = 4
    GENERAL = 3
    ROOK = 8
    KING = 1000


WINWIDTH = 600
BOARDWIDTH = 500

MARGIN = WINWIDTH // 2 - BOARDWIDTH // 2

FPS = 30
WHITE = (255, 255, 255)
GREY = (128, 128, 128)
YELLOW = (227, 200, 0)
BLUE = (50, 25, 255)
BLACK = (0, 0, 0)
GREEN = (0, 171, 169)
LIME = (164, 196, 0)
RED = (229, 20, 0)
PURPLE = (170, 0, 225)
ORANGE = (211, 84, 0)
MAGNETO = (216, 0, 115)
CYAN = (27, 161, 226)
BROWN = (160, 82, 45)

COLORS = {
    'w': WHITE, 'd': BLACK, 'y': YELLOW,
    'g': GREEN, 'r': RED, 'p': PURPLE,
    'b': BLUE, 'o': ORANGE, 'm': MAGNETO,
    'c': CYAN, 'br': BROWN, 'l': LIME
}

TILESIZE = BOARDWIDTH // 8

w_king = pygame.transform.scale(pygame.image.load('assets/wk.png'), (TILESIZE, TILESIZE))
b_king = pygame.transform.scale(pygame.image.load('assets/bk.png'), (TILESIZE, TILESIZE))
w_queen = pygame.transform.scale(pygame.image.load('assets/wb.png'), (TILESIZE, TILESIZE))
b_queen = pygame.transform.scale(pygame.image.load('assets/bb.png'), (TILESIZE, TILESIZE))
w_bishop = pygame.transform.scale(pygame.image.load('assets/we.png'), (TILESIZE, TILESIZE))
b_bishop = pygame.transform.scale(pygame.image.load('assets/be.png'), (TILESIZE, TILESIZE))
w_knight = pygame.transform.scale(pygame.image.load('assets/wn.png'), (TILESIZE, TILESIZE))
b_knight = pygame.transform.scale(pygame.image.load('assets/bn.png'), (TILESIZE, TILESIZE))
w_rook = pygame.transform.scale(pygame.image.load('assets/wr.png'), (TILESIZE, TILESIZE))
b_rook = pygame.transform.scale(pygame.image.load('assets/br.png'), (TILESIZE, TILESIZE))
w_pawn = pygame.transform.scale(pygame.image.load('assets/wp.png'), (TILESIZE, TILESIZE))
b_pawn = pygame.transform.scale(pygame.image.load('assets/bp.png'), (TILESIZE, TILESIZE))

PIECES_IMG = {
    'K': w_king, 'k': b_king, 'Q': w_queen, 'q': b_queen, 'B': w_bishop, 'b': b_bishop,
    'N': w_knight, 'n': b_knight, 'R': w_rook, 'r': b_rook, 'P': w_pawn, 'p': b_pawn
}

DECK = {
    'kHide': '4PPPP/PPPPQN2/1BKBN3/5RR1',
    'nConnected': '4PPPP/PPPPQBN1/3BNK2/1RR5',
    'nSide': '4PPPP/PPPPQB2/2BNNK2/1R1R4',
    'nCross': '4PPPP/PPPPQNB1/3BN1K1/2R2R2',
    'nSandwich': '4PPPP/PPPPQB2/2NBNK2/1R1R4',
    'nBattery': '4PPPP/PPPPQNB1/3B1NK1/2R1R3',
    'eSide': '4PPPP/PPPPQBB1/3N1NK1/3R1R2',
    'gInside': '4PPPP/PPPPNQ2/1B2NB2/2RR1K2'
}

def GetBoardSetup(white=DECK['kHide'], black=DECK['nCross'], rand=False):
    """
    :param white: Setup for White
    :param black: Setup for Black
    :param rand: Create randomized setups for both
    :return: FEN string
    """
    if rand:
        white_pos = random.choice(list(DECK.keys()))
        black_pos = random.choice(list(DECK.keys()))
        white = DECK[white_pos]
        black = DECK[black_pos]
    black = black[::-1].lower()
    fen = black + '/' + white
    return fen + ' w - - 0 1'


