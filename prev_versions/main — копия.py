import math

import pygame
import random

# import pyinstaller


pygame.init()

clock = pygame.time.Clock()
Width, Height = 1000, 680
screen = pygame.display.set_mode((Width, Height))
background = pygame.image.load("Assets/Background/Space Background.png").convert_alpha()
pygame.display.set_caption("Space Sindicate")
icon = pygame.image.load("Assets/12.png").convert_alpha()
pygame.display.set_icon(icon)

player = pygame.image.load("Assets/Player/Ship6.png").convert_alpha()
shoot = pygame.image.load("Assets/Player/shoots/shot5_asset.png").convert_alpha()
enemysimg1 = pygame.image.load("Assets/Enemys/Ship1.png").convert_alpha()
enemysimg = enemysimg1


class Vampus:
    def __init__(self, x, y, width, height, speed):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = speed

    def move(self):
        if self.x >= -self.width:
            pygame.draw.rect(screen, (100, 255, 31), (self.x, self.y, self.width, self.height))
            self.x -= self.speed
        else:
            self.x = 900


keys = [False, False, False, False]
shooting = False
pause = False
playerpos = [100, 100]

healthvalue = 300
armorvalue = 210
difficult = 5

vampus_width = 20
vampus_height = 70
vampus_x = 900
vampus_y = 100


def run_game():
    global shooting, event, playerpos1, position, armorvalue, healthvalue, pause
    game = True
    vampus_arr = []
    shoots = []
    create_vampus_arr(vampus_arr)
    while game:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                space = True
            if event.type == pygame.MOUSEBUTTONUP:
                space = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    keys[0] = True
                elif event.key == pygame.K_a:
                    keys[1] = True
                elif event.key == pygame.K_s:
                    keys[2] = True
                elif event.key == pygame.K_d:
                    keys[3] = True
                elif event.key == pygame.K_p:
                    pause = not pause
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    keys[0] = False
                elif event.key == pygame.K_a:
                    keys[1] = False
                elif event.key == pygame.K_s:
                    keys[2] = False
                elif event.key == pygame.K_d:
                    keys[3] = False
        if keys[0]:
            playerpos[1] -= 5
        elif keys[2]:
            playerpos[1] += 5
        if keys[1]:
            playerpos[0] -= 5
        elif keys[3]:
            playerpos[0] += 5
        if space:
            Attack(shoots)

        screen.fill(0)
        screen.blit(background, (0, 0))
        position = pygame.mouse.get_pos()
        angle = math.atan2(position[1] - (playerpos[1] + 32), position[0] - (playerpos[0] + 26))
        playerrot = pygame.transform.rotate(player, 360 - angle * 57.29)
        playerpos1 = (playerpos[0] - playerrot.get_rect().width / 2, playerpos[1] - playerrot.get_rect().height / 2)
        screen.blit(playerrot, playerpos1)

        draw_arr(vampus_arr)
        draw_Attack(shoots)
        Pause()
        pygame.display.flip()


def create_vampus_arr(array):
    array.append(Vampus(900, random.randint(20, 600), 45, 30, 4))


def draw_arr(array):
    for vampus in array:
        vampus.move()


def Attack(array):
    global playerpos, shoots, event, shooting, playerpos1
    position = pygame.mouse.get_pos()
    array.append([math.atan2(
                  position[1] - (playerpos1[1] + 32),
                  position[0] - (playerpos1[0] + 32)),
                  playerpos1[0] + 50,
                  playerpos1[1] + 0])
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_SPACE:
            space = False


def draw_Attack(array):
    for bullet in array:
        index = 0
        velx = math.cos(bullet[0]) * 35
        vely = math.sin(bullet[0]) * 35
        bullet[1] += velx
        bullet[2] += vely
        if bullet[1] < - 64 or bullet[1] > 1000 or bullet[2] < - 64 or bullet[2] > 640:
            array.pop(index)
        index += 1
        for projectile in array:
            arrow1 = pygame.transform.rotate(shoot, 360 - projectile[0] * 57.29)
            screen.blit(arrow1, (projectile[1], projectile[2]))


def Pause():
    global pause
    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    pause = not pause


run_game()
