from pygame import *


class GameSprite(sprite.Sprite):
    def __init__(self,x,y,picture,speed,h,w,windows):
        self.picture = transform.scale(image.load(picture),(w,h))
        self.rect = self.picture.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed
        self.windows = windows
        super().__init__()
class Player(GameSprite):
    def move(self):
        key_press = key.get_pressed()
        if key_press[K_w] and self.rect.y > 5:
            self.rect.y -= 10
        if key_press[K_s] and self.rect.y < 415:
            self.rect.y += 10
    def move1(self):
        key_press = key.get_pressed()
        if key_press[K_UP] and self.rect.y > 5:
            self.rect.y -= 10
        if key_press[K_DOWN] and self.rect.y < 415:
            self.rect.y += 10
    def draw(self):
        self.windows.blit(self.picture,(self.rect.x,self.rect.y))
class Ball(GameSprite):
    cont1 = 0
    cont2 = 0
    speed_x = 2
    speed_y = 2
    def moving(self):
        self.rect.x -= self.speed_x
        self.rect.y -= self.speed_y
    def o(self,pl1,pl2):
        if self.rect.y < 475:
            self.speed_y *= -1
        if self.rect.y > 5:
            self.speed_y *= -1
        sprites_list = sprite.collide_rect(self,pl1)
        sprites_list1 = sprite.collide_rect(self,pl2)
        if sprites_list == True or sprites_list1 == True:
            self.speed_x *= -1
        if self.rect.x <= 0:
            self.cont2 += 1
            self.rect.x = 340
            self.rect.y = 235
        if self.rect.x >=700:
            self.cont1 += 1
            self.rect.x = 340
            self.rect.y = 235

    def draw(self):
        self.windows.blit(self.picture,(self.rect.x,self.rect.y))