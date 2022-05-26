from tile import Tile
from utils import BOARDWIDTH, COLORS, MARGIN, SQSIZE

import chess
import pygame


class Board(chess.Board):
    BGCOLOR = COLORS['l']
    BOARDSIZE = BOARDWIDTH

    def __init__(self, win, *args):
        super().__init__(*args)
        self.window = win
        self.rect = pygame.Rect(MARGIN - 1, MARGIN - 1, self.BOARDSIZE + 5, self.BOARDSIZE + 5)
        self.squares = []
        self.moving = False
        self.selected_tile = None
        self.pending_move = []
        self._makeTiles()

    def _makeTiles(self):
        for file in range(8):
            for rank in range(8):
                tile = Tile(rank, file)
                self.squares.append(tile)

    def UpdateDisplay(self):
        self.window.fill(COLORS['b'])
        pygame.draw.rect(self.window, self.BGCOLOR, self.rect)

        pygame.draw.line(self.window, COLORS['pi'], (MARGIN, MARGIN), (MARGIN + self.BOARDSIZE, MARGIN + self.BOARDSIZE),
                         3)
        pygame.draw.line(self.window, COLORS['pi'], (MARGIN + self.BOARDSIZE, MARGIN), (MARGIN, MARGIN + self.BOARDSIZE),
                         3)
        pygame.draw.rect(self.window, COLORS['d'], self.rect, 5)

        for tile in self.squares:
            tile.highlighted = False
            if self.moving and tile.name in self.AvailableSquares():
                tile.highlighted = True
            tile.drawSquare(self.window)
            if tile.square == self.king(self.turn) and self.is_check():
                tile.drawSquare(self.window, True)
            piece = self.piece_at(tile.square)
            # Get Piece object from square
            if piece is not None:
                tile.drawPiece(piece, self.window)

        for i in range(8):
            pygame.draw.line(self.window, COLORS['d'], (MARGIN, MARGIN+SQSIZE*(i+1)),
                             (MARGIN + self.BOARDSIZE, MARGIN+SQSIZE*(i+1)), 3)
            pygame.draw.line(self.window, COLORS['d'], (MARGIN + SQSIZE * (i + 1), MARGIN),
                             (MARGIN + SQSIZE * (i + 1), MARGIN + self.BOARDSIZE), 3)

    def AvailableSquares(self):
        """
        :return: Legal squares for selected piece to highlight
        """
        # legal_moves = (str(move) for move in self.legal_moves)
        available_moves = [move[2:] for move in self.SittuyinMoves() if
                           move[:2] == self.pending_move[0]]
        return available_moves

    def TargetedSquares(self):
        pass

    def SittuyinMoves(self):
        """
        :return: Valid Move objects that correspond to selected piece
        """
        selected_piece = self.piece_at(self.selected_tile.square) if self.selected_tile else None
        if selected_piece is None:
            return

        sittuyin_moves = []
        pseudo_legal_moves = [str(move) for move in self.legal_moves]

        rank = chess.square_rank(self.selected_tile.square)
        file = chess.square_file(self.selected_tile.square)

        legal_squares = [(rank, file) for rank in range(8) for file in range(8)]
        # if selected_piece.symbol() in 'qQbB':
        #     # legal_squares = [(rank + 1, file - 1), (rank + 1, file + 1), (rank - 1, file - 1), (rank - 1, file + 1)]
        #
        #     if self.turn == chess.WHITE and selected_piece.symbol() == 'B':
        #         head_tile = (rank + 1, file)
        #         for tile in self.squares:
        #             if (tile.rank, tile.file) == head_tile:
        #                 if self.color_at(tile.square) == chess.WHITE:
        #                     break
        #                 # TODO Validate discover check !
        #                 legal_squares.append(head_tile)
        #                 sittuyin_moves.append(self.selected_tile.name + tile.name)
        #
        #     if self.turn == chess.BLACK and selected_piece.symbol() == 'b':
        #         head_tile = (rank - 1, file)
        #         for tile in self.squares:
        #             if (tile.rank, tile.file) == head_tile:
        #                 if self.color_at(tile.square) == chess.BLACK:
        #                     break
        #                 legal_squares.append(head_tile)
        #                 sittuyin_moves.append(self.selected_tile.name + tile.name)

        # Remove all squares that are not in legal squares for special pieces
        for tile in self.squares:
            if (tile.rank, tile.file) not in legal_squares:
                move = self.selected_tile.name + tile.name
                if move in pseudo_legal_moves:
                    pseudo_legal_moves.remove(move)

        sittuyin_moves += pseudo_legal_moves

        return [move for move in sittuyin_moves if move[:2] == self.selected_tile.name]

    def MoveReady(self, tile):
        """
        :param tile: User selected Tile object
        :return: Whether a move can be made from selected tiles
        """
        if not self.moving and not self.piece_at(tile.square):
            return None
        if not self.moving:
            self.moving = True
            self.selected_tile = tile
            self.selected_tile.selected = True
        else:
            self.moving = False
        self.pending_move.append(tile.name)
        return len(self.pending_move) == 2

    def MovePiece(self, tile):
        """
        Make a move on board if it is legal
        """
        if not self.MoveReady(tile):
            return

        move = ''.join(self.pending_move)
        if move in self.SittuyinMoves():
            self.push(self.parse_uci(move))
            print("Moving...", move)

            # for move in self.move_stack:
            #     print(move)
        else:
            print("Invalid Move! ", self.pending_move)
        self.pending_move = []
        self.selected_tile.selected = False

    def GetSelectedSquare(self, x, y):
        """
        :param x: Mouse position-x
        :param y: Mouse position-y
        :return: User-clicked Tile object
        """
        for tile in self.squares:
            if pygame.Rect(tile.x, tile.y, tile.SIZE, tile.SIZE).collidepoint(x, y):
                return tile
        return None

# TODO Pawn promotion
# TODO Indicate Check
# TODO UI
