import pygame, sys, random
from pygame.locals import *

# determine if the two rectangles overlap - this method is taken from Invent Your Own Computer Games
def doRectsOverlap(rect1, rect2):
    for a, b, in [(rect1, rect2), (rect2, rect1)]:
        # Check is a's corners are inside b
        if ((isPointInsideRect(a.left, a.top, b)) or (isPointInsideRect(a.left, a.bottom, b)) or (isPointInsideRect(a.right, a.top, b)) or (isPointInsideRect(a.right, a.bottom, b))):
            return True
    return False

# determine if the two rectangles overlap - this method is taken from Invent Your Own Computer Games
def isPointInsideRect(x, y, rect):
    if (x > rect.left) and (x < rect.right) and (y > rect.top) and (y < rect.bottom):
        return True
    else:
        return False

pygame.init() #initialize modules
mainClock = pygame.time.Clock()
random.seed() # instantiate random generator

# ssset up colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# set up keyboard variables
moveUpLeft = False
moveDownLeft = False
moveUpRight = False
moveDownRight = False
MOVESPEED = 3
DOWNLEFT = 1
DOWN = 2
DOWNRIGHT = 3
RIGHT = 6
UPRIGHT = 9
UP = 8
UPLEFT = 7
LEFT = 4
WINDOWHEIGHT = 400
WINDOWWIDTH = 600
leftPoints = 0
rightPoints = 0

# set up window
windowSurface = pygame.display.set_mode((600, 400), 0, 32)
pygame.display.set_caption("Bacon Pong!")

# set up the basic pictures
mouth = pygame.image.load('sample_mouth.jpg')
mouthImage = pygame.transform.scale(mouth, (100, 400))
bacon = pygame.image.load('bacon.jpg')
baconImage = pygame.transform.scale(bacon, (50, 50))

# set up music
pygame.mixer.pre_init(44100, 16, 2, 4096)
pygame.mixer.music.load('death.mid')
pygame.mixer.music.play(-1, 0.0)

# set up the baconMove object
baconMove = {'rect':pygame.Rect(windowSurface.get_rect().centerx - 25,windowSurface.get_rect().centery - 25, 50, 50), 'dir':DOWNRIGHT}

# set up the left paddle and right paddle
leftPaddle = pygame.Rect(100, 150, 25, 100)
rightPaddle = pygame.Rect(475, 150, 25, 100)

while True:
    # check for the QUIT event
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            # change the keyboard variables
            if event.key == ord('w'):
                moveUpLeft = True
                moveDownLeft = False
            if event.key == K_UP:
                moveUpRight = True
                moveDownRight = False
            if event.key == ord('s'):
                moveUpLeft = False
                moveDownLeft = True
            if event.key == K_DOWN:
                moveUpRight = False
                moveDownRight = True
        if event.type == KEYUP:
            if event.key == K_UP:
                moveUpRight = False
            if event.key == ord('w'):
                moveUpLeft = False
            if event.key == K_DOWN:
                moveDownRight = False
            if event.key == ord('s'):
                moveDownLeft = False

        if moveUpLeft and leftPaddle.top > 0:
            leftPaddle.top -= 12
        if moveDownLeft and leftPaddle.bottom < 600:
            leftPaddle.top += 12
        if moveUpRight and rightPaddle.top > 0:
            rightPaddle.top -= 12
        if moveDownRight and rightPaddle.bottom < 600:
            rightPaddle.top += 12

    # check if the baconMove has moved out of the window or hit a paddle
    if doRectsOverlap(baconMove['rect'], leftPaddle):
        if baconMove['dir'] == UPLEFT:
            num = random.randint(1, 3)
            if num == 1:
                baconMove['dir'] = DOWNRIGHT
            elif num == 2:
                baconMove['dir'] = RIGHT
            elif num == 3:
                baconMove['dir'] = DOWN
        elif baconMove['dir'] == UP:
            num = random.randint(1, 3)
            if num == 1:
                baconMove['dir'] = DOWN
            elif num == 2:
                baconMove['dir'] = DOWNRIGHT
            elif num == 3:
                baconMove['dir'] = DOWNLEFT
        elif baconMove['dir'] == UPRIGHT:
            if num == 1:
                baconMove['dir'] = DOWNLEFT
            elif num == 2:
                baconMove['dir'] = LEFT
            elif num == 3:
                baconMove['dir'] = DOWN
        elif baconMove['dir'] == RIGHT:
            if num == 1:
                baconMove['dir'] = DOWNLEFT
            elif num == 2:
                baconMove['dir'] = LEFT
            elif num == 3:
                baconMove['dir'] = UPLEFT       
        elif baconMove['dir'] == DOWNRIGHT:
            num = random.randint(1, 3)
            if num == 1:
                baconMove['dir'] = UPLEFT
            elif num == 2:
                baconMove['dir'] = LEFT
            elif num == 3:
                baconMove['dir'] = UP
        elif baconMove['dir'] == DOWN:
            num = random.randint(1, 3)
            if num == 1:
                baconMove['dir'] = UPLEFT
            elif num == 2:
                baconMove['dir'] = UP
            elif num == 3:
                baconMove['dir'] = UPRIGHT
        elif baconMove['dir'] == DOWNLEFT:
            num = random.randint(1, 3)
            if num == 1:
                baconMove['dir'] = UPRIGHT
            elif num == 2:
                baconMove['dir'] = RIGHT
            elif num == 3:
                baconMove['dir'] = UP
        elif baconMove['dir'] == LEFT:
            num = random.randint(1, 3)
            if num == 1:
                baconMove['dir'] = UPRIGHT
            elif num == 2:
                baconMove['dir'] = RIGHT
            elif num == 3:
                baconMove['dir'] = DOWNRIGHT
    # check if the baconMove has moved out of the window or hit a paddle
    if doRectsOverlap(baconMove['rect'], rightPaddle):
        if baconMove['dir'] == UPLEFT:
            num = random.randint(1, 3)
            if num == 1:
                baconMove['dir'] = DOWNRIGHT
            elif num == 2:
                baconMove['dir'] = RIGHT
            elif num == 3:
                baconMove['dir'] = DOWN
        elif baconMove['dir'] == UP:
            num = random.randint(1, 3)
            if num == 1:
                baconMove['dir'] = DOWN
            elif num == 2:
                baconMove['dir'] = DOWNRIGHT
            elif num == 3:
                baconMove['dir'] = DOWNLEFT
        elif baconMove['dir'] == UPRIGHT:
            num = random.randint(1, 3)
            if num == 1:
                baconMove['dir'] = DOWNLEFT
            elif num == 2:
                baconMove['dir'] = LEFT
            elif num == 3:
                baconMove['dir'] = DOWN
        elif baconMove['dir'] == RIGHT:
            num = random.randint(1, 3)
            if num == 1:
                baconMove['dir'] = DOWNLEFT
            elif num == 2:
                baconMove['dir'] = LEFT
            elif num == 3:
                baconMove['dir'] = UPLEFT       
        elif baconMove['dir'] == DOWNRIGHT:
            num = random.randint(1, 3)
            if num == 1:
                baconMove['dir'] = UPLEFT
            elif num == 2:
                baconMove['dir'] = LEFT
            elif num == 3:
                baconMove['dir'] = UP
        elif baconMove['dir'] == DOWN:
            num = random.randint(1, 3)
            if num == 1:
                baconMove['dir'] = UPLEFT
            elif num == 2:
                baconMove['dir'] = UP
            elif num == 3:
                baconMove['dir'] = UPRIGHT
        elif baconMove['dir'] == DOWNLEFT:
            num = random.randint(1, 3)
            if num == 1:
                baconMove['dir'] = UPRIGHT
            elif num == 2:
                baconMove['dir'] = RIGHT
            elif num == 3:
                baconMove['dir'] = UP
        elif baconMove['dir'] == LEFT:
            num = random.randint(1, 3)
            if num == 1:
                baconMove['dir'] = UPRIGHT
            elif num == 2:
                baconMove['dir'] = RIGHT
            elif num == 3:
                baconMove['dir'] = DOWNRIGHT
    elif baconMove['rect'].top < 0: 
        # bouncer has moved past the top
        if baconMove['dir'] == UPLEFT:
            baconMove['dir'] = DOWNLEFT
        if baconMove['dir'] == UPRIGHT:
            baconMove['dir'] = DOWNRIGHT
        if baconMove['dir'] == UP:
            num = random.randint(1, 3)
            if num == 1:
                baconMove['dir'] = DOWN
            elif num == 2:
                baconMove['dir'] = DOWNRIGHT
            elif num == 3:
                baconMove['dir'] = DOWNLEFT
    elif baconMove['rect'].bottom > WINDOWHEIGHT:
        # bouncer has moved past the bottom
        if baconMove['dir'] == DOWNLEFT:
            baconMove['dir'] = UPLEFT
        if baconMove['dir'] == DOWNRIGHT:
            baconMove['dir'] = UPRIGHT
        elif baconMove['dir'] == DOWN:
            num = random.randint(1, 3)
            if num == 1:
                baconMove['dir'] = UPLEFT
            elif num == 2:
                baconMove['dir'] = UP
            elif num == 3:
                baconMove['dir'] = UPRIGHT
    elif baconMove['rect'].left < 0:
        baconMove['rect'] = pygame.Rect(windowSurface.get_rect().centerx - 25,windowSurface.get_rect().centery - 25, 50, 50)
        baconMove['dir'] = DOWNRIGHT
        rightPoints += 1
    elif baconMove['rect'].right > WINDOWWIDTH:
        baconMove['rect'] = pygame.Rect(windowSurface.get_rect().centerx - 25,windowSurface.get_rect().centery - 25, 50, 50)
        baconMove['dir'] = DOWNLEFT
        leftPoints += 1
        
    # move the bacon data structure
    if baconMove['dir'] == DOWN:
        baconMove['rect'].top += MOVESPEED
    if baconMove['dir'] == DOWNLEFT:
        baconMove['rect'].left -= MOVESPEED
        baconMove['rect'].top += MOVESPEED
    if baconMove['dir'] == LEFT:
        baconMove['rect'].left -= MOVESPEED
    if baconMove['dir'] == UPLEFT:
        baconMove['rect'].left -= MOVESPEED
        baconMove['rect'].top -= MOVESPEED
    if baconMove['dir'] == UP:
        baconMove['rect'].top -= MOVESPEED
    if baconMove['dir'] == UPRIGHT:
        baconMove['rect'].left += MOVESPEED
        baconMove['rect'].top -= MOVESPEED
    if baconMove['dir'] == RIGHT:
        baconMove['rect'].left += MOVESPEED
    if baconMove['dir'] == DOWNRIGHT:
        baconMove['rect'].left += MOVESPEED
        baconMove['rect'].top += MOVESPEED
    if baconMove['dir'] == DOWN:
        baconMove['rect'].top += MOVESPEED

    windowSurface.fill(WHITE)
    
    font = pygame.font.Font(None, 36)
    text = font.render("Bacon Pong!", 1, (10, 10, 10))
    textpos = text.get_rect()
    textpos.centerx = windowSurface.get_rect().centerx

    if leftPoints != 10 and rightPoints != 10:
        # display left paddle points
        left = pygame.font.Font(None, 36)
        leftPaddlePts = left.render(str(rightPoints), 1, (0, 0, 0))
        leftPaddlePtsPos = leftPaddlePts.get_rect()
        leftPaddlePtsPos.center = (450, 15)
        windowSurface.blit(leftPaddlePts, leftPaddlePtsPos)

        # display right paddle points
        right = pygame.font.Font(None, 36)
        rightPaddlePts = right.render(str(leftPoints), True, BLACK, WHITE)
        rightPaddlePtsPos = rightPaddlePts.get_rect()
        rightPaddlePtsPos.center = (150, 15)
        windowSurface.blit(rightPaddlePts, rightPaddlePtsPos) 

        # display bacon and left and right paddles
        windowSurface.blit(baconImage, baconMove['rect'])
        pygame.draw.rect(windowSurface, BLACK, leftPaddle)
        pygame.draw.rect(windowSurface, BLACK, rightPaddle)

        windowSurface.blit(text, textpos)
        windowSurface.blit(mouthImage, (500, 0))
        windowSurface.blit(pygame.transform.flip(mouthImage, True, True), (0, 0))
    else:
        windowSurface.blit(text, textpos)
        windowSurface.blit(mouthImage, (500, 0))
        windowSurface.blit(pygame.transform.flip(mouthImage, True, True), (0, 0))
        winnerScreen = pygame.font.Font(None, 50)
        if leftPoints >= 10:
            winner = "The player on the left wins!"
        else:
            winner = "The player on the right wins!"
        winnerScreenRend = winnerScreen.render(winner, True, BLACK, WHITE)
        winnerScreenRendPos = winnerScreenRend.get_rect()
        winnerScreenRendPos.centerx = windowSurface.get_rect().centerx
        winnerScreenRendPos.centery = windowSurface.get_rect().centery
        windowSurface.blit(winnerScreenRend, winnerScreenRendPos)
        leftPoints = 0
        rightPoints = 0
        pygame.display.update()
        pygame.time.wait(5000)

    pygame.display.update()
    mainClock.tick(45)
