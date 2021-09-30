import pygame
import random
import psutil
from pygame.constants import FULLSCREEN



#############################################
running = True
caption = "Array sort"
FPS = 30

display = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
displayX ,displayY = display.get_size()

BarstartPos = random.randint(20,displayY)
berWidth = 1
berAmmout = displayX/berWidth
#############################################
pygame.init()
clock = pygame.time.Clock()
pygame.display.set_caption(caption)
#############################################
# timer = 100
start = False
itration = 0
time = 0
plushTime = 1
isRevers = False
cpuTime = 0
cpuUseage = psutil.cpu_percent(.0001)
isRedbar = 0
isDone = False
#############################################

WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
CYAN = (0,255,255)
BLUE = (0,0,255)


#############################################

def genBars(berammount):
    berList= []
    BarstartX = 0
    for i in range(round(berammount)):
        nBer = []
        BarstartY = random.randint (0,displayY)
        # BarstartY = BarstartX



        nBer.append(BarstartX)
        nBer.append(BarstartY)
        berList.append(nBer)
        BarstartX += berWidth
    
    # print(berList)
    return berList


def drawBars(berList=list):
    for bar in berList:
        if berWidth >= 5:
            pygame.draw.line(display, WHITE, (bar[0],bar[1]), (bar[0],displayY), berWidth)
        pygame.draw.rect(display, BLUE, ((bar[0]-4,bar[1]), (berWidth,displayY)), 2)




def sortArray(array=list):
    global itration,time,isRedbar,start,plushTime,isDone
    for index,ber in enumerate(array):
        itration += 1
        try:
            if index < len(array)-1:
                if ber[1] < array[index+1][1]:
                    isRedbar += 1
                    # print(array[index+1])
                    pygame.draw.line(display, RED, (array[index+1][0],array[index+1][1]), (array[index+1][0],displayY), berWidth)
                    pygame.draw.rect(display, RED, ((array[index+1][0]-4,array[index+1][1]), (berWidth,displayY)), 1)
                    tampNext = array[index][1]
                    array[index][1] = array[index+1][1]
                    array[index+1][1] = tampNext
                    # break 
        except Exception as e:
            print(e)
            pass
    
    if isRedbar < 1 :
        start = False
        plushTime = 0
        isDone = True
    isRedbar = 0

def sortArrayRevers(array=list):
    global itration,time,isRedbar,start,plushTime,isDone
    for index,ber in enumerate(array):
        itration += 1
        try:
            if index < len(array)-1:
                if ber[1] > array[index+1][1]:
                    isRedbar += 1
                    # print(array[index+1])
                    pygame.draw.line(display, RED, (array[index+1][0],array[index+1][1]), (array[index+1][0],displayY), berWidth)
                    pygame.draw.rect(display, RED, ((array[index+1][0]-4,array[index+1][1]), (berWidth,displayY)), 1)
                    tampNext = array[index][1]
                    array[index][1] = array[index+1][1]
                    array[index+1][1] = tampNext
                    # break 
        except Exception as e:
            print(e)
            pass
    
    if isRedbar < 1 :
        start = False
        plushTime = 0
        isDone = True
    isRedbar = 0




font = pygame.font.SysFont(None,40)
def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    display.blit(screen_text, [x,y])

#############################################
berlist = genBars(berAmmout)
# tempBerlist = berlist

drawBars(berlist)
while running:


    # sort2 (berlist)
    display.fill((0,0,0))
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
                start = False
                time = 0
                plushTime = 1
                itration = 0
            if event.key == pygame.K_RETURN:
                if start == False:
                    if isDone:
                        start = True
                        itration = 0
                        isDone =False
                    
                    else:
                        start = True
                else:
                    start = False
            if event.key == pygame.K_SPACE:
                if isRevers == False:
                    isRevers = True
                    itration = 0
                else:
                    isRevers = False

    drawBars(berlist)
    if start:
        time += plushTime
        if not isRevers:
            sortArray(berlist)

        else:
            sortArrayRevers(berlist)

    text_screen(f"Itration:{itration}",WHITE,5,5)
    text_screen(f"Time:{time}ms",WHITE,5,45)
    text_screen(f"Bars:{int(berAmmout)}",WHITE,5,85)
    text_screen(f"FPS:{int(FPS)}",WHITE,5,130)
    # text_screen(f"CPU usage:{int(cpuUseage)}",WHITE,5,85+45+45)
    
    
    clock.tick(FPS)
    pygame.display.update()
    
        




