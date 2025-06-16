import pytest
import pygame

import sys
sys.path.append("../.")
sys.path.append("./")

# Импортируем необходимые компоненты
from figure import Figure
from figure_chooser import FigureChooser
from constants import WIDTH, HEIGHT, MOD_DEFAULT

class TestCollision:
    
    def setup_method(self):
        pygame.init()
        self.field = [[0 for x in range(WIDTH)] for y in range(HEIGHT)]
        self.chooser = FigureChooser(self.field, MOD_DEFAULT)
        self.figure = Figure(self.chooser, MOD_DEFAULT)
        self.figure.spawn()
    
    def teardown_method(self):
        pygame.quit()
    
    #------------------X------------------#
    def test_collision_x_no_collision(self):
        # Проверяем движение вправо на 1
        assert not self.figure.collision_x(1, self.field)
        # Проверяем движение влево на 1
        assert not self.figure.collision_x(-1, self.field)
    
    def test_collision_x_left_border(self):
        # упираемся влево
        while not self.figure.collision_x(-1, self.field):
            self.figure.move_x(-1)

        left_x = min(block.x for block in self.figure.figure)
        assert left_x == 0
        assert self.figure.collision_x(-1, self.field)
    
    def test_collision_x_right_border(self):
        # упираемся вправо
        while not self.figure.collision_x(1, self.field):
            self.figure.move_x(1)

        right_x = max(block.x for block in self.figure.figure)
        assert right_x == WIDTH - 1
        assert self.figure.collision_x(1, self.field)
    
    def test_collision_x_with_blocks(self):
        # блоки справа от фигуры
        for block in self.figure.figure:
            if block.x + 1 < WIDTH:
                self.field[block.y][block.x + 1] = 1
        
        assert self.figure.collision_x(1, self.field)
    
    def test_collision_x_zero_movement(self):
        assert not self.figure.collision_x(0, self.field)
    
    def test_collision_x_large_movement(self):
        assert self.figure.collision_x(WIDTH, self.field)
        assert self.figure.collision_x(-WIDTH, self.field)
    
    #------------------Y------------------#
    def test_collision_y_no_collision(self):
        assert not self.figure.collision_y(1, self.field)
    
    def test_collision_y_fall_down(self):
        while not self.figure.collision_y(1, self.field):
            self.figure.move_y(1)
        
        bottom_y = max(block.y for block in self.figure.figure)
        assert bottom_y == HEIGHT - 1
        assert self.figure.collision_y(1, self.field) # упёрлись в низ
    
    def test_collision_y_with_blocks_below(self):
        # блоки под фигурой
        for block in self.figure.figure:
            if block.y + 1 < HEIGHT:
                self.field[block.y + 1][block.x] = 1
        
        assert self.figure.collision_y(1, self.field)
    
    def test_collision_y_zero_movement(self):
        assert not self.figure.collision_y(0, self.field)
    
    def test_collision_y_large_movement(self):
        assert self.figure.collision_y(HEIGHT, self.field)
    
    def test_collision_y_up(self):
        assert not self.figure.collision_y(-1, self.field)
    
    def test_collision_y_top_border(self):
        while not self.figure.collision_y(-1, self.field):
            self.figure.move_y(-1)

        min_y = min(block.y for block in self.figure.figure)
        assert min_y == 0