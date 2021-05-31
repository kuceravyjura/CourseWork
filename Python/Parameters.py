import pygame

clock = pygame.time.Clock()
Width, Height = 1000, 680
screen = pygame.display.set_mode((Width, Height))


spawn_delay = 100
ATTACK_DELAY = 0
playerpos = [100, 100]



difficult = 5

vampus_width = 20
vampus_height = 70
vampus_x = 900
vampus_y = 100