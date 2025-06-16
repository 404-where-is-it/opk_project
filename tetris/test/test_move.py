import pygame
import pytest

import sys
sys.path.append("../.")
sys.path.append("./")

from figure import Figure
from figure_chooser import FigureChooser
from constants import WIDTH, HEIGHT, MOD_DEFAULT

class TestMove:
    
    def setup_method(self):
        pygame.init()
        self.field = [[0 for x in range(WIDTH)] for y in range(HEIGHT)]
        self.chooser = FigureChooser(self.field, MOD_DEFAULT)
        self.figure = Figure(self.chooser, MOD_DEFAULT)
        self.figure.spawn()
    
    def teardown_method(self):
        pygame.quit()
    
    #------------------X------------------#
    def test_move_x_right_10(self):
        # сдвиг вправо на 10
        initial_positions = [(block.x, block.y) for block in self.figure.figure]
        self.figure.move_x(10)
        
        for i, block in enumerate(self.figure.figure):
            assert block.x == initial_positions[i][0] + 10
            assert block.y == initial_positions[i][1]
    
    def test_move_x_left_10(self):
        # сдвиг влево на 10
        initial_positions = [(block.x, block.y) for block in self.figure.figure]
        self.figure.move_x(-10)
        
        for i, block in enumerate(self.figure.figure):
            assert block.x == initial_positions[i][0] - 10
            assert block.y == initial_positions[i][1]
    
    def test_move_x_zero(self):
        # сдвиг на 0
        initial_positions = [(block.x, block.y) for block in self.figure.figure]
        self.figure.move_x(0)
        
        for i, block in enumerate(self.figure.figure):
            assert block.x == initial_positions[i][0]
            assert block.y == initial_positions[i][1]
    
    #------------------Y------------------#
    def test_move_y_down_10(self):
        # сдвиг вниз на 10
        initial_positions = [(block.x, block.y) for block in self.figure.figure]
        self.figure.move_y(10)
        
        for i, block in enumerate(self.figure.figure):
            assert block.x == initial_positions[i][0]
            assert block.y == initial_positions[i][1] + 10
    
    def test_move_y_up_10(self):
        # сдвиг вверх на 10
        initial_positions = [(block.x, block.y) for block in self.figure.figure]
        self.figure.move_y(-10)
        
        for i, block in enumerate(self.figure.figure):
            assert block.x == initial_positions[i][0]
            assert block.y == initial_positions[i][1] - 10
    
    def test_move_y_zero(self):
        # сдвиг на 0
        initial_positions = [(block.x, block.y) for block in self.figure.figure]
        self.figure.move_y(0)
        
        for i, block in enumerate(self.figure.figure):
            assert block.x == initial_positions[i][0]
            assert block.y == initial_positions[i][1] 