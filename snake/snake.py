import pygame
import time
import random

pygame.init()

display_width = 800
display_height = 600

gameScreen = pygame.display.set_mode((display_width,display_height));
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,155,0)
xcolor = (205,127,50)
blue = (128,0,155)
sblue = (235,206,235)
gold = (255,215,0)

clock = pygame.time.Clock()
FPS = 10

pygame.display.set_caption("KatRaj!!")
img = pygame.image.load('snakehead.png')
apple = pygame.image.load('apple.png')
pygame.display.set_icon(apple)
smallfont = pygame.font.SysFont("Comicsans", 25)
mediumfont = pygame.font.SysFont("Comicsans", 40)
largefont = pygame.font.SysFont("Comicsans", 80)

def gameintro():
    intro = True
    while intro:
        gameScreen.fill(sblue)
        message_to_screen("Welcome To KatRaj",blue,-100,"large")
        message_to_screen("This is just a normal snake game,  ",black,-20,"small")
        message_to_screen("which u have already played, but ..",black)
        message_to_screen("read the instructions carefully  :)", black,20)
        message_to_screen("Eat an apple to score a point, dont", black,40)
        message_to_screen("cross the boundaries and dont ", black,60 )
        message_to_screen("run into urself", red,80)
        message_to_screen("All the best Katraj", green, 130,"medium")
        message_to_screen("Press SPACE to play and Q to Quit",black,180,"medium")
        message_to_screen("-BY KARTHIK",xcolor,220)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                intro = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    intro = False
                if event.key == pygame.K_SPACE:
                    gameLoop()
    while not intro:
        pygame.quit()
        quit()


def score(score):
    text = smallfont.render("Score : " + str(score),True, black)
    gameScreen.blit(text,(0,0))


def textObject(msg,type,size):
    if size == "small":
        textSurface = smallfont.render(msg, True, type)
    if size == "medium":
        textSurface = mediumfont.render(msg,True,type)
    if size == "large":
        textSurface = largefont.render(msg, True, type)
    return textSurface, textSurface.get_rect()


def message_to_screen(msg,type, y_displace = 0, size = "small"):
    #screen_text = font.render(msg,True,type)
    #gameScreen.blit(screen_text, [display_width/2,display_height/2])
    textSurf, textRect = textObject(msg,type,size)
    textRect.center = (display_width/2),(display_height/2) + y_displace
    gameScreen.blit(textSurf,textRect)


def katraj(size_of_block, snakelist):
    if direction == "Right":
        head = pygame.transform.rotate(img,270)
    if direction == "Left":
        head = pygame.transform.rotate(img,90)
    if direction == "Up":
        head = img
    if direction == "Down":
        head = pygame.transform.rotate(img,180)
    gameScreen.blit(head,(snakelist[-1][0],snakelist[-1][1]))

    for XY in snakelist[:-1]:
        pygame.draw.rect(gameScreen,green,[XY[0],XY[1],size_of_block,size_of_block])


def gameLoop():
    global direction
    direction = "Right"
    gameOver = False
    gameClose = False

    size_of_block = 20
    snakeList = []
    snakeLength = 1
    lead_x_change = 20
    lead_y_change = 0

    randAppleX = round(random.randrange(0,display_width - size_of_block)/20.0)*20.0
    randAppleY = round(random.randrange(0, display_height - size_of_block)/20.0)*20.0

    lead_x = display_width / 2
    lead_y = display_height / 2
    while not gameClose:
        while gameOver == True:
            gameScreen.fill(gold)
            message_to_screen("Kaatteee!!!",red,-50,"large")
            message_to_screen("SPACE otti aadu leda Q otti dobbey", black,50,"medium")
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameClose = True
                    gameOver = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameClose = True
                        gameOver = False
                    if event.key == pygame.K_SPACE:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameClose = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    direction = "Left"
                    lead_x_change = -size_of_block
                    lead_y_change = 0
                if event.key == pygame.K_RIGHT:
                    direction = "Right"
                    lead_x_change = size_of_block
                    lead_y_change = 0
                if event.key == pygame.K_UP:
                    direction = "Up"
                    lead_y_change = -size_of_block
                    lead_x_change = 0
                if event.key == pygame.K_DOWN:
                    direction = "Down"
                    lead_y_change = size_of_block
                    lead_x_change = 0
        lead_x += lead_x_change
        lead_y += lead_y_change
        if lead_x >= 800 or lead_x < 10 or lead_y >= 600 or lead_y <= 0:
            gameOver = True
        gameScreen.fill(white)
        #pygame.draw.rect(gameScreen,red,(randAppleX,randAppleY,size_of_block,size_of_block))
        gameScreen.blit(apple,(randAppleX,randAppleY))
        pygame.display.update()
        snakeHead = []
        snakeHead.append(lead_x)
        snakeHead.append(lead_y)
        snakeList.append(snakeHead)

        if len(snakeList) > snakeLength:
            del snakeList[0]

        for eachSegment in snakeList[:-1]:
            if eachSegment == snakeHead:
                gameOver = True

        katraj(size_of_block, snakeList)
        score(snakeLength-1)
        pygame.display.update()

        if lead_x == randAppleX and lead_y == randAppleY:
            randAppleX = round(random.randrange(0, display_width - size_of_block) / 20.0) * 20.0
            randAppleY = round(random.randrange(0, display_height - size_of_block) / 20.0) * 20.0
            snakeLength += 1

        clock.tick(FPS)


    #message_to_screen("Kaaateeeee!!!!",red)
    #pygame.display.update()
    pygame.quit()
    quit()

gameintro()
#gameLoop()
