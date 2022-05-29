import chess
import random

class Royar:
    def __init__(self, turn):
        self.turn = turn

    def GetEngineMove(self, moves):
        rand_move = random.choice(moves)
        return rand_move
