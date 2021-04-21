import pygame
import random
import math

pygame.init()

# TITLE AND ICON
pygame.display.set_caption("SpaceGame")
icon = pygame.image.load('launch.png')
pygame.display.set_icon(icon)

# BACKGROUND IMG

# PLAYER
plimg = pygame.image.load('battleship.png')
plX = 360
plY = 480
plXchange = 0

# ENEMY
enimg = pygame.image.load('ufo.png')
enX = random.randint(0, 736)
enY = random.randint(25, 150)
enXchange = 0.3
enYchange = 10

# MISSILE
msimg = pygame.image.load('missile.png')
msX = 0
msY = 480
msXchange = 0
msYchange = 0.5
msstate = "ready"

score=0

def player(x, y):
    screen.blit(plimg, (x, y))


def enemy(x, y):
    screen.blit(enimg, (x, y))


def fire_missile(x, y):
    global msstate
    msstate = "fire"
    screen.blit(msimg, (x + 16, y + 16))


def iscollision(enX, enY, msX, msY):
    dist = math.sqrt(math.pow((enX - msX), 2) + math.pow((enY - msY), 2))
    if dist < 27 :
        return True
    else:
        return False

# SCREEN
screen = pygame.display.set_mode((800, 600))

run = True
while run:
    # RGB - (0-255,0-255,0-255)
    screen.fill((10, 0, 70))  # This is for background colour

    # This is for background image

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        # Using the keyboard for movement
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                plXchange = -0.4

            if event.key == pygame.K_RIGHT:
                plXchange = 0.4

            if event.key == pygame.K_SPACE:
                if msstate is "ready":
                    msX = plX
                    fire_missile(msX, msY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                plXchange = 0

    plX += plXchange
    enX += enXchange

    if plX <= 0:
        plX = 0
    elif plX >= 736:
        plX = 736

    if enX <= 0:
        enXchange = 0.25
        enY += enYchange
    elif enX >= 736:
        enXchange = -0.25
        enY += enYchange

    if msY <= 0:
        msY = 480
        msstate = "ready"

    if msstate is "fire":
        fire_missile(msX, msY)
        msY -= msYchange

    collision=iscollision(enX,enY,msX,msY)
    if collision:
        msY= 480
        msstate="ready"
        score +=1
        print(score)
        enX = random.randint(0, 736)
        enY = random.randint(25, 150)

    player(plX, plY)
    enemy(enX, enY)
    pygame.display.update()
