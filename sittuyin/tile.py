from .utils import MARGIN, TILESIZE

import chess

class Tile:
    SIZE = TILESIZE
    NORMAL = 0
    CAPTURABLE = 1
    SELECTED = 3
    MOVABLE = 4
    CHECKED = 5

    def __init__(self, rank, file):
        self.rank = rank
        self.file = file
        self.x = MARGIN + (self.file * self.SIZE)
        self.y = MARGIN + ((7 - self.rank) * self.SIZE)
        self.rect = (self.x + 2, self.y + 2, self.SIZE-3, self.SIZE-3)
        self.square = chess.square(file, rank)
        self.name = chess.SQUARE_NAMES[self.square]
        self.state = self.NORMAL

