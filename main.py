from sittuyin.board import Board
from sittuyin.utils import GetBoardSetup
from sittuyin.gui import GUI
from engine import Engine

import pygame
import chess


def main():
    starting_fen = GetBoardSetup(rand=True)
    chessboard = Board(starting_fen)
    gui = GUI(chessboard)
    ai_player = Engine(chess.BLACK, 3)
    player = chess.WHITE

    running = True
    while running:
        if chessboard.turn == ai_player.color:
            engine_move = ai_player.evaluate_best_move(chessboard)
            chessboard.push(engine_move)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_r:
                    # Refresh the game
                    starting_fen = GetBoardSetup(rand=True)
                    chessboard = Board(starting_fen)
                    gui = GUI(chessboard)
                if event.key == pygame.K_e:
                    ai_player.evaluate_materials(chessboard)
            if event.type == pygame.MOUSEBUTTONUP:
                if chessboard.turn == player:
                    tile = gui.get_selected_square(event.pos)
                    if tile is not None:
                        chessboard.MovePieceTo(tile)

        gui.update_display()

    pygame.quit()


if __name__ == '__main__':
    main()
