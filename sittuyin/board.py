from .tile import Tile
from .utils import BOARDWIDTH, MARGIN

import chess


class Board(chess.Board):
    SIZE = BOARDWIDTH

    def __init__(self, *args):
        super().__init__(*args)
        self.rect = (MARGIN - 3, MARGIN - 3, self.SIZE + 4, self.SIZE + 4)
        self.squares = []
        self.moving = False
        self.selected_tile = None
        self.pending_move = []
        self._create_tiles()

    def _create_tiles(self):
        for file in range(8):
            for rank in range(8):
                tile = Tile(rank, file)
                self.squares.append(tile)

    def AvailableSquares(self):
        """
        :return: Legal squares for selected piece to highlight
        """
        return [move[2:] for move in self.GetLegalMoves() if move[:2] == self.pending_move[0]]

    def TargetedSquares(self):
        targets = []
        for tile in self.squares:
            piece = self.piece_at(tile.square)
            if piece is None:
                continue
            if tile.state == tile.MOVABLE:
                tile.state = tile.CAPTURABLE
                targets.append(tile.name)
        return targets

    def GetLegalMoves(self):
        """
        :return: Valid Move objects that correspond to selected piece
        """
        return [str(move) for move in self.legal_moves]

    def prepare_move(self, tile):
        if not self.moving:
            piece = self.piece_at(tile.square)
            if piece is None or piece.color != self.turn:
                return
            self.moving = True
            self.selected_tile = tile
            self.selected_tile.state = self.selected_tile.SELECTED
        else:
            self.moving = False
        self.pending_move.append(tile.name)

    def ready_to_move(self):
        return len(self.pending_move) == 2

    def MovePieceTo(self, tile):
        """
        Make a move on board if it is legal
        """
        self.prepare_move(tile)
        if not self.ready_to_move():
            return

        move = ''.join(self.pending_move)
        if move in self.GetLegalMoves():
            self.push(self.parse_uci(move))
            print("Moving...", move)
            # ai_move = evaluate_best_move(self.GetLegalMoves())
            # self.push(self.parse_uci(ai_move))
            # print("Moving...", ai_move)
        else:
            print("Invalid Move! ", self.pending_move)
        self.pending_move = []
        self.selected_tile.state = self.selected_tile.NORMAL

# TODO Pawn promotion
