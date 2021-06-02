import pygame

pygame.init()

background = pygame.image.load("Assets/Background/Space Background1.png").convert_alpha()

icon = pygame.image.load("Assets/12.png").convert_alpha()

player = pygame.image.load("Assets/Player/Ship6.png").convert_alpha()
shoot = pygame.image.load("Assets/Player/shoots/shot5_asset.png").convert_alpha()

player_state = [pygame.image.load("Assets/Player/Fire/state/exhaust1.png").convert_alpha(),
                pygame.image.load("Assets/Player/Fire/state/exhaust2.png").convert_alpha(),
                pygame.image.load("Assets/Player/Fire/state/exhaust3.png").convert_alpha(),
                pygame.image.load("Assets/Player/Fire/state/exhaust4.png").convert_alpha()
                ]

player_moving = [pygame.image.load("Assets/Player/Fire/Flight/exhaust1.png").convert_alpha(),
                pygame.image.load("Assets/Player/Fire/Flight/exhaust2.png").convert_alpha(),
                pygame.image.load("Assets/Player/Fire/Flight/exhaust3.png").convert_alpha(),
                pygame.image.load("Assets/Player/Fire/Flight/exhaust4.png").convert_alpha()]


enemysimg = [pygame.image.load("Assets/Enemys/Ship1.png").convert_alpha(),
             pygame.image.load("Assets/Enemys/Ship2.png").convert_alpha(),
             pygame.image.load("Assets/Enemys/Ship3.png").convert_alpha(),
             pygame.image.load("Assets/Enemys/Ship4.png").convert_alpha(),
             pygame.image.load("Assets/Enemys/Ship5.png").convert_alpha()]

enemy_moving_1 =[pygame.image.load("Assets/Enemys/Ship1/Ship1_turbol_flight_001.png").convert_alpha(),
                 pygame.image.load("Assets/Enemys/Ship1/Ship1_turbol_flight_003.png").convert_alpha(),
                 pygame.image.load("Assets/Enemys/Ship1/Ship1_turbol_flight_005.png").convert_alpha(),
                 pygame.image.load("Assets/Enemys/Ship1/Ship1_turbol_flight_007.png").convert_alpha()]

enemy_moving_2 =[pygame.image.load("Assets/Enemys/Ship2/Ship2_turbo_flight_001.png").convert_alpha(),
                 pygame.image.load("Assets/Enemys/Ship2/Ship2_turbo_flight_003.png").convert_alpha(),
                 pygame.image.load("Assets/Enemys/Ship2/Ship2_turbo_flight_005.png").convert_alpha(),
                 pygame.image.load("Assets/Enemys/Ship2/Ship2_turbo_flight_007.png").convert_alpha()]

enemy_moving_3 =[pygame.image.load("Assets/Enemys/Ship3/Ship3_turbo_flight_001.png").convert_alpha(),
                 pygame.image.load("Assets/Enemys/Ship3/Ship3_turbo_flight_003.png").convert_alpha(),
                 pygame.image.load("Assets/Enemys/Ship3/Ship3_turbo_flight_005.png").convert_alpha(),
                 pygame.image.load("Assets/Enemys/Ship3/Ship3_turbo_flight_007.png").convert_alpha()]

enemy_moving_4 =[pygame.image.load("Assets/Enemys/Ship4/Ship4_turbo_flight_001.png").convert_alpha(),
                 pygame.image.load("Assets/Enemys/Ship4/Ship4_turbo_flight_003.png").convert_alpha(),
                 pygame.image.load("Assets/Enemys/Ship4/Ship4_turbo_flight_005.png").convert_alpha(),
                 pygame.image.load("Assets/Enemys/Ship4/Ship4_turbo_flight_007.png").convert_alpha()]

enemy_moving_5 =[pygame.image.load("Assets/Enemys/Ship5/Ship5_turbo_flight_001.png").convert_alpha(),
                 pygame.image.load("Assets/Enemys/Ship5/Ship5_turbo_flight_003.png").convert_alpha(),
                 pygame.image.load("Assets/Enemys/Ship5/Ship5_turbo_flight_005.png").convert_alpha(),
                 pygame.image.load("Assets/Enemys/Ship5/Ship5_turbo_flight_007.png").convert_alpha()]






menu_bckgr = pygame.image.load("Assets/menu/menu.jpg")

shop_button = pygame.image.load("Assets/shop/cog.png")
shop_button_inact = pygame.image.load("Assets/shop/cog_a.png")
shop = pygame.image.load("Assets/shop/background.png")

