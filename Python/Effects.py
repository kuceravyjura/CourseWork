from Parameters import *

def print_text(message, x, y, font_color=(30, 255, 50), font_type='Art-Metropol.ttf', font_size=35):
    font_type = pygame.font.Font(font_type, font_size)
    text = font_type.render(message, True, font_color)
    screen.blit(text, (x, y))