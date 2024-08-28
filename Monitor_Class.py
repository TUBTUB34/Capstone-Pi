import pygame
from Button_Class import Button
from I2CScanner_Class import I2CScanner
from Dictionaries import color_dic,address_names

class Monitor:
    def __init__(self, screen):
        self.screen = screen
        self.i2c_scanner = I2CScanner()
        self.buttons = []
        self.no_Devices = None
        self.create_buttons()
        self.Voltage = None
        self.Current = None
        self.Power = None
        self.font = pygame.font.Font(None, 36)
        self.displayValue = False

    def create_buttons(self):
        
        addresses = self.i2c_scanner.scan()
        button_width = 200
        button_height = 50
        button_color = color_dic["gray"]
        hover_color = color_dic["light_gray"]
        button_x = 30
        button_y = 100
        spacing = 60
        
        
        if not addresses:
            font = pygame.font.Font(None, 36)
            self.no_Devices = font.render("No Devices Connected", True, color_dic["white"])
            back_button = Button("Back", (button_x,self.screen.get_height() // 2 + spacing), (button_width, button_height), button_color, hover_color)
            self.buttons.append(back_button)
        else:
            for i, address in enumerate(addresses):
            
                # Get the name from the dictionary, or default to the address if not found
                button_text = address_names.get(int(address, 16), f"I2C Address: {address}")
                new_button = Button(button_text, (button_x, button_y + i * spacing), (button_width, button_height), button_color, hover_color)
                self.buttons.append(new_button)
            back_button = Button("Back", (button_x,button_y + len(addresses) * spacing + spacing), (button_width, button_height), button_color, hover_color)
            self.buttons.append(back_button)

    def draw(self):
        mouse_pos = pygame.mouse.get_pos()
        mouse_click = pygame.mouse.get_pressed()[0]
        
        if self.no_Devices:
            text_rect = self.no_Devices.get_rect(center=(self.screen.get_width() // 2, self.screen.get_height() // 2))
            self.screen.blit(self.no_Devices, text_rect)
        
        for button in self.buttons:
            button.draw(self.screen, mouse_pos)
            if button.is_clicked(mouse_pos, mouse_click):
                if button.text == "Back":
                    self.displayValue = False
                    return button.text
                else:
                    self.update(button.text)
                    self.displayValue = True
                    
            if self.displayValue:
                Vtext = self.font.render(f"Voltage: {self.Voltage}", True, color_dic["white"])
                Ctext = self.font.render(f"Current: {self.Current}", True, color_dic["white"])
                Ptext = self.font.render(f"Power: {self.Power}", True, color_dic["white"])
                    
                text_rect1 = Vtext.get_rect(center=(self.screen.get_width() // 2+100, self.screen.get_height() // 2-100))
                text_rect2 = Ctext.get_rect(center=(self.screen.get_width() // 2+100, self.screen.get_height() // 2))
                text_rect3 = Ptext.get_rect(center=(self.screen.get_width() // 2+100, self.screen.get_height() // 2+100))
                    
                self.screen.blit(Vtext, text_rect1)
                self.screen.blit(Ctext, text_rect2)
                self.screen.blit(Ptext, text_rect3)
            
        return None
    
    def update(self,text):
        address = self.getaddress(text)
        self.Voltage = self.i2c_scanner.GetData(address,'voltage')
        self.Current = self.i2c_scanner.GetData(address,'current')
        self.Power = self.i2c_scanner.GetData(address,'power')
        
    def getaddress(self,text):
        print(text)
        address = next((key for key, value in address_names.items() if value == text),None)
        return address
        
    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.i2c_scanner.close()
                    return "Quit"
                
            self.screen.fill(color_dic["black"])
            result = self.draw()
    
            if result:
                return result
            pygame.display.flip()