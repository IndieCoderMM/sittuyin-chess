from board import Board
from utils import generateFen, WINWIDTH, FPS

import pygame
import os

def main():
    os.environ['SDL_VIDEO_CENTERED'] = '1'
    pygame.init()
    pygame.display.init()
    win = pygame.display.set_mode((WINWIDTH, WINWIDTH))
    clock = pygame.time.Clock()
    pygame.display.set_caption("STY")

    start_fen = generateFen(rand=True)
    board = Board(win, start_fen)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_r:
                    # Refresh the game
                    start_fen = generateFen(rand=True)
                    board = Board(win, start_fen)
            if event.type == pygame.MOUSEBUTTONUP:
                x, y = event.pos
                tile = board.GetSelectedSquare(x, y)
                if tile is not None:
                    board.MovePiece(tile)

        board.UpdateDisplay()
        pygame.display.update()
        clock.tick(FPS)

    pygame.quit()


if __name__ == '__main__':
    main()
