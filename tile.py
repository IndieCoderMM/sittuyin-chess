from utils import COLORS, SQSIZE, PIECES_IMG, MARGIN

import pygame
import chess

class Tile:
    SIZE = SQSIZE

    def __init__(self, rank, file):
        self.rank = rank
        self.file = file
        self.x = MARGIN + (self.file * self.SIZE)
        self.y = MARGIN + ((7 - self.rank) * self.SIZE)
        self.rect = (self.x + 2, self.y + 2, self.SIZE-3, self.SIZE-3)
        self.square = chess.square(file, rank)
        self.name = chess.SQUARE_NAMES[self.square]
        self.highlighted = False
        self.selected = False

    def drawSquare(self, win, checked=False):
        if self.highlighted:
            pygame.draw.rect(win, COLORS['y'], self.rect, 3)
        # TODO Selected tile should be highlighted
        elif self.selected:
            pygame.draw.rect(win, COLORS['g'], self.rect, 3)
        if checked:
            pygame.draw.rect(win, COLORS['r'], self.rect)
        # else:
        #     pygame.draw.rect(win, COLORS['r'], self.rect)

    def drawPiece(self, piece, win):
        win.blit(PIECES_IMG[piece.symbol()], (self.x, self.y))
