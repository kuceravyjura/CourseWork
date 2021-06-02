from Effects import *


class Button:
    def __init__(self, width, height, icon = None, inactive_icon = None, active_color = (31, 128, 222), inactive_color = (92, 31, 222)):
        self.width = width
        self.height = height
        self.inactive_color = inactive_color
        self.active_color = active_color
        self.icon = icon
        self.inactive_icon = inactive_icon
    def draw(self, x, y, message, action = None, font_size = 30, text_pos_x = 10, text_pos_y = 10):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if self.icon is None:
            if x < mouse[0] < x+self.width and y < mouse[1] < y+self.height:

                pygame.draw.rect(screen, self.active_color , (x, y, self.width, self.height))
                if click[0] == 1:
                    # pygame.mixer.Sound.play(button_sound)
                    # pygame.time.delay(300)
                    if action is not None:
                        if action == quit:
                            pygame.quit()
                            quit()
                        else:
                            action()
                    else:
                        return True
            else:
                pygame.draw.rect(screen,self.inactive_color , (x, y, self.width, self.height))
        else:
             if x < mouse[0] < x+self.width and y < mouse[1] < y+self.height:
                 screen.blit(self.icon, (x, y))
                 if click[0] == 1:
                     # pygame.mixer.Sound.play(button_sound)
                     # pygame.time.delay(300)
                     if action is not None:
                         if action == quit:
                             pygame.quit()
                             quit()
                         else:
                             action()
             else:
                 screen.blit(self.inactive_icon, (x, y))

        print_text(message = message, x = x + text_pos_x, y = y + text_pos_y , font_size = font_size)

