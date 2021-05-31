# import math
import pygame
import random

# import arcade

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
ATTACK_DELAY = 0


class Vampus:
    def __init__(self, x, y, width, height, speed, image, personal_width, personal_height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = speed
        self.image = image
        self.bottom = self.y + personal_height
        self.back = self.x + personal_width

    def move(self):
        if self.x >= -self.width:
            screen.blit(self.image, (self.x, self.y))
            self.x -= self.speed
            self.back -= self.speed


class Bullet:
    def __init__(self, x, y, width, height, bul_width, bul_height, speed, image):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = speed
        self.image = image
        self.bul_width = bul_width
        self.bul_height = bul_height
        self.top = self.y
        self.bottom = self.y + self.bul_height
        self.fow = self.x + self.bul_width
        self.back = self.x

    def move(self):
        if self.x <= self.width:
            screen.blit(self.image, (self.x, self.y))
            self.x += self.speed
            self.back += self.speed


class Button:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.inactive_color = (92, 31, 222)
        self.active_color = (31, 128, 222)
    def draw(self, x, y, message, action = None, font_size = 30, text_pos_x = 10, text_pos_y = 10):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if x < mouse[0] < x+self.width and y < mouse[1] < y+self.height:
            pygame.draw.rect(screen,self.active_color , (x, y, self.width, self.height))
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
            pygame.draw.rect(screen,self.inactive_color , (x, y, self.width, self.height))

        print_text(message = message, x = x + text_pos_x, y = y + text_pos_y , font_size = font_size)

keys = [False, False, False, False]
shooting = False
pause = False
playerpos = [100, 100]

healthvalue = 300
armorvalue = 210
scores = 0
difficult = 5

vampus_width = 20
vampus_height = 70
vampus_x = 900
vampus_y = 100
vampus_arr = []

def show_menu():
    menu_bckgr = pygame.image.load("Assets/menu/menu.jpg")

    start_btn = Button(278, 70)
    quit_btn = Button(278, 70)

    show = True
    while show:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        screen.blit(menu_bckgr, (-400, -100))
        start_btn.draw(365, 200, 'Start game', start_game, 50)
        quit_btn.draw(365, 300, 'Quit', quit, 50, 90)


        pygame.display.flip()
        clock.tick(60)

def start_game():
    global  scores, healthvalue, armorvalue, playerpos
    while game_cicle():
        scores = 0
        healthvalue = 300
        armorvalue = 210
        playerpos = [100, 100]

def game_cicle():
    global shooting, event, position, armorvalue, healthvalue, pause, spawn_delay, ATTACK_DELAY
    game = True
    index = 0
    shoots = []
    count = 10
    spawn_rate = count // 10
    button = Button(100, 50)
    while game:
        ATTACK_DELAY -= 1
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
                shooting = True
            if event.type == pygame.MOUSEBUTTONUP:
                shooting = False
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
                    Pause()
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
            playerpos[1] -= 8
        elif keys[2]:
            playerpos[1] += 8
        if keys[1]:
            playerpos[0] -= 8
        elif keys[3]:
            playerpos[0] += 8
        if shooting:
            Attack(shoots)

        screen.fill(0)
        screen.blit(background, (0, 0))
        screen.blit(player, (playerpos[0], playerpos[1]))

        button.draw(20, 100, "Wow")

        draw_arr(vampus_arr)
        Bul_update(shoots)
        Collision_check(vampus_arr, shoots)
        bars()

        print_text("Score: "+ str(scores), 10, 20)
        pygame.display.flip()
        if healthvalue <=0:
            game = False
    return game_over()


def create_vampus_arr(array, index):
    personal_width, personal_height = 80, 40
    rnd = random.randint(0, 4)
    img = enemysimg[rnd]
    if rnd == 0:
        personal_width, personal_height = 59, 30
    elif rnd == 1:
        personal_width, personal_height = 78, 35
    elif rnd == 2:
        personal_width, personal_height = 87, 40
    elif rnd == 3:
        personal_width, personal_height = 98, 48
    elif rnd == 4:
        personal_width, personal_height = 104, 64

    array.append(Vampus(1100, random.randint(20, 600),Width, Height, random.randint(4, 9), img, personal_width, personal_height))


def draw_arr(array):
    global healthvalue, armorvalue
    for vampus in array:
        index = 0
        vampus.move()
        if vampus.x < -64:
            if armorvalue > 0:
                armorvalue -= 35
                array.pop(index)
            else:
                healthvalue -= 15
                array.pop(index)


def Attack(array):
    global event, shooting, playerpos, shoot, ATTACK_DELAY
    if ATTACK_DELAY <= 0:
        array.append(Bullet(playerpos[0]+80, playerpos[1]+36, 1000, 680, 31, 6, 7, shoot))
        ATTACK_DELAY = 8
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_SPACE:
            shooting = False


def Bul_update(array):
    index = 0
    for bullet in array:
        Bullet.move(bullet)
        if bullet.x > bullet.width:
            array.pop(index)
        index += 1


def Collision_check(array_1, array_2):
    global scores
    for enemy in array_1:
        enemy_index = 0
        index = 0
        for bullet in array_2:
            if (enemy.x < bullet.x) and (bullet.back < enemy.back):
                if (bullet.bottom < enemy.bottom and bullet.bottom > enemy.y) or\
                        (bullet.top > enemy.y and bullet.top < enemy.bottom):
                    array_2.pop(index)
                    array_1.pop(enemy_index)
                    scores += 1
            index += 1
        enemy_index += 1


def bars():
    healthbar = pygame.image.load("Assets/Player/Health/Health_Bar_Table.png").convert_alpha()
    health = pygame.image.load("Assets/Player/Health/Health_Dot.png").convert_alpha()
    screen.blit(healthbar, (5, 530))

    for health1 in range(healthvalue):
        screen.blit(health, (health1 + 12, 535))

    armorbar = pygame.image.load("Assets/Player/Health/Armor_Bar_Table.png").convert_alpha()
    armor = pygame.image.load("Assets/Player/Health/Armor_Bar_Dot.png").convert_alpha()
    screen.blit(armorbar, (5, 610))
    for armor1 in range(armorvalue):
        screen.blit(armor, (armor1 + 12, 615))

def Pause():
    pause = True
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

def print_text(message, x, y, font_color=(30, 255, 50), font_type='Art-Metropol.ttf', font_size=35):
    font_type = pygame.font.Font(font_type, font_size)
    text = font_type.render(message, True, font_color)
    screen.blit(text, (x, y))


def game_over():
    stop = True
    while stop:
        print_text('Game Over', 500, 10)
        pygame.display.flip()
        clock.tick(20)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return True
                if event.key == pygame.K_ESCAPEN:
                    return False

show_menu()
pygame.quit()
quit()
