import pygame
from Button_Class import Button
from Dictionaries import color_dic

class MainMenu:
    def __init__(self, screen):
        self.screen = screen
        self.buttons = self.create_buttons()
        self.select_option = None
        
    def create_buttons(self):
        button_width = 200
        button_height = 50
        button_color = color_dic["gray"]
        hover_color = color_dic["light_gray"]
        button_x = (self.screen.get_width() - button_width) // 2
        button_y = 100
        spacing = 60
        
        view_button = Button("View", (button_x, button_y),(button_width, button_height), button_color, hover_color)
        monitor_button = Button("Monitor", (button_x, button_y+spacing),(button_width, button_height), button_color, hover_color)
        
        return [view_button, monitor_button]
    
    def draw(self):
        mouse_pos = pygame.mouse.get_pos()
        mouse_click = pygame.mouse.get_pressed()[0]
        
        for button in self.buttons:
            button.draw(self.screen, mouse_pos)
            if button.is_clicked(mouse_pos, mouse_click):
                return button.text
            
        return None
    
    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return "Quit"
                
            self.screen.fill(color_dic["black"])
            selected_option = self.draw()
            
            if selected_option:
                return selected_option
            
            pygame.display.flip()