import pygame  
  
pygame.init()  
screen = pygame.display.set_mode((1000, 700))  
done = False  
x = 30  
y = 30  
  
while not done:  
    for event in pygame.event.get():  
        if event.type == pygame.QUIT:  
            done = True  
        
     
    print("Enter the number")
    a=input()
    if a == 1:
        x-=1
    if a == 2:
        x+=1        
  
    if is_blue:  
        color = (0, 128, 255)  
    else:   
        color = (255, 100, 0)  
    pygame.draw.rect(screen, color, pygame.Rect(x, y, 40, 40))  
  
    pygame.display.flip()  
