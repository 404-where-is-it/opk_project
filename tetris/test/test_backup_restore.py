import pygame
import pytest

import sys
sys.path.append("../.")
sys.path.append("./")

from figure import Figure
from figure_chooser import FigureChooser
from constants import WIDTH, HEIGHT, MOD_DEFAULT

class TestBackupRestore:
    
    def setup_method(self):
        pygame.init()
        self.field = [[0 for x in range(WIDTH)] for y in range(HEIGHT)]
        self.chooser = FigureChooser(self.field, MOD_DEFAULT)
        self.figure = Figure(self.chooser, MOD_DEFAULT)
        self.figure.spawn()
    
    def teardown_method(self):
        pygame.quit()
    
    def test_backup_restore(self):
        initial_positions = [(block.x, block.y) for block in self.figure.figure]
        
        self.figure.backup()
        self.figure.move_x(5)
        self.figure.move_y(3)
        
        self.figure.restore()
        
        for i, block in enumerate(self.figure.figure):
            assert block.x == initial_positions[i][0]
            assert block.y == initial_positions[i][1]
    
    def test_backup_restore_multiple_moves(self):
        initial_positions = [(block.x, block.y) for block in self.figure.figure]
        
        self.figure.backup()
        self.figure.move_x(2)
        self.figure.move_y(1)
        self.figure.move_x(-1)
        self.figure.move_y(4)
        
        self.figure.restore()
        
        for i, block in enumerate(self.figure.figure):
            assert block.x == initial_positions[i][0]
            assert block.y == initial_positions[i][1] 