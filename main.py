from pygame import *
from GameSprite import *

font.init()
font2 = font.Font(None,40)
font1 = font.Font(None,60)
window = display.set_mode((700,500))
clock = time.Clock()
fps = 60
end = True
player1 = Player(30,275,'rocket.png',4,80,10,window)
player2 = Player(660,265,'rocket.png',4,80,10,window)
ball = Ball(340,235,'ball.png',4,20,20,window)
feedback = True
while end:
    for i in event.get():
        if i.type == QUIT:
            end = False
    if feedback == True:
        window.fill((71, 158, 49))
        player1.draw()
        player2.draw()
        ball.draw()
        player1.move()
        player2.move1()
        ball.moving()
        ball.o(player1,player2)
        counter1 = font2.render('счёт:'+str(ball.cont1),True,(40,0,255))
        counter2 = font2.render('счёт:'+str(ball.cont2),True,(40,0,255))
        window.blit(counter1,(10,10))
        window.blit(counter2,(605,10))
        if ball.cont1 == 3:
            win1 = font1.render('Победил первый игрок',True,(40,0,255))
            window.blit(win1,(140,235))
            feedback = False
        if ball.cont2 == 3:
            win2 = font1.render('Победил второй игрок', True,(40,0,255))
            window.blit(win2,(140,235))
            feedback = False
    clock.tick(fps)
    display.update()