from copy import deepcopy
from idlelib.configdialog import changes

from constants import Figures, NUM_OF_BLOCKS, OFFSET_Y, OFFSET_X, NUM_OF_FIGURES, NUM_OF_ROTATES
from constants import figures_position, FIGURE_RECTS, HEIGHT, WIDTH, MOD_DEFAULT, MOD_HARD
from random import shuffle, choice
from figure import Figure



class FigureChooser:
    def __init__(self, field=None, mode=MOD_DEFAULT):
        self.generator = self.gen_bag_chooser()
        self.sim_field = field
        self.changes = None
        self.mode = mode

    def get_rand_figure(self) -> Figures:
        if self.mode == MOD_DEFAULT:
            return next(self.generator)
        elif self.mode == MOD_HARD:
            return self.get_worse_figure()


    @staticmethod
    def gen_bag_chooser():
        bag = []
        while True:
            if len(bag) == 0:
                bag = list(Figures)
                shuffle(bag)
            yield bag.pop()

    def simulate_drop(self, figure: Figure):
        dy = 1
        distance = 0
        while not figure.collision_y(dy, self.sim_field):
            figure.move_y(dy)
            distance += dy
        self.changes = figure.save_on_field_and_get_pos(self.sim_field, 1)
        return distance

    def count_full_lines(self):
        count = 0
        for line in range(HEIGHT):
            count += all(self.sim_field[line])
        return count

    def count_max_height(self):
        max_y = 0
        for y in range(HEIGHT - 1, -1, -1):
            is_empty_line = True
            for x in range(WIDTH):
                if self.sim_field[y][x]:
                    max_y = max(HEIGHT - y, max_y)
                    is_empty_line = False
            if is_empty_line:
                break
        return max_y

    def evaluate_badness(self):
        lines_cleared = self.count_full_lines() # very good: -
        max_height = self.count_max_height()    # bad: +
        return max_height - lines_cleared

    @staticmethod
    def figure_max(array):
        if array is None:
            return None
        m = array[0]
        argmax = []
        for i in Figures:
            if array[i.value] > m:
                m = array[i.value]
        for i in Figures:
            if array[i.value] == m:
                argmax.append(i)
        print('SUGGEST: ',*[i.name for i in argmax])

        return argmax

    def get_worse_figure(self) -> Figures:
        # (максимальная плохость)
        badness = [0] * NUM_OF_FIGURES

        figure = Figure()
        figure.figure = [0]*NUM_OF_BLOCKS

        for index in Figures:
            figure.num = index
            figure.figure = deepcopy(FIGURE_RECTS[index.value])
            # сдвигаем фигуру влево вверх
            figure.move_x(-OFFSET_X)
            figure.move_y(-OFFSET_Y)
            min_badness = 9999999999
            dx = 1
            can_move_x = not figure.collision_x(dx, self.sim_field)
            while can_move_x:
                for i in range(NUM_OF_ROTATES):
                    diff_y = self.simulate_drop(figure)

                    scalar_badness = self.evaluate_badness()
                    self.restore_changes()

                    figure.move_y(-diff_y) # возвращаем обратно наверх

                    if scalar_badness < min_badness:
                        min_badness = scalar_badness

                    figure.rotate_if_possible(self.sim_field)

                can_move_x = not figure.collision_x(dx, self.sim_field)
                figure.move_x(dx)

            badness[index.value] = min_badness
        print()
        print(*[i.name for i in Figures], sep='\t')
        print(*badness, sep='\t')
        return choice(self.figure_max(badness))

    def restore_changes(self):
        for pos in self.changes:
            x = pos[0]
            y = pos[1]
            self.sim_field[y][x] = 0

