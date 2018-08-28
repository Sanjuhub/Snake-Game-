# from video 18 Mor apple and snake functions

import pygame
import time
import random

pygame.init()

white = (255,255,255) # color defines in the RGB formate
black = (0,0,0)
red = (255,0,0)
green = (0, 255, 0)

display_width = 800
display_hight = 600
gameDisplay = pygame.display.set_mode((display_width, display_hight))
pygame.display.set_caption('SNAKE GAME')



block_size =10
clock = pygame.time.Clock()
fps = 30

font = pygame.font.SysFont(None, 20)

def snake(block_size, snakelist):
    for XnY in snakelist:
        pygame.draw.rect(gameDisplay, green, [XnY[0],XnY[1 ], block_size,block_size])


def message_to_screen(msg, color):
    screen_text = font.render(msg, True, color)
    gameDisplay.blit(screen_text,[display_width/2, display_hight/2])
    
def gameLoop():
    gameExit = False
    gameOver = False

    lead_x = display_width/2
    lead_y = display_hight/2

    lead_x_change = 0
    lead_y_change = 0

    snakelist = []
    snakeLength = 1

    randAppleX = round(random.randrange(0, display_width - block_size)/10.0)*10.0
    randAppleY = round(random.randrange(0, display_hight - block_size)/10.0)*10.0
    
    AppleThickness = 30
    
    while not gameExit:

        while gameOver == True:
            gameDisplay.fill(white)
            message_to_screen("Game Over !!!. Press C to continue or Q to quit the game.", red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type ==  pygame.QUIT:
                    gameOver = False
                    gameExit = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameExit = True
                        gameOver =  False
                    if event.key == pygame.K_c:
                        gameLoop()
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    lead_x_change   =  -block_size
                    lead_y_change   =  0
                    
                elif  event.key ==  pygame.K_RIGHT:
                    lead_x_change  = block_size
                    lead_y_change   =  0
             
                elif event.key == pygame.K_UP:
                    lead_y_change   =  -block_size
                    lead_x_change  = 0
                    
                elif  event.key ==  pygame.K_DOWN:
                    lead_y_change  = block_size
                    lead_x_change  = 0

        if lead_x >=display_width or lead_x < 0 or lead_y >= display_hight or lead_y < 0:
            gameOver = True
           

        lead_x += lead_x_change
        lead_y += lead_y_change    

                
        gameDisplay.fill(black) #fill the desktop background with the color passed as the argument 
        pygame.draw.rect(gameDisplay, red , [randAppleX, randAppleY, AppleThickness, AppleThickness])

       
        sankeHead = []
        sankeHead.append(lead_x)
        sankeHead.append(lead_y)
        snakelist.append(sankeHead)
        
        if len(snakelist) > snakeLength:
            del snakelist[0]

        for eachSegment in snakelist[:-1]:
            if eachSegment == sankeHead:
                gameOver = True
            
        
        snake(block_size, snakelist)
        #gameDisplay.fill(red, rect=[200,200,50,50]) #draw rectangle but the method is different and faster than the previous one
        pygame.display.update() #update the background



##        if lead_x >= randAppleX and lead_x <= randAppleX + AppleThickness:
##            if lead_y >= randAppleY and lead_y <= randAppleY + AppleThickness:
##                randAppleX = round(random.randrange(0, display_width - block_size))#/10.0)*10.0
##                randAppleY = round(random.randrange(0, display_hight - block_size))#/10.0)*10.0
##                snakeLength += 1
            
            
        clock.tick(fps)

    
    pygame.quit()
    quit()
gameLoop()

