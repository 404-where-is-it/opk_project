import pygame
import pytest
from collections import Counter

import sys
sys.path.append("../.")
sys.path.append("./")

from figure_chooser import FigureChooser
from constants import WIDTH, HEIGHT, MOD_HARD, Figures

class TestGetWorseFigure:
    
    def setup_method(self):
        pygame.init()
        self.field = [[0 for x in range(WIDTH)] for y in range(HEIGHT)]
        self.chooser = FigureChooser(self.field, MOD_HARD)
    
    def teardown_method(self):
        pygame.quit()
    
    def test_get_worse_figure_avoid_i(self):
        # на поле не хватает фигуры I для стирания 4 линий
        # всё, кроме I-й фигуры
        for y in range(HEIGHT - 4, HEIGHT):
            for x in range(WIDTH):
                if x < WIDTH - 1:
                    self.field[y][x] = 1
        
        # если за 50 раз она не выпала, скорее всего, не выпадет вообще
        figures = [self.chooser.get_worse_figure() for _ in range(50)]
        for figure in figures:
            assert figure != Figures.I
    
    def test_get_worse_figure_avoid_i_rotated(self):
        # аналогично, только I лежит
        for x in range(WIDTH - 4):
            self.field[-1][x] = 1
        
        figures = [self.chooser.get_worse_figure() for _ in range(50)]
        
        for figure in figures:
            assert figure != Figures.I
    
    def test_get_worse_figure_avoid_o(self):
        for y in range(HEIGHT - 2, HEIGHT):
            for x in range(WIDTH - 2):
                 self.field[y][x] = 1
        
        figures = [self.chooser.get_worse_figure() for _ in range(50)]
        
        for figure in figures:
            assert figure != Figures.O
    
    