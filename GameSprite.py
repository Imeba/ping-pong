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