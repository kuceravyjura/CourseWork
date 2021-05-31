from Parameters import *

class Vampus:
    def __init__(self, x, y, width, height, speed, image, personal_width, personal_height, health):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = speed
        self.image = image
        self.bottom = self.y + personal_height
        self.back = self.x + personal_width
        self.health = health

    def move(self):
        if self.x >= -self.width:
            screen.blit(self.image, (self.x, self.y))
            self.x -= self.speed
            self.back -= self.speed