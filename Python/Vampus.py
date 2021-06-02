from Parameters import *

class Vampus:
    def __init__(self, x, y, speed, image, personal_width, personal_height, health, rnd, anim_count = 0):
        self.x = x
        self.y = y
        self.speed = speed
        self.image = image
        self.bottom = self.y + personal_height
        self.back = self.x + personal_width
        self.health = health
        self.rnd = rnd
        self.anim_count = anim_count



    def move(self):
        screen.blit(self.image, (self.x, self.y))
        self.x -= self.speed
        self.back -= self.speed