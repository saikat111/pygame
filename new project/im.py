import pygame
pygame.init()
pygame.display.set_caption("Hello")
screen = pygame.display.set_mode((960,540))
color =(255, 255, 255)
x =0
y = 0
z = 50
p = 50
o = 200
m = 200



while True:
    event = pygame.event.wait()
    if event.type == pygame.QUIT:
        break
    if event.type == pygame.KEYDOWN:
        key_name = pygame.key.name(event.key)
        print(key_name)
        if z == m or p == o :
            break;
        if key_name == "up":
            p -=10
        if key_name == "down":
            p +=10
        if key_name == "right":
            z +=10
        if key_name == "left":
            z -=10
        if key_name == "w":
            m -=10
        if key_name == "s":
            m +=10
        if key_name == "d":
            o +=10
        if key_name == "a":
            o -=10


    i=pygame.image.load("k.png").convert()
    b=pygame.image.load("saikat.jpg").convert()
    screen.blit(b,(x,y))
    screen.blit(i,(z,p))
    screen.blit(i,(o,m))
    pygame.display.flip()
