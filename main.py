from board import Board
from utils import GetBoardSetup
from gui import GUI
from engine import Royar

import pygame


def main():
    starting_fen = GetBoardSetup(rand=True)
    chessboard = Board(starting_fen)
    gui = GUI(chessboard)
    player = 1
    engine = Royar(not player)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_r:
                    # Refresh the game
                    starting_fen = GetBoardSetup(rand=True)
                    chessboard = Board(starting_fen)
            if event.type == pygame.MOUSEBUTTONUP:
                if chessboard.turn == player:
                    tile = gui.GetSelectedSquare(event.pos)
                    if tile is not None:
                        chessboard.MovePieceTo(tile)

        gui.UpdateDisplay()

    pygame.quit()


if __name__ == '__main__':
    main()
