import math
import pygame
import random
import arcade

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
enemysimg = [pygame.image.load("Assets/Enemys/Ship1.png").convert_alpha(),
             pygame.image.load("Assets/Enemys/Ship2.png").convert_alpha(),
             pygame.image.load("Assets/Enemys/Ship3.png").convert_alpha(),
             pygame.image.load("Assets/Enemys/Ship4.png").convert_alpha(),
             pygame.image.load("Assets/Enemys/Ship5.png").convert_alpha()]

spawn_delay = 100


class Vampus:
    def __init__(self, x, y, width, height, speed, image, index):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = speed
        self.image = image
        self.index = index

    def move(self):
        if self.x >= -self.width:
            screen.blit(self.image, (self.x, self.y))
            self.x -= self.speed


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
vampus_arr = []


def run_game():
    global shooting, event, playerpos1, position, armorvalue, healthvalue, pause, spawn_delay
    game = True
    index = 0
    shoots = []
    count = 10
    spawn_rate = count // 10
    while game:
        spawn_delay -= spawn_rate
        if spawn_delay <= 0:
            create_vampus_arr(vampus_arr, index)
            index += 1
            spawn_delay = 100
            count += 1

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

        # draw_arr(vampus_arr)
        collision(vampus_arr, shoots)
        draw_Attack(shoots)
        Pause()
        pygame.display.flip()


def create_vampus_arr(array, index):
    rnd = random.randint(0, 4)
    img = enemysimg[rnd]
    array.append(Vampus(1100, random.randint(20, 600), 45, 30, 4, img, index))


# def draw_arr(array):
#     for vampus in array:
#         index = 0
#         vampus.move()
#         if vampus.x < -64:
#             if armorvalue > 0:
#                 armorvalue -= 35
#                 array.pop(index)
#             else:
#                 healthvalue -= 15
#                 array.pop(index)


def Attack(array):
    global playerpos, shoots, event, shooting, playerpos1
    position = pygame.mouse.get_pos()
    array.append([math.atan2(
                  position[1] - (playerpos1[1] + 32),
                  position[0] - (playerpos1[0] + 32)),
                  playerpos1[0] + 50,
                  playerpos1[1] - 24])
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
        print_text('Paused. Press P to continue', 500, 10)
        pygame.display.flip()
        clock.tick(20)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    pause = not pause


def print_text(massage, x, y, font_color=(30, 255, 50), font_type='Art-Metropol.ttf', font_size=35):
    font_type = pygame.font.Font(font_type, font_size)
    text = font_type.render(massage, True, font_color)
    screen.blit(text, (x, y))


def collision(array_1, array_2):

    for vampus in array_1:
        badrect = pygame.Rect(vampus.image.get_rect())
        badrect.top = vampus.y
        badrect.left = vampus.x
        index = 0
        vampus.move()
        if vampus.x < -64:
            if armorvalue > 0:
                armorvalue -= 35
                array_1.pop(index)
            else:
                healthvalue -= 15
                array_1.pop(index)
        index1 = 0
        for bullet in array_2:
            bullrect = pygame.Rect(shoot.get_rect())

            bullrect.left = bullet[0]
            bullrect.top = bullet[1]
            if arcade.check_for_collision_with_list(bullet, array_1):
                array_1.pop(index)
                array_2.pop(index1)
            index1 += 1
        # index += 1


run_game()
