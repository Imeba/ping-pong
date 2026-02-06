from pygame import *

window = display.set_mode((700,500))
clock = time.Clock()
fps = 60
end = True
while end:
    for i in event.get():
        if i.type == QUIT:
            end = False
    window.fill((71, 158, 49))
    clock.tick(fps)
    display.update()