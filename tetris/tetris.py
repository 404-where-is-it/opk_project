import sys

from constants import *
import pygame
from draw import Drawer
from figure_chooser import FigureChooser
from figure import Figure
from button import ImageButton


class TetrisGame:
    def __init__(self):
        self.drawer                 = None
        self.field                  = None
        self.figure                 = None

        pygame.init()
        self.mode                   = MOD_DEFAULT
        self.screen                 = pygame.display.set_mode(GAME_RES)

        self.clock                  = pygame.time.Clock()
        # Настройки падения
        self.start_fall_speed       = 0
        self.fall_count             = 0
        self.fall_speed             = 0
        self.fall_threshold         = 0

        self.score = -1
        self.lines_cleared = 0

        pygame.display.set_caption("т-те.. как там его .. тетр.. тетраэдр ")

    def prepare_new_game(self, mode):

        self.field = [[0 for x in range(WIDTH)] for y in range(HEIGHT)]

        self.mode = mode
        self.drawer                 = Drawer(self.screen, self.mode)
        chooser                     = FigureChooser(self.field, self.mode)
        self.figure                 = Figure(chooser, self.mode)

        # счет
        self.score                  = 0
        self.lines_cleared          = 0

        self.start_fall_speed       = START_FALL_SPEED
        self.fall_count             = 0
        self.fall_speed             = self.start_fall_speed
        self.fall_threshold         = FALL_THRESHOLD

    def clear_lines(self):
        lines_cleared = 0
        line = HEIGHT - 1   # координата линии

        for row in range(HEIGHT - 1, -1, -1):
            if not all(self.field[row]):
                # копируем
                for i in range(WIDTH):
                    self.field[line][i] = self.field[row][i]
                line -= 1
            else: # ряд заполнен
                lines_cleared += 1

        # очищаем верхние строки
        for row in range(line + 1):
            for i in range(WIDTH):
                self.field[row][i] = 0

        return lines_cleared

    @staticmethod
    def handle_input():
        rotate = False
        dx, dy = 0, 0
        fall_multiple = 1

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True, 0, 0, False, 0  # quit flag

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    fall_multiple *= 30
                if event.key == pygame.K_UP:
                    rotate = True
                if event.key == pygame.K_LEFT:
                    dx -= 1
                if event.key == pygame.K_RIGHT:
                    dx += 1

        return False, dx, dy, rotate, fall_multiple

    def update(self, dx, dy, rotate):
        # обновляем каждый кадр

        # пытаемся повернуться
        if rotate:
            self.figure.rotate_if_possible(self.field)

        # Обработка движения
        can_move_dx = not self.figure.collision_x(dx, self.field)
        can_move_dy = not self.figure.collision_y(dy, self.field)

        if can_move_dx and can_move_dy:
            self.figure.move_x(dx)
        if can_move_dy:
            self.figure.move_y(dy)

        # фигурка упала
        if not can_move_dy:
            self.figure.save_on_field(self.field, self.figure.color)

            # подчищаем линии
            lines_cleared = self.clear_lines()
            if lines_cleared > 0:
                self.lines_cleared += lines_cleared
                self.score += lines_cleared * 100

            # сброс скорости падения
            # каждые 500 очков ускорение
            self.fall_speed = self.start_fall_speed + 5 * (self.score // SPEED_UP_THRESHOLD)
            self.fall_count = 0

            # создаем новую фигуру
            self.figure.spawn()

            # game over?
            if self.figure.collision_y(0, self.field):
                return True  # Game over
        return False

    def calc_falling(self, dy, fall_multiple):
        self.fall_speed *= fall_multiple
        self.fall_count += self.fall_speed
        if self.fall_count >= self.fall_threshold:
            dy += 1
            self.fall_count = 0
        return dy

    def game_over(self):
        print(f"Game Over! Final Score: {self.score}")

    def run(self):
        running = True
        print(f"Start Game in {self.mode} mode;")

        self.figure.spawn()

        while running:
            self.clock.tick(FPS)

            # ввод
            quit_game, dx, dy, rotate, fall_multiple = self.handle_input()
            if quit_game:
                pygame.quit()
                sys.exit()

            # падение
            dy = self.calc_falling(dy, fall_multiple)

            # обновление состояния
            game_over = self.update(dx, dy, rotate)
            if game_over:
                self.game_over()
                running = False

            # рисуем всё
            self.drawer.draw(self.figure, self.score, self.lines_cleared, self.field)

    def main_menu(self):
        btn_width = GAME_RES[1] // 3
        btn_height = btn_width / 3
        btn_easy_mode = ImageButton(GAME_RES[0] / 2 - (btn_width / 2), GAME_RES[1] // 6, btn_width, btn_height,
                                    "",
                                    "assets/5.jpg",
                                    "assets/4.jpg",
                                    font_size=TILE)
        btn_hard_mode = ImageButton(GAME_RES[0] / 2 - (btn_width / 2), GAME_RES[1] // 3, btn_width, btn_height,
                                    "",
                                    "assets/2.jpg",
                                    "assets/3.jpg",
                                    font_size=TILE,
                                    font_color=GREEN_Z)
        btn_quit = ImageButton(GAME_RES[0] / 2 - (btn_width / 2), GAME_RES[1] // 1.25, btn_width, btn_height,
                               "Quit",
                               "assets/btn_background.jpg",
                               "assets/7.jpg",
                               font_size=TILE)

        btns = [btn_easy_mode, btn_hard_mode, btn_quit]

        running = True
        while running:
            self.clock.tick(FPS)
            self.screen.fill(BLACK)

            for event in pygame.event.get():
                for btn in btns:
                    btn.handle_event(event)

                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.USEREVENT:
                    for btn in btns:
                        if event.BtnEvent == btn:
                            print(f'btn {btn} pressed')
                            if btn == btn_quit:
                                pygame.event.post(pygame.event.Event(pygame.QUIT))
                            if btn == btn_easy_mode:
                                self.prepare_new_game(MOD_DEFAULT)
                                return
                            if btn == btn_hard_mode:
                                self.prepare_new_game(MOD_HARD)
                                return

            for btn in btns:
                btn.draw(self.screen, pygame.mouse.get_pos())

            if self.score >= 0:
                font = pygame.font.Font(None, TILE)
                text = font.render(f"Score: {self.score}", True, WHITE)
                text_rect = text.get_rect(center=(GAME_RES[0] // 2, GAME_RES[1] // 12))
                self.screen.blit(text, text_rect)

            # btn_hard_mode.draw(self.screen, pygame.mouse.get_pos())
            pygame.display.flip()
