import pytest
import pygame
import sys

import sys
sys.path.append("../.")
sys.path.append("./")


# Импортируем константы и класс из оригинального кода
from tetris import WIDTH, HEIGHT, TetrisGame, MOD_DEFAULT

class TestClearLines:
    """Тесты для функции clear_lines"""
    
    def setup_method(self):
        """Настройка перед каждым тестом"""
        # Инициализируем pygame для тестов
        pygame.init()
        self.game = TetrisGame()
        # Инициализируем игру для создания поля
        self.game.prepare_new_game(MOD_DEFAULT)
    
    def teardown_method(self):
        """Очистка после каждого теста"""
        pygame.quit()
    
    def test_clear_lines_empty_field(self):
        """Тест: очистка линий на пустом поле"""
        lines_cleared = self.game.clear_lines()
        
        assert lines_cleared == 0
        # Поле должно остаться пустым
        for y in range(HEIGHT):
            for x in range(WIDTH):
                assert self.game.field[y][x] == 0
    
    def test_clear_lines_one_full_line(self):
        """Тест: очистка одной заполненной линии"""
        # Заполняем одну линию (последнюю)
        for x in range(WIDTH):
            self.game.field[HEIGHT - 1][x] = pygame.Color('red')
        
        lines_cleared = self.game.clear_lines()
        
        assert lines_cleared == 1
        # Поле должно стать пустым
        for y in range(HEIGHT):
            for x in range(WIDTH):
                assert self.game.field[y][x] == 0
    
    def test_clear_lines_multiple_full_lines(self):
        """Тест: очистка нескольких заполненных линий"""
        # Заполняем две последние линии
        for y in range(HEIGHT - 2, HEIGHT):
            for x in range(WIDTH):
                self.game.field[y][x] = pygame.Color('blue')
        
        lines_cleared = self.game.clear_lines()
        
        assert lines_cleared == 2
        # Поле должно стать пустым
        for y in range(HEIGHT):
            for x in range(WIDTH):
                assert self.game.field[y][x] == 0
    
    def test_clear_lines_partial_line(self):
        """Тест: частично заполненная линия не очищается"""
        # Заполняем только половину линии
        for x in range(WIDTH // 2):
            self.game.field[HEIGHT - 1][x] = pygame.Color('green')
        
        lines_cleared = self.game.clear_lines()
        
        assert lines_cleared == 0
        # Линия должна остаться на месте
        for x in range(WIDTH // 2):
            assert self.game.field[HEIGHT - 1][x] == pygame.Color('green')
    
    def test_clear_lines_with_blocks_above(self):
        """Тест: очистка линии с блоками выше"""
        # 1 линия полностью заполнена
        for x in range(WIDTH):
            self.game.field[-1][x] = pygame.Color('red')
        
        # Добавляем блоки выше
        self.game.field[-2][0] = pygame.Color('blue')
        self.game.field[-3][-1] = pygame.Color('green')
        

        lines_cleared = self.game.clear_lines()
        
        assert lines_cleared == 1
        # вниз всё
        assert self.game.field[-1][0] == pygame.Color('blue')
        assert self.game.field[-2][-1] == pygame.Color('green')
        # 3 линия удалилась
        assert self.game.field[-3][0] == 0
    
    def test_clear_lines_all_lines_full(self):
        """Тест: очистка всех заполненных линий"""
        # Заполняем все линии
        for y in range(HEIGHT):
            for x in range(WIDTH):
                self.game.field[y][x] = pygame.Color('yellow')
        
        lines_cleared = self.game.clear_lines()
        
        assert lines_cleared == HEIGHT
        # Поле должно стать пустым
        for y in range(HEIGHT):
            for x in range(WIDTH):
                assert self.game.field[y][x] == 0
    
    def test_clear_lines_mixed_scenario(self):
        # полная, половина, полная
        
        # первая линия полностью
        for x in range(WIDTH):
            self.game.field[-1][x] = pygame.Color('red')
        
        # вторая линия частично
        for x in range(WIDTH // 2):
            self.game.field[-2][x] = pygame.Color('blue')
        
        # третья линия полностью
        for x in range(WIDTH):
            self.game.field[-3][x] = pygame.Color('green')
        
        
        lines_cleared = self.game.clear_lines()
        
        assert lines_cleared == 2
        
        # должна быть заполненной на половину
        for x in range(WIDTH // 2):
            assert self.game.field[-1][x] == pygame.Color('blue')  # вниз на 1
        for x in range(WIDTH // 2, WIDTH):
            assert self.game.field[0][x] == 0

        # 2 и 3 должны быть пустыми
        for x in range(WIDTH):
            assert self.game.field[-2][x] == 0
            assert self.game.field[-3][x] == 0
    
    def test_clear_lines_return_value(self):
        """Тест: проверка возвращаемого значения"""      
        # Заполняем 3 линии
        for y in range(3):
            for x in range(WIDTH):
                self.game.field[HEIGHT - 1 - y][x] = pygame.Color('purple')
        
        lines_cleared = self.game.clear_lines()
        
        assert lines_cleared == 3
        assert isinstance(lines_cleared, int)
        assert lines_cleared >= 0 