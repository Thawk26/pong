import pygame

pygame.init()

#INITIALS
WIDTH, HEIGHT = 1900, 1000
wn = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong_ultra")
run = True


#colours  
BLUE = (0, 0, 255) #### to change ####

#for the ball
radius = 30
ball_x, ball_y = WIDTH/2 - radius, HEIGHT/2 - radius


#main loop
while run:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            run = False
        
    pygame.draw.circle(wn, BLUE, (ball_x, ball_y), radius) #change colour and update dimensions
    pygame.display.update()




