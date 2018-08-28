import pygame

pygame.init()

white = (255,255,255) # color defines int the RGB formate
black = (0,0,0)
red = (255,0,0)
gameDisplay = pygame.display.set_mode((800, 600))
pygame.display.set_caption('SNAKE GAME')

gameExit = False

lead_x = 300
lead_y = 300
lead_x_change = 0
lead_y_change = 0
clock = pygame.time.Clock()
while not gameExit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                lead_x_change   =  -10
                
            if  event.key ==  pygame.K_RIGHT:
                lead_x_change  = 10

         #if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                lead_y_change   =  -10
                
            if  event.key ==  pygame.K_DOWN:
                lead_y_change  = 10

        if event.type == pygame.KEYUP:
            if event.key ==pygame.K_LEFT or  event.key == pygame.K_RIGHT:
                lead_x_change = 0

        #if event.type == pygame.KEYUP:
            if event.key ==pygame.K_UP or  event.key == pygame.K_DOWN:
                lead_y_change = 0
            

    lead_x += lead_x_change
    lead_y += lead_y_change    
            
    gameDisplay.fill(white) #fill the desktop background with the color passed as the argument 
    pygame.draw.rect(gameDisplay, black, [lead_x,lead_y,10,10]) #draw rectangle 
    #gameDisplay.fill(red, rect=[200,200,50,50]) #draw rectangle but the method is different and faster than the previous one

    
    pygame.display.update() #update the background
    clock.tick(15)
pygame.quit()
quit()
