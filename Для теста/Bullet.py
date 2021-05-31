from Parameters import *

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