import pygame

pygame.init()

background = pygame.image.load("Assets/Background/Space Background.png").convert_alpha()

icon = pygame.image.load("Assets/12.png").convert_alpha()

player = pygame.image.load("Assets/Player/Ship6.png").convert_alpha()
shoot = pygame.image.load("Assets/Player/shoots/shot5_asset.png").convert_alpha()

enemysimg = [pygame.image.load("Assets/Enemys/Ship1.png").convert_alpha(),
             pygame.image.load("Assets/Enemys/Ship2.png").convert_alpha(),
             pygame.image.load("Assets/Enemys/Ship3.png").convert_alpha(),
             pygame.image.load("Assets/Enemys/Ship4.png").convert_alpha(),
             pygame.image.load("Assets/Enemys/Ship5.png").convert_alpha()]


menu_bckgr = pygame.image.load("Assets/menu/menu.jpg")

shop_button = pygame.image.load("Assets/shop/cog.png")
shop_button_inact = pygame.image.load("Assets/shop/cog_a.png")
shop = pygame.image.load("Assets/shop/background.png")