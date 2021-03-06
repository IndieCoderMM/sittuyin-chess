from .utils import COLORS, WINWIDTH, MARGIN, TILESIZE, FPS, PIECES_IMG

import pygame
import os

class GUI:
    BOARDCOLOR = COLORS['l']

    def __init__(self, board):
        os.environ['SDL_VIDEO_CENTERED'] = '1'
        pygame.init()
        pygame.font.init()

        self.window = pygame.display.set_mode((WINWIDTH, WINWIDTH))
        self.clock = pygame.time.Clock()

        self.board = board
        pygame.display.set_caption("STY")

    def update_chessboard(self):
        self.draw_baseboard()

        for tile in self.board.squares:
            piece = self.board.piece_at(tile.square)
            # Change tile state for highlighting
            if tile.state != tile.SELECTED:
                tile.state = tile.NORMAL
                if tile.square == self.board.king(self.board.turn) and self.board.is_check():
                    tile.state = tile.CHECKED
                if self.board.moving and tile.name in self.board.AvailableSquares():
                    tile.state = tile.MOVABLE
                if tile.name in self.board.TargetedSquares():
                    tile.state = tile.CAPTURABLE
            self.highlight_tile(tile)
            if piece is not None:
                self.draw_piece(piece, tile)
            # Draw grid lines
            for i in range(8):
                pygame.draw.line(self.window, COLORS['d'], (MARGIN, MARGIN + TILESIZE * (i + 1)),
                                 (MARGIN + self.board.SIZE, MARGIN + TILESIZE * (i + 1)), 3)
                pygame.draw.line(self.window, COLORS['d'], (MARGIN + TILESIZE * (i + 1), MARGIN),
                                 (MARGIN + TILESIZE * (i + 1), MARGIN + self.board.SIZE), 3)

    def draw_baseboard(self):
        pygame.draw.rect(self.window, self.BOARDCOLOR, self.board.rect)

        pygame.draw.line(self.window, COLORS['m'], (MARGIN, MARGIN),
                         (MARGIN + self.board.SIZE, MARGIN + self.board.SIZE),
                         3)
        pygame.draw.line(self.window, COLORS['m'], (MARGIN + self.board.SIZE, MARGIN),
                         (MARGIN, MARGIN + self.board.SIZE),
                         3)
        pygame.draw.rect(self.window, COLORS['d'], self.board.rect, 5)

    def highlight_tile(self, tile):
        color = None
        if tile.state == tile.MOVABLE:
            color = COLORS['m']
        elif tile.state == tile.SELECTED:
            color = COLORS['y']
        elif tile.state == tile.CHECKED:
            color = COLORS['r']
        if tile.state == tile.CAPTURABLE:
            color = COLORS['c']
        if color:
            pygame.draw.rect(self.window, color, tile.rect, 3)

    def draw_piece(self, piece, tile):
        self.window.blit(PIECES_IMG[piece.symbol()], (tile.x, tile.y))

    def write_text(self, text, fontsize, pos, color=COLORS['w']):
        font = pygame.font.Font(None, fontsize)
        rendered_text = font.render(text, True, color)
        self.window.blit(rendered_text, pos)

    def get_selected_square(self, pos):
        """
        :param pos: XY position of the mouse click
        :return: User-clicked Tile object
        """
        x, y = pos
        for tile in self.board.squares:
            if pygame.Rect(tile.rect).collidepoint(x, y):
                return tile
        return None

    def update_display(self):
        self.window.fill(COLORS['b'])
        if self.board.turn:
            self.write_text("White to move...", 50, (100, 10))
        else:
            self.write_text("Black to move...", 50, (100, 10))
        self.update_chessboard()

        pygame.display.update()
        self.clock.tick(FPS)
