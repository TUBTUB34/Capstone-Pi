import pygame
from MainMenu_Class import MainMenu
from Monitor_Class import Monitor


def main():
    
    pygame.init()
    screen_width = 800
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    what_screen = "Main_Menu"
    pygame.display.set_caption(what_screen)
    
    while True:
        if what_screen == "Main_Menu":
            menu = MainMenu(screen)
            result = menu.run()
            if result == "Monitor":
                what_screen = "Monitor"
            elif result == "View":
                print("I Had put something in here")
            elif result == "Quit":
                break
            
        elif what_screen == "Monitor":
            monitor = Monitor(screen)
            result = monitor.run()
            if result == "Back":
                what_screen = "Main_Menu"
            elif result == "Quit":
                break
            
    pygame.quit()
        
if __name__ == "__main__":
    main()