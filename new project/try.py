import pygame
pygame.init()
pygame.display.set_caption("Hello")
screen = pygame.display.set_mode((400,400))
color =(255,255,255)
x = 30
y = 30
while True:
    event = pygame.event.wait()
    if event.type == pygame.QUIT:
        break
    if event.type == pygame.KEYDOWN:
        key_name = pygame.key.name(event.key)
        print(key_name)
        if key_name == "up":
            y -=5
            
        
        
    pygame.draw.rect(screen, color, pygame.Rect(x,y,40,40))
    pygame.display.flip()
