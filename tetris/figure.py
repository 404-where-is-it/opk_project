from constants import *
from random import choice
from copy import deepcopy

class Figure:
    def __init__(self, figure_chooser=None, mode=MOD_DEFAULT):
        self.next_color             = None
        self.mode                   = mode
        self.figure                 = None
        self.is_square              = False
        self.color                  = None
        self.num: Figures           = Figures.I
        self.chooser                = figure_chooser
        self.figure_old             = None

        # традиционно первая фигура -- одна из I, O, L, T
        self.next_num               = choice((Figures.I, Figures.O, Figures.L, Figures.T))

    def backup(self):
        self.figure_old = deepcopy(self.figure)

    def restore(self):
        self.figure = self.figure_old

    def spawn(self):

        if self.mode == MOD_DEFAULT:
            self.num = self.next_num
            self.next_num = self.chooser.get_rand_figure()
            self.next_color = figures_color[self.next_num.value]

        if self.mode == MOD_HARD:
            # нет следующей фигуры в хард моде
            self.num = self.chooser.get_rand_figure()

        # Копируем из массива всех нашу
        self.figure = deepcopy(FIGURE_RECTS[self.num.value])
        self.color = figures_color[self.num.value]

        # Флаг для запрета вращения
        self.is_square = self.check_if_square()

    def collision_x(self, dx, field):
        # проверка столкновения по X
        for i in range(NUM_OF_BLOCKS):
            new_x = self.figure[i].x + dx
            if new_x < 0 or new_x > WIDTH - 1:
                return True
            
            if field[self.figure[i].y][new_x]:
                return True
        return False

    def collision_y(self, dy, field):
        # проверка столкновения по Y
        for i in range(4):
            new_y = self.figure[i].y + dy
            if new_y > HEIGHT - 1 or new_y < 0:
                return True
            if field[new_y][self.figure[i].x]:
                return True
        return False

    def move_x(self, dx):
        for i in range(NUM_OF_BLOCKS):
            self.figure[i].x += dx

    def move_y(self, dy):
        for i in range(NUM_OF_BLOCKS):
            self.figure[i].y += dy

    def save_on_field_and_get_pos(self, field, value):
        # сохраняет на поле и возвращает координаты
        # упавшей фигуры
        pos = [0] * NUM_OF_BLOCKS
        for i in range(NUM_OF_BLOCKS):
            x = self.figure[i].x
            y = self.figure[i].y
            pos[i] = (x, y)
            field[y][x] = value
        return pos

    def save_on_field(self, field, value):
        # сохранить упавшую
        
        for i in range(NUM_OF_BLOCKS):
            x = self.figure[i].x
            y = self.figure[i].y
            
            field[y][x] = value

    def check_if_square(self):
        if self.num == Figures.O:
            return True
        return False

    def rotate_if_possible(self, field):
        if self.is_square:
            return
        self.backup()
        self.rotate()
        if self.collision_x(0, field):
            self.restore()

    def rotate(self):
        center = self.figure[0]
        for i in range(4):
            # Смещаем центр координат и меняем x <-> y
            x = self.figure[i].y - center.y
            y = self.figure[i].x - center.x

            # Возвращаем центр координат обратно
            self.figure[i].x = center.x - x
            self.figure[i].y = center.y + y
