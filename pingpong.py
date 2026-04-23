import pygame
import random

def randForce():
    rand = 0
    while rand == 0:
        rand = random.randint(-3,3)
    return rand
pygame.init()
screen = pygame.display.set_mode((800,500))
bounds = pygame.Rect((20,20,760,460))
leftPane = pygame.Rect((bounds.left,200,5,100))
rightPane = pygame.Rect((bounds.right,200,5,100))
clock = pygame.time.Clock()
ballPos = pygame.Vector2((400,250))
force = pygame.Vector2((randForce(),0))
pygame.display.flip()
running = True
pointsLeft = 0
font = pygame.font.Font(None, 36) 
font2 = pygame.font.Font(None, 20) 
pointsRight = 0
def chooseMode():
    text_surface = font.render("Choose your mode", True, (255,255,255))
    textWidth, textHeight = font.size("Choose your mode")
    screen.blit(text_surface, (400-textWidth/2,200-textHeight/2))
    SingleSurface = font2.render("Single Player", True, (255,255,255))
    textWidth, textHeight = font2.size("Single Player")
    SingleBounds = SingleSurface.get_rect()
    SingleBounds.left = 340-textWidth/2
    SingleBounds.top = 260-textHeight/2
    screen.blit(SingleSurface, (340-textWidth/2,260-textHeight/2))
    TwoSurface = font2.render("Two Player", True, (255,255,255))
    textWidth, textHeight = font2.size("Two Player")
    screen.blit(TwoSurface, (460-textWidth/2,260-textHeight/2))
    waiting=True
    TwoBounds = TwoSurface.get_rect()
    TwoBounds.left = 460-textWidth/2
    TwoBounds.top = 260-textHeight/2
    while waiting:
        for e in pygame.event.get():
            if int(e.type) == 1025:
                pos = pygame.mouse.get_pos()
                pos = pygame.Vector2(pos)
                print(pos)
                if pos.x > SingleBounds.left and pos.x < SingleBounds.right and pos.y > SingleBounds.top and pos.y < SingleBounds.bottom:
                    mode = "single"
                elif pos.x > TwoBounds.left and pos.x < TwoBounds.right and pos.y > TwoBounds.top and pos.y < TwoBounds.bottom:
                    mode = "2player"
                else:
                    continue
                return mode
        pygame.display.flip()
mode = None
isStart=True
while running:
    if not mode:
        mode = chooseMode()
    if mode == "single":
        if isStart:
            force.x = random.randint(1,3)
            isStart = False
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                running = False
        keys = pygame.key.get_pressed()
        if keys[pygame.K_DOWN] and rightPane.bottom < bounds.bottom:
            rightPane.y += 1
        if keys[pygame.K_UP] and rightPane.top > bounds.top:
            rightPane.y -= 1
        pygame.draw.rect(screen, (255, 255, 255), (0,0,800,500) , border_radius=5)
        pygame.draw.rect(screen, (0,0,0), rightPane, border_radius=5)
        ballPos.x += force.x/3
        ballPos.y += force.y/3
        touches = False
        if ballPos.x+5 > rightPane.right and ballPos.x-5 < rightPane.left:
            if ballPos.y+5 > rightPane.top and ballPos.y-5 < rightPane.bottom:
                touches = "right"
        if touches:
            force.x = -force.x
            if force.x < 0:
                force.x -= 1
            else:
                force.x += 1
            if touches == "right" and ballPos.y < rightPane.bottom-50:
                force.y += random.randint(-3,-1)
                pointsRight += 1
        if ballPos.y < bounds.top or ballPos.y > bounds.bottom:
            force.y = -force.y
        if ballPos.x < 20:
            force.x = -force.x
        if ballPos.x > 800:
            pointsLeft += 1
            ballPos.x = 400
            ballPos.y = 250
            force.x = random.randint(1,3)
            force.y = 0
        text_surface = font.render("Points: "+str(pointsLeft), True, (255,0,0))
        screen.blit(text_surface, (20,20))
        text_surface = font.render("Points: "+str(pointsRight), True, (0,0,255))
        rightTextWidth, n = font.size("Points"+str(pointsRight))
        screen.blit(text_surface, (780-rightTextWidth,20))
            
        pygame.draw.circle(screen, (0,0,0), ballPos, 5)
        pygame.display.flip()
        clock.tick(180)
    elif mode == "2player":
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                running = False
        keys = pygame.key.get_pressed()
        if keys[pygame.K_s] and leftPane.bottom < bounds.bottom:
            leftPane.y += 1
        if keys[pygame.K_w] and leftPane.top > bounds.top:
            leftPane.y -= 1
        if keys[pygame.K_DOWN] and rightPane.bottom < bounds.bottom:
            rightPane.y += 1
        if keys[pygame.K_UP] and rightPane.top > bounds.top:
            rightPane.y -= 1
        pygame.draw.rect(screen, (255, 255, 255), (0,0,800,500) , border_radius=5)
        pygame.draw.rect(screen, (0,0,0), leftPane, border_radius=5)
        pygame.draw.rect(screen, (0,0,0), rightPane, border_radius=5)
        ballPos.x += force.x/3
        ballPos.y += force.y/3
        touches = False
        if ballPos.x-5 < leftPane.right and ballPos.x+5 > leftPane.left:
            if ballPos.y+5 > leftPane.top and ballPos.y-5 < leftPane.bottom:
                touches = "left"
        if ballPos.x+5 > rightPane.right and ballPos.x-5 < rightPane.left:
            if ballPos.y+5 > rightPane.top and ballPos.y-5 < rightPane.bottom:
                touches = "right"
        if touches:
            force.x = -force.x
            if force.x < 0:
                force.x -= 1
            else:
                force.x += 1
            if touches == "right" and ballPos.y > rightPane.bottom-50 or touches == "left" and ballPos.y > leftPane.bottom-50:
                force.y += random.randint(1,3)
            if touches == "right" and ballPos.y < rightPane.bottom-50 or touches == "left" and ballPos.y < leftPane.bottom-50:
                force.y += random.randint(-3,-1)
        if ballPos.y < bounds.top or ballPos.y > bounds.bottom:
            force.y = -force.y
        if ballPos.x < 0:
            pointsRight += 1
            ballPos.x = 400
            ballPos.y = 250
            force.x = randForce()
            force.y = 0
        if ballPos.x > 800:
            pointsLeft += 1
            ballPos.x = 400
            ballPos.y = 250
            force.x = randForce()
            force.y = 0
        text_surface = font.render("Points: "+str(pointsLeft), True, (255,0,0))
        screen.blit(text_surface, (20,20))
        text_surface = font.render("Points: "+str(pointsRight), True, (0,0,255))
        rightTextWidth, n = font.size("Points"+str(pointsRight))
        screen.blit(text_surface, (780-rightTextWidth,20))
            
        pygame.draw.circle(screen, (0,0,0), ballPos, 5)
        pygame.display.flip()
        clock.tick(180)

pygame.quit()
