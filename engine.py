from sittuyin.utils import PieceValue

class Engine:
    def __init__(self, color, level):
        self.color = color
        self.level = level

    def evaluate_best_move(self, board):
        return self.minimax(board, self.level, True)[1]

    def get_piece_value(self, piece):
        value = 0
        factor = -1 if piece.color != self.color else 1
        piece_type = piece.piece_type
        if piece_type == 1:
            value = PieceValue.PAWN.value
        elif piece_type == 2:
            value = PieceValue.KNIGHT.value
        elif piece_type == 3:
            value = PieceValue.ELEPHANT.value
        elif piece_type == 4:
            value = PieceValue.ROOK.value
        elif piece_type == 5:
            value = PieceValue.GENERAL.value
        elif piece_type == 6:
            value = PieceValue.KING.value
        return factor * value

    def evaluate_materials(self, board):
        evaluation = 0
        for tile in board.squares:
            piece = board.piece_at(tile.square)
            if piece is None:
                continue
            evaluation += self.get_piece_value(piece)
        return evaluation

    def minimax(self, board, depth, ai_turn):
        print("thinking...")
        if depth == 0 or board.is_game_over():
            return self.evaluate_materials(board), board.peek()
        if ai_turn:
            max_eval = float('-inf')
            best_move = None
            for move in board.GetLegalMoves():
                board.push(board.parse_uci(move))
                eval_ = self.minimax(board, depth-1, False)[0]
                max_eval = max(max_eval, eval_)
                move = board.pop()
                if max_eval == eval_:
                    best_move = move
            return max_eval, best_move
        else:
            min_eval = float('+inf')
            best_move = None
            for move in board.GetLegalMoves():
                board.push(board.parse_uci(move))
                eval_ = self.minimax(board, depth - 1, True)[0]
                min_eval = min(min_eval, eval_)
                move = board.pop()
                if min_eval == eval_:
                    best_move = move
            return min_eval, best_move

