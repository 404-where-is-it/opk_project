import pygame
import pytest

import sys
sys.path.append("../.")
sys.path.append("./")
from figure_chooser import FigureChooser
from constants import WIDTH, HEIGHT, MOD_DEFAULT, NUM_OF_FIGURES

class TestFigureChooser:
    
    def setup_method(self):
        
        pygame.init()
        self.field = [[0 for x in range(WIDTH)] for y in range(HEIGHT)]
        self.chooser = FigureChooser(self.field, MOD_DEFAULT)
    
    def teardown_method(self):
        pygame.quit()
    
    def test_7_bag_system(self):
        # каждый раз должны получить уникальные фигуры! (из 7 штук)
        num_of_tests = 10
        for i in range(num_of_tests):
            figures = []
            for _ in range(NUM_OF_FIGURES):
                figures.append(self.chooser.get_rand_figure())
            
            unique_figures = set(figures)
            assert len(unique_figures) == NUM_OF_FIGURES 