from pygame import *
from GameSprite import *

window = display.set_mode((700,500))
clock = time.Clock()
fps = 60
end = True
player1 = Player(30,275,'rocket.png',4,80,10,window)
player2 = Player(660,265,'rocket.png',4,80,10,window)
while end:
    for i in event.get():
        if i.type == QUIT:
            end = False
    window.fill((71, 158, 49))
    player1.draw()
    player2.draw()
    player1.move()
    player2.move1()
    clock.tick(fps)
    display.update()