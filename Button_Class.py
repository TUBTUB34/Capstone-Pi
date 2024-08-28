# button_class.py

import pygame

class Button:
    def __init__(self, text, pos, size, color, hover_color):
        self.text = text
        self.pos = pos
        self.size = size
        self.color = color
        self.hover_color = hover_color
        self.rect = pygame.Rect(pos, size)
        self.font = pygame.font.Font(None, 36)
        self.clicked = False  # Track if the button is currently being clicked

    def draw(self, screen, mouse_pos):
        if self.rect.collidepoint(mouse_pos):
            pygame.draw.rect(screen, self.hover_color, self.rect)
        else:
            pygame.draw.rect(screen, self.color, self.rect)
        text_surf = self.font.render(self.text, True, (255, 255, 255))
        screen.blit(text_surf, (self.pos[0] + 10, self.pos[1] + 10))

    def is_clicked(self, mouse_pos, mouse_click):
        if self.rect.collidepoint(mouse_pos):
            if mouse_click and not self.clicked:
                self.clicked = True
                return True
            if not mouse_click:
                self.clicked = False  # Reset clicked state when mouse button is released
        return False
