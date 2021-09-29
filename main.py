import pygame
import random



#############################################
running = True
caption = "Array sort"
FPS = 25
displayY = 800
displayX = 1600

BarstartPos = random.randint(20,displayY)
berWidth = 10
berAmmout = displayX/berWidth
#############################################

display = pygame.display.set_mode((displayX,displayY))
clock = pygame.time.Clock()
pygame.display.set_caption(caption)
#############################################
#############################################

WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
CYAN = (0,255,255)


#############################################

def genBars(berammount):
    berList= []
    BarstartX = 0
    for i in range(round(berammount)):
        nBer = []
        BarstartY = random.randint(0,displayY)

        nBer.append(BarstartX)
        nBer.append(BarstartY)
        berList.append(nBer)
        BarstartX += berWidth
    
    
    return berList


def drawBars(berList=list):
    for bar in berList:
        for j in bar:
            pygame.draw.line(display, GREEN, (bar[0],bar[1]), (bar[0],displayY), berWidth)




def sortArray(array=list):
    for index,ber in enumerate(array):
        try:
            if index < len(array)-1:
                if ber[1] < array[index+1][1]:
                    # print(array[index+1])
                    pygame.draw.line(display, RED, (array[index+1][0],array[index+1][1]), (array[index+1][0],displayY), berWidth)
                    tampNext = array[index][1]
                    array[index][1] = array[index+1][1]
                    array[index+1][1] = tampNext
                    # break 
        except Exception as e:
            print(e)
            pass



#############################################
berlist = genBars(berAmmout)

drawBars(berlist)
while running:
    # sort2 (berlist)
    display.fill((0,0,0))
    drawBars(berlist)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
                exit()
            
            if event.key == pygame.K_r:
                berlist = genBars(berAmmout)

    sortArray(berlist)
    clock.tick(FPS)
    pygame.display.update()
    
        




