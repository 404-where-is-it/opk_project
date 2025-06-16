import pygame
import pytest

import sys
sys.path.append("../.")
sys.path.append("./")

from figure import Figure
from figure_chooser import FigureChooser
from constants import WIDTH, HEIGHT, MOD_DEFAULT

class TestSave:
    
    def setup_method(self):
        pygame.init()
        self.field = [[0 for x in range(WIDTH)] for y in range(HEIGHT)]
        self.chooser = FigureChooser(self.field, MOD_DEFAULT)
        self.figure = Figure(self.chooser, MOD_DEFAULT)
        self.figure.spawn()
    
    def teardown_method(self):
        pygame.quit()
    
    def test_save_on_field(self):
        initial_positions = [(block.x, block.y) for block in self.figure.figure]
        test_color = pygame.Color('red')
        
        self.figure.save_on_field(self.field, test_color)
        
        # сохранилась ли?
        for x, y in initial_positions:
            assert self.field[y][x] == test_color
    
    def test_save_on_field_and_get_pos(self):

        initial_positions = [(block.x, block.y) for block in self.figure.figure]
        test_color = pygame.Color('blue')
        
        pos = self.figure.save_on_field_and_get_pos(self.field, test_color)
        
        # сохранилась ли?
        for x, y in initial_positions:
            assert self.field[y][x] == test_color
        
        # проверка позиций
        assert len(pos) == len(initial_positions)
        for i, (x, y) in enumerate(initial_positions):
            assert pos[i] == (x, y) 