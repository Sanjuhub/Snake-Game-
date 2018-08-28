import pygame
import time
import random

pygame.init()

white = (255,255,255) # color defines in the RGB formate
black = (0,0,0)
red = (255,0,0)
green = (40, 255, 40)

display_width = 800
display_hight = 600

gameDisplay = pygame.display.set_mode((display_width, display_hight))
pygame.display.set_caption('SNAKE GAME')

img = pygame.image.load('snakehead.png')  #load the image file using the load function 
appleimg = pygame.image.load('apple.png')
block_size =20

AppleThickness = 30

clock = pygame.time.Clock()
fps = 10

direction = "right"

smallfont = pygame.font.SysFont("comicsansms", 25)
medfont = pygame.font.SysFont("comicsansms", 50)
largefont = pygame.font.SysFont("comicsansms", 60)

def pause():
    pause = True
    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key -- pygame.K_c:
                    pause = False
                elif event.key == pygame.K_q:
                    pygame.quit()
                    quit()
        gameDisplay.fill(white)
        message_to_screen("Pause", black, -100,size = "large")

        message_to_screen("Press c to continue or q to quit.", black, 25, )
        pygame.display.update()
        clock.tick(5)
                    

def score(score):
    text = smallfont.render("Score:" +str(score), True , white)
    gameDisplay.blit(text, [0,0])
    

def randAppleGen():
    randAppleX = round(random.randrange(0, display_width - AppleThickness))#/10.0)*10.0
    randAppleY = round(random.randrange(0, display_hight - AppleThickness))#/10.0)*10.0

    return randAppleX, randAppleY


def game_intro():
    intro = True
    while intro:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    intro = False
                if event.key == pygame.K_q:
                    quit()
            
        gameDisplay.fill(white)
        message_to_screen("Welcome to Snake Game", green, -100, "large")

        message_to_screen("The Objective of the is to eat the red Apples", black, -30, "small")
        message_to_screen("The more Apple you eat the longer you get", black, 10, "small")
        message_to_screen("If you run into yourself or the edges, you fail.", black, 50, "small")
        message_to_screen("Press C to play, p to pause or  Q to quit", black, 180, "small")
        pygame.display.update()
        clock.tick(15)
        
def snake(block_size, snakelist):

    if  direction == "right":
        head = pygame.transform.rotate(img, 270)

    if  direction == "left":
        head = pygame.transform.rotate(img, 90)

    if  direction == "up":
        head = img

    if  direction == "down":
        head = pygame.transform.rotate(img, 180)
        
    gameDisplay.blit(head, (snakelist[-1][0], snakelist[-1][1]))

    for XnY in snakelist[:-1]:
        pygame.draw.rect(gameDisplay, green, [XnY[0],XnY[1 ], block_size,block_size])

def text_objects(text, color,size):#this block made the text centered
    if size == "small":
        textSurface = smallfont.render(text, True, color)
    if size == "med":
        textSurface = medfont.render(text, True, color)
    if size == "large":
        textSurface = largefont.render(text, True, color)
    return textSurface, textSurface.get_rect()

def message_to_screen(msg, color,y_displace=0, size = "small"):
    textSurface, textRect = text_objects(msg, color,size)
##    screen_text = font.render(msg, True, color)
##    gameDisplay.blit(screen_text,[display_width/2, display_hight/2])
    textRect.center = (display_width /2) , (display_hight /2) + y_displace
    gameDisplay.blit(textSurface, textRect)

def gameLoop():
    global direction
    direction = 'right'
    
    gameExit = False
    gameOver = False

    lead_x = display_width/2
    lead_y = display_hight/2

    lead_x_change = 0
    lead_y_change = 0

    snakelist = []
    snakeLength = 1

    randAppleX , randAppleY = randAppleGen()
    
    
    while not gameExit:

        while gameOver == True:
            gameDisplay.fill(white)
            message_to_screen("Game Over !!!", red, y_displace= -50,  size = "large")
            message_to_screen("Press C to continue or Q to quit the game.",black, 50,size = "small")
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
                    direction = "left"
                    lead_x_change   =  -block_size
                    lead_y_change   =  0
                    
                elif  event.key ==  pygame.K_RIGHT:
                    direction = "right"
                    lead_x_change  = block_size
                    lead_y_change   =  0
             
                elif event.key == pygame.K_UP:
                    direction = "up"
                    lead_y_change   =  -block_size
                    lead_x_change  = 0
                    
                elif  event.key ==  pygame.K_DOWN:
                    direction = "down"
                    lead_y_change  = block_size
                    lead_x_change  = 0

                elif event.key == pygame.K_p:
                    pause()

        if lead_x >=display_width or lead_x < 0 or lead_y >= display_hight or lead_y < 0:
            gameOver = True
           

        lead_x += lead_x_change
        lead_y += lead_y_change    

                
        gameDisplay.fill(black)   #fill the desktop background with the color passed as the argument 
        #pygame.draw.rect(gameDisplay, red , [randAppleX, randAppleY, AppleThickness, AppleThickness])
        gameDisplay.blit(appleimg , (randAppleX, randAppleY))
       
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
        score(snakeLength-1)
        
        pygame.display.update() #update the background



        if lead_x > randAppleX and lead_x < randAppleX + AppleThickness or lead_x + block_size > randAppleX and lead_x + block_size < randAppleX + AppleThickness:
            
            if lead_y > randAppleY and lead_y < randAppleY + AppleThickness:
                randAppleX , randAppleY = randAppleGen()
                snakeLength += 1
            elif lead_y + block_size > randAppleY and lead_y + block_size < randAppleY + AppleThickness:
                randAppleX , randAppleY = randAppleGen()
                snakeLength += 1
            
        clock.tick(fps)

    
    pygame.quit()
    quit()
game_intro()
gameLoop()

