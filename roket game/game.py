import pygame


pygame.display.set_caption("Rocket action")
screen = pygame.display.set_mode((1000,700))
color = (255,255,255)
x = 400
y = 400
e_x = 400
e_y = 100

gameExit = False
while not gameExit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True
        if event.type == pygame.KEYDOWN:
            key_name = pygame.key.name(event.key)
            if y == e_y:
                break
            if key_name == "up":
                y -=20
            if key_name == "down":
                y +=20
            if key_name == "left":
                x -=20
            if key_name == "right":
                x +=20


    screen.fill(color)
    #pygame.display.update()
    rocket = pygame.image.load("rocket.png").convert()
    screen.blit(rocket,(x,y))
    en = pygame.image.load("e.jpg").convert()
    screen.blit(en,(e_x,e_y))
    pygame.display.flip()
