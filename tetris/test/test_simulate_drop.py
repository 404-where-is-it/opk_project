import pygame
import pytest

import sys
sys.path.append("../.")
sys.path.append("./")

from figure_chooser import FigureChooser
from figure import Figure
from constants import WIDTH, HEIGHT, MOD_HARD

class TestSimulateDrop:
    
    def setup_method(self):
        pygame.init()
        self.field = [[0 for x in range(WIDTH)] for y in range(HEIGHT)]
        self.chooser = FigureChooser(self.field, MOD_HARD)
        self.figure = Figure(self.chooser, MOD_HARD)
        self.figure.spawn()
    
    def teardown_method(self):
        pygame.quit()
    
    def test_simulate_drop_and_restore(self):
        # создаем блоки внизу для падения
        for x in range(WIDTH):
            self.field[-1][x] = 1
        
        # запоминаем начальное состояние поля
        initial_field = [row for row in self.field]
        
        drop_distance = self.chooser.simulate_drop(self.figure)
        
        # падение есть
        assert drop_distance > 0

        # блоки на поле есть
        for block in self.figure.figure:
            assert self.field[block.y][block.x] == 1
        
        # восстанавливаем изменения
        self.chooser.restore_changes()
        
        # проверяем, что поле вернулось к исходному состоянию
        for y in range(HEIGHT):
            for x in range(WIDTH):
                assert self.field[y][x] == initial_field[y][x] 