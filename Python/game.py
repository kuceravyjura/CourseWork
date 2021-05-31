from Effects import *
from image import *
from Parameters import *
from Button import *
from Bullet import *
from Vampus import *
from Souds import *
from State import *
import random


class Game:
    def __init__(self):
        pygame.display.set_caption("Space Sindicate")
        pygame.display.set_icon(icon)

        self.keys = [False, False, False, False]
        self.shooting = False
        self.pause = False
        self.upgrade = False

        self.vampus_arr = []

        self.playerspeed = 8
        self.healthvalue = 130
        self.armorvalue = 130
        self.damage = 1
        self.proj_num = 1

        self.scores = 0

        self.game_state = GameState()

    def start(self):
        if self.game_state.check(State.Menu):
            self.show_menu()
        elif self.game_state.check(State.START):
            self.start_game()
        elif self.game_state.check(State.CONTINUE):
            pass
        elif self.game_state.check(State.QUIT):
            pass

    def show_menu(self):
        start_btn = Button(278, 70)
        quit_btn = Button(278, 70)

        show = True
        while show:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            screen.blit(menu_bckgr, (-400, -100))
            start_btn.draw(365, 200, 'New game', self.start_game, 50)
            quit_btn.draw(365, 300, 'Quit', quit, 50, 90)

            pygame.display.flip()
            clock.tick(60)

    def start_game(self):
        global playerpos
        while self.game_cicle():
            self.scores = 0
            self.healthvalue = 300
            self.playerspeed = 8
            self.armorvalue = 210
            playerpos = [100, 100]


    def return_from_shop(self):
        self.upgrade = False

    def upgrade_damage(self):
        price = (50 * self.damage)
        if self.scores >= price:
            self.damage += 0.5
            self.scores -= price
            pygame.time.delay(300)

    def upgrade_speed(self):
        price = 50 * (self.playerspeed // 4)
        if self.scores >= price:
            self.playerspeed += 1
            self.scores -= price
            pygame.time.delay(300)

    def upgrade_proj_num(self):
        global proj_button_str
        self.scores += 300
        if self.scores >= 50 and self.proj_num<3:
            self.proj_num += 2
            self.scores -= 50
            pygame.time.delay(300)
        elif self.scores >= 100 and 3 == self.proj_num:
            self.proj_num += 2
            self.scores -= 100
            pygame.time.delay(300)
        elif self.proj_num == 5:
            proj_button_str = str("  MAX")

    def Repair_hull(self):
        global healthbar_str
        if self.scores >= 10:
            if self.healthvalue < 300:
                self.healthvalue += 5
                self.scores -= 10
                pygame.time.delay(300)

    def Repair_armor(self):
        global armorbar_str
        if self.scores >= 2:
            if self.armorvalue < 210:
                self.armorvalue += 5
                if self.armorvalue > 210:
                    self.armorvalue = 210
                self.scores -= 2
                pygame.time.delay(300)

    def upgrade_menu(self):
        global proj_button_str, healthbar_str, armorbar_str
        button_exit = Button(142, 77, active_color=(241, 126, 142), inactive_color=(31, 12, 222))
        button_repair = Button(531, 68, active_color=(83, 20, 60), inactive_color=(31, 12, 222))
        button_upgrade_speed = Button(531, 68, active_color=(83, 20, 60), inactive_color=(31, 12, 222))
        button_upgrade_damage = Button(531, 68, active_color=(83, 20, 60), inactive_color=(31, 12, 222))
        button_upgrade_extra_proj = Button(531, 68, active_color=(83, 20, 60), inactive_color=(31, 12, 222))
        button_repair_hull = Button(531, 68, active_color=(83, 20, 60), inactive_color=(31, 12, 222))
        self.shooting = False
        self.upgrade = True
        proj_button_str = str("+projectiles")
        healthbar_str = str("Repair Hull +5")
        armorbar_str = str("Repair armor +5")
        while self.upgrade:

            screen.blit(shop, (0,0))

            button_exit.draw(46, 542, "Return", self.return_from_shop, text_pos_y = 14, text_pos_x= 14, font_size = 40)
            button_repair.draw(38, 325, armorbar_str ,self.Repair_armor , text_pos_y = 7, text_pos_x= 70, font_size = 50)
            button_upgrade_speed.draw(38, 228, "+speed",self.upgrade_speed , text_pos_y = 7, text_pos_x= 190, font_size = 50)
            button_upgrade_damage.draw(38, 128,"+Damage",self.upgrade_damage , text_pos_y = 7, text_pos_x= 180, font_size = 50)
            button_upgrade_extra_proj.draw(37, 30, proj_button_str, self.upgrade_proj_num, text_pos_y = 7, text_pos_x= 170, font_size = 50)
            button_repair_hull.draw(38,424, healthbar_str, self.Repair_hull, text_pos_y = 7, text_pos_x= 78, font_size = 50)


            print_text("Player stats:", 670, 350)
            print_text("Hull:  " + str(self.healthvalue), 630, 400)
            print_text("Armor: " + str(self.armorvalue), 630, 445)
            print_text("Speed:   " + str(self.playerspeed), 630, 490)
            print_text("Damage:  " + str(self.damage), 630, 535)
            print_text("Projectile number:"+ str(self.proj_num), 630, 580)
            print_text("Money: "+str(self.scores), 350, 550, font_size=45)

            screen.blit(player, (700, 130))
            screen.blit(shoot, (820, 165))


            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.upgrade = False

    def game_cicle(self):
        global event, position, spawn_delay, ATTACK_DELAY
        game = True
        index = 0
        shoots = []
        count = 10
        spawn_rate = count // 10
        upgr_button = Button(32, 32, shop_button, shop_button_inact)
        while game:

            ATTACK_DELAY -= 1
            spawn_delay -= spawn_rate
            if spawn_delay <= 0:
                self.create_vampus_arr(self.vampus_arr, index)
                index += 1
                spawn_delay = 100
                count += 1

            clock.tick(60)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_w:
                        self.keys[0] = True
                    elif event.key == pygame.K_a:
                        self.keys[1] = True
                    elif event.key == pygame.K_s:
                        self.keys[2] = True
                    elif event.key == pygame.K_d:
                        self.keys[3] = True
                    elif event.key == pygame.K_p:
                        self.Pause()
                    elif event.key == pygame.K_SPACE:
                        self.shooting = True
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_w:
                        self.keys[0] = False
                    elif event.key == pygame.K_a:
                        self.keys[1] = False
                    elif event.key == pygame.K_s:
                        self.keys[2] = False
                    elif event.key == pygame.K_d:
                        self.keys[3] = False
                    elif event.key == pygame.K_SPACE:
                        self.shooting = False
            if self.keys[0]:
                playerpos[1] -= self.playerspeed
            elif self.keys[2]:
                playerpos[1] += self.playerspeed
            if self.keys[1]:
                playerpos[0] -= self.playerspeed
            elif self.keys[3]:
                playerpos[0] += self.playerspeed
            if self.shooting:
                self.Attack(shoots)

            screen.fill(0)
            screen.blit(background, (0, 0))
            screen.blit(player, (playerpos[0], playerpos[1]))



            self.draw_arr(self.vampus_arr)
            self.Bul_update(shoots)
            self.Collision_check(self.vampus_arr, shoots)
            self.bars()

            upgr_button.draw(20, 100, message=None, action = self.upgrade_menu)
            print_text("Upgrade",15, 130, font_size=15)

            print_text("Score: " + str(self.scores), 10, 20)
            pygame.display.flip()
            if self.healthvalue <= 0:
                game = False

        return self.game_over()

    @staticmethod
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

        array.append(Vampus(1100, random.randint(20, 600), Width, Height, random.randint(4, 9), img, personal_width,
                            personal_height, 3))


    def draw_arr(self, array):
        for vampus in array:
            index = 0
            vampus.move()
            if vampus.x < -64:
                if self.armorvalue > 0:
                    self.armorvalue -= 35
                    if self.armorvalue <0:
                        self.armorvalue = 0
                    array.pop(index)
                else:
                    self.healthvalue -= 15
                    array.pop(index)


    def Attack(self, array):
        global event, playerpos, shoot, ATTACK_DELAY
        if ATTACK_DELAY <= 0:
            array.append(Bullet(playerpos[0] + 80, playerpos[1] + 36, 1000, 680, 31, 6, 7, shoot))
            ATTACK_DELAY = 8
            if self.proj_num >= 3:
                array.append(Bullet(playerpos[0] + 60, playerpos[1] + 10, 1000, 680, 31, 6, 7, shoot))
                array.append(Bullet(playerpos[0] + 60, playerpos[1] + 65, 1000, 680, 31, 6, 7, shoot))
                if self.proj_num == 5:
                    array.append(Bullet(playerpos[0] + 35, playerpos[1] - 10, 1000, 680, 31, 6, 7, shoot))
                    array.append(Bullet(playerpos[0] + 35, playerpos[1] + 90, 1000, 680, 31, 6, 7, shoot))


        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                self.shooting = False

    @staticmethod
    def Bul_update(array):
        index = 0
        for bullet in array:
            Bullet.move(bullet)
            if bullet.x > bullet.width:
                array.pop(index)
            index += 1


    def Collision_check(self, array_1, array_2):
        for enemy in array_1:
            enemy_index = 0
            index = 0
            for bullet in array_2:
                if (enemy.x < bullet.x) and (bullet.back < enemy.back):
                    if (bullet.bottom < enemy.bottom and bullet.bottom > enemy.y) or \
                            (bullet.top > enemy.y and bullet.top < enemy.bottom):
                        array_2.pop(index)
                        enemy.health -= self.damage
                        if enemy.health <= 0:
                            array_1.pop(enemy_index)
                        self.scores += 1
                index += 1
            enemy_index += 1


    def Pause(self):
        self.pause = True
        while self.pause:
            print_text('Paused. Press P to continue', 500, 10)
            pygame.display.flip()
            clock.tick(20)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p:
                        self.pause = not self.pause

    @staticmethod
    def game_over():
        stop = True
        while stop:
            print_text('Game Over', 300, 200, font_size= 70)
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


    def bars(self):
        pygame.draw.rect(screen, (200, 0, 0), (playerpos[0] - 5, playerpos[1] - 10, 130, 5))
        for health1 in range(self.healthvalue):
            pygame.draw.rect(screen, (0, 200, 0), (playerpos[0] - 5 + health1, playerpos[1] - 10, 2, 5))

        for armor1 in range(self.armorvalue):
            pygame.draw.rect(screen, (0, 0, 210), (playerpos[0] - 5 + armor1, playerpos[1] - 10, 2, 5))
