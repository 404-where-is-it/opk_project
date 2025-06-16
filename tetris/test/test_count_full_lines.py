import pygame
import pytest

import sys
sys.path.append("../.")
sys.path.append("./")

from figure_chooser import FigureChooser
from constants import WIDTH, HEIGHT, MOD_HARD

class TestCountFullLines:
    
    def setup_method(self):
        pygame.init()
        self.field = [[0 for x in range(WIDTH)] for y in range(HEIGHT)]
        self.chooser = FigureChooser(self.field, MOD_HARD)
    
    def teardown_method(self):
        pygame.quit()
    
    def test_count_full_lines_2_lines(self):
        # 2 полных линии
        for y in range(HEIGHT - 2, HEIGHT):
            for x in range(WIDTH):
                self.field[y][x] = 1
        
        count = self.chooser.count_full_lines()
        
        assert count == 2
    
    def test_count_full_lines_mixed(self):
        # 1 полностью, 2 частично
        for x in range(WIDTH):
            self.field[HEIGHT - 1][x] = 1
        
        for x in range(WIDTH - 2):
            self.field[HEIGHT - 2][x] = 1
        
        count = self.chooser.count_full_lines()
        
        assert count == 1 