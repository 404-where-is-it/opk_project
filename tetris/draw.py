import pygame

from constants import *


class Drawer:
    def __init__(self, screen, mode=MOD_DEFAULT):
        self.mod = mode
        self.screen = screen
        self.grid = [pygame.Rect(x * TILE, y * TILE, TILE, TILE)
                     for x in range(WIDTH)
                     for y in range(HEIGHT)]

        self.figure_rect = pygame.Rect(0, 0, TILE - BORDER, TILE - BORDER)

    def draw_grid(self):
        for rect in self.grid:
            pygame.draw.rect(self.screen, HACKER, rect, 1)

    def draw_ui(self, figure, score, lines_cleared):

        font = pygame.font.Font(None, TILE)
        # FIXME: исправить отрисовку текста

        # очки
        score_text = font.render(f"Score: {score}", True, WHITE)
        self.screen.blit(score_text, (10, 10))

        # линий стёрто
        lines_text = font.render(f"Lines: {lines_cleared}", True, WHITE)
        self.screen.blit(lines_text, (10, 10 + TILE))

        # текущая фигура
        figure_text = font.render(f"Current: {figure.num.name}", True, figure.color)
        self.screen.blit(figure_text, (10, 10 + 2 * TILE))

        # следующей фигуры
        if self.mod != MOD_HARD:
            next_figure_text = font.render(f"Next: {figure.next_num.name}", True, figure.next_color)
            self.screen.blit(next_figure_text, (10, 10 + 3 * TILE))

    def draw_figure(self, figure, color):
        for i in range(NUM_OF_BLOCKS):
            self.figure_rect.x = figure[i].x * TILE
            self.figure_rect.y = figure[i].y * TILE
            pygame.draw.rect(self.screen, color, self.figure_rect)

    def draw_game(self, figure, field):
        self.screen.fill(BLACK)
        self.draw_grid()

        # отрисовка текущей фигуры
        self.draw_figure(figure.figure, figure.color)

        # отрисовка размещенных фигур
        for y in range(HEIGHT):
            for x in range(WIDTH):
                if field[y][x]:
                    self.figure_rect.x, self.figure_rect.y = x * TILE, y * TILE
                    pygame.draw.rect(self.screen, field[y][x], self.figure_rect)

    def draw(self, figure, score, lines_cleared, field):
        self.draw_game(figure, field)
        self.draw_ui(figure, score, lines_cleared)

        pygame.display.flip()
