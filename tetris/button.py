import pygame

from constants import WHITE


class ImageButton:
    def __init__(self, x, y, width, height, text, image_path, hover_image_path=None, font_size=36, font_color=WHITE):
        self.x = x
        self.y = y
        self.width = width

        self.height = height
        self.text = text
        self.font_size = font_size
        self.font_color = font_color

        self.image = pygame.image.load(image_path)
        # масштабируем под размер кнопки
        self.image = pygame.transform.scale(self.image, (width, height))

        self.hover_image = self.image
        if hover_image_path:
            self.hover_image = pygame.image.load(hover_image_path)
            self.hover_image = pygame.transform.scale(self.hover_image, (width, height))

        # создаём прямоугольник с координатами и размером image
        self.rect = self.image.get_rect(topleft=(x, y))
        self.is_hovered = False

    def __str__(self):
        return f'"{self.text}"'

    def draw(self, screen: pygame.Surface, mouse_pos: tuple[int, int]):

        self.check_hover(mouse_pos)

        if self.is_hovered:
            current_image = self.hover_image
        else:
            current_image = self.image
        screen.blit(current_image, self.rect.topleft)

        if self.text:
            font = pygame.font.Font(None, self.font_size)
            text_surface = font.render(self.text, True, self.font_color)
            # прямоугольник, куда будет отображаться текст
            text_rect = text_surface.get_rect(center=self.rect.center)
            screen.blit(text_surface, text_rect)

    def check_hover(self, mouse_pos):
        self.is_hovered = self.rect.collidepoint(mouse_pos)

    def handle_event(self, event: pygame.event.Event):
        if event.type == pygame.MOUSEBUTTONDOWN and self.is_hovered:
            event = pygame.event.Event(pygame.USEREVENT, BtnEvent=self)
            pygame.event.post(event)
