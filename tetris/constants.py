from enum import Enum

import pygame

# Константы
WIDTH, HEIGHT = 10, 20  # ширина и высота в клетках
TILE =40 # клетка в пикселях
GAME_RES = WIDTH * TILE, HEIGHT * TILE
FPS = 60.0
BORDER = 5

START_FALL_SPEED = 20
FALL_THRESHOLD = 1000
SPEED_UP_THRESHOLD = 500

NUM_OF_FIGURES = 7
NUM_OF_BLOCKS = 4
NUM_OF_ROTATES = 4

MOD_DEFAULT = "Default"
MOD_HARD = "Hard"


class Figures(Enum):
    I = 0
    O = 1
    Z = 2
    L = 3
    T = 4
    J = 5
    S = 6


# Цвета
BLACK = pygame.Color('black')
WHITE = pygame.Color('white')
GRAY = pygame.Color(40, 40, 40)
HACKER = pygame.Color("#102614")
GREEN_I = pygame.Color("#a5f216")
GREEN_O= pygame.Color("#316301")
GREEN_Z = pygame.Color("#02fa34")
GREEN_L = pygame.Color("#02fa86")
GREEN_T = pygame.Color("#036336")
GREEN_J = pygame.Color("#186303")
GREEN_S = pygame.Color("#518244")

# Цвета для каждой фигуры
figures_color = [0] * NUM_OF_FIGURES
figures_color[Figures.I.value] = GREEN_I
figures_color[Figures.O.value] = GREEN_O
figures_color[Figures.Z.value] = GREEN_Z
figures_color[Figures.L.value] = GREEN_L
figures_color[Figures.T.value] = GREEN_T
figures_color[Figures.J.value] = GREEN_J
figures_color[Figures.S.value] = GREEN_S

figures_position = [(0, 0) * NUM_OF_BLOCKS] * NUM_OF_FIGURES
figures_position[Figures.I.value] = ((0, 1), (0, 0), (0, 2), (0, 3))
figures_position[Figures.O.value] = ((1, 1), (0, 0), (1, 0), (0, 1))
figures_position[Figures.Z.value] = ((1, 1), (0, 1), (1, 0), (0, 2))
figures_position[Figures.L.value] = ((1, 1), (1, 0), (0, 0), (1, 2))
figures_position[Figures.T.value] = ((1, 1), (0, 1), (1, 0), (1, 2))
figures_position[Figures.J.value] = ((1, 1), (1, 0), (1, 2), (0, 2))
figures_position[Figures.S.value] = ((1, 1), (0, 0), (0, 1), (1, 2))

# спавн
OFFSET_X = WIDTH // 2 - 1
OFFSET_Y = 2

# фигуры в координатах
FIGURE_RECTS = [[pygame.Rect(x + OFFSET_X, y + OFFSET_Y, 0, 0) for (x, y) in figure_pos] \
                for figure_pos in figures_position]
