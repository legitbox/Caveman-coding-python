import pygame
pygame.init()

win = pygame.display.set_mode((500, 500))

pygame.display.set_caption("pygame ooga booga")

walk_Right = [pygame.image.load('sprites/R1.png'), pygame.image.load('sprites/R2.png'), pygame.image.load('sprites/R3.png'), pygame.image.load('sprites/R4.png'), pygame.image.load('sprites/R5.png'), pygame.image.load('sprites/R6.png'), pygame.image.load('sprites/R7.png'), pygame.image.load('sprites/R8.png'), pygame.image.load('sprites/R9.png')]
walk_Left = [pygame.image.load('sprites/L1.png'), pygame.image.load('sprites/L2.png'), pygame.image.load('sprites/L3.png'), pygame.image.load('sprites/L4.png'), pygame.image.load('sprites/L5.png'), pygame.image.load('sprites/L6.png'), pygame.image.load('sprites/L7.png'), pygame.image.load('sprites/L8.png'), pygame.image.load('sprites/L9.png')]
bg = pygame.image.load('sprites/bg.jpg')
char = pygame.image.load('sprites/standing.png')

clock = pygame.time.Clock()

x = 50
y = 400
width = 64
height = 64
vel = 5
left = False
right = False
walkcount = 0

isJump = False
jumpCount = 10

def redrawGameWindow():
    global walkcount

    win.blit(bg, (0, 0))
    if walkcount + 1 >= 27:
        walkcount = 0
    
    if left:
        win.blit(walk_Left[walkcount//3], (x,y))
        walkcount += 1
    elif right:
        win.blit(walk_Right[walkcount//3], (x,y))
        walkcount += 1
    else:
        win.blit(char, (x,y))

    pygame.display.update()
    

run = True
while run:
    clock.tick(27)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    keys = pygame.key.get_pressed()

    if keys[pygame.K_a] and x > vel:
        x -= vel
        left = True
        right = False

    elif keys[pygame.K_d] and x < 500 - width - vel:
        x += vel
        right = True
        left = False
    else:
        left = False
        right = False
        walkcount = 0
    
    if not(isJump):
        if keys[pygame.K_SPACE]:
            isJump = True
            left = False
            right = False
            walkcount = 0
    else:
        if jumpCount >= -10:
            neg = 1
            if jumpCount < 0:
                neg = -1
            y -= (jumpCount ** 2) * 0.5 * neg
            jumpCount -= 1

        else:
            isJump = False
            jumpCount = 10

    redrawGameWindow()
    



pygame.quit()