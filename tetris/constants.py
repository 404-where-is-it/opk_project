from enum import Enum

import pygame

# Константы
WIDTH, HEIGHT = 10, 20  # ширина и высота в клетках
TILE = 50  # клетка в пикселях
GAME_RES = WIDTH * TILE, HEIGHT * TILE
FPS = 60.0
BORDER = 10

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

# Традиционные цвета фигур Tetris
CYAN = pygame.Color(0, 255, 255)  # I - голубой
YELLOW = pygame.Color(255, 255, 0)  # O - желтый
RED = pygame.Color(255, 0, 0)  # Z - красный
ORANGE = pygame.Color(255, 165, 0)  # L - оранжевый
PURPLE = pygame.Color(128, 0, 128)  # T - фиолетовый
BLUE = pygame.Color(0, 0, 255)  # J - синий
GREEN = pygame.Color(0, 255, 0)  # S - зеленый

# Цвета для каждой фигуры
figures_color = [0] * NUM_OF_FIGURES
figures_color[Figures.I.value] = CYAN
figures_color[Figures.O.value] = YELLOW
figures_color[Figures.Z.value] = RED
figures_color[Figures.L.value] = ORANGE
figures_color[Figures.T.value] = PURPLE
figures_color[Figures.J.value] = BLUE
figures_color[Figures.S.value] = GREEN

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
