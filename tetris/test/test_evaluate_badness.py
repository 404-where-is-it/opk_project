import pygame
import pytest

import sys
sys.path.append("../.")
sys.path.append("./")

from figure_chooser import FigureChooser
from constants import WIDTH, HEIGHT, MOD_HARD

class TestEvaluateBadness:
    
    def setup_method(self):
        pygame.init()
        self.field = [[0 for x in range(WIDTH)] for y in range(HEIGHT)]
        self.chooser = FigureChooser(self.field, MOD_HARD)
    
    def teardown_method(self):
        pygame.quit()
    
    def test_evaluate_badness_4_lines_clear(self):
        # 4 полных линии
        for y in range(HEIGHT - 4, HEIGHT):
            for x in range(WIDTH):
                self.field[y][x] = 1
        
        badness = self.chooser.evaluate_badness()
        
        assert badness < -30  # -4 линии * 10 = -40
    
    def test_evaluate_badness_no_lines_clear(self):
        # какие-то блоки есть, но нет линий
        for y in range(HEIGHT - 8, HEIGHT):
            for x in range(WIDTH - 2):
                self.field[y][x] = 1
    
        badness = self.chooser.evaluate_badness()
        assert badness > 0 # высота + никаких линий