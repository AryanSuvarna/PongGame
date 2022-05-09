# import secrets
import pygame

# Constants and variables
WHITE = (255,255,255)
BLACK = (0,0,0)

WIDTH = 600
LENGTH = 600

pygame.init()
gameFont = pygame.font.SysFont("Ubuntu",40)

delay = 25

paddleSpeed = 20
paddleWidth = 10
paddleHeight = 100

p1Xpos = 10
p1Ypos = LENGTH / 2 - paddleHeight / 2

p2Xpos = WIDTH - paddleWidth - 10
p2Ypos = LENGTH / 2 - paddleHeight / 2

p1Score = 0
p2Score = 0

# Movements
p1Up = False
p1Down = False
p2Up = False
p2Down = False

ballXPos = WIDTH / 2
ballYPos = LENGTH / 2
ballWidth = 8
ballXVel = -10
ballYVel = 0

screen = pygame.display.set_mode((WIDTH,LENGTH))

# Drawing objects
def draw_objects():
    pygame.draw.rect(screen,WHITE,(int(p1Xpos),int(p1Ypos), paddleWidth, paddleHeight))
    pygame.draw.rect(screen,WHITE,(int(p2Xpos),int(p2Ypos), paddleWidth, paddleHeight))
    pygame.draw.circle(screen, WHITE, (ballXPos, ballYPos), ballWidth)

    score = gameFont.render(f"Player 1: {str(p1Score)}                      Player 2: {str(p2Score)}", False, WHITE)
    screen.blit(score, (30, 30))

def applyPlayerMovement():
    global p1Ypos
    global p2Ypos

    if p1Up:
        p1Ypos = max(p1Ypos - paddleSpeed , 0)
    elif p1Down:
        p1Ypos = min(p1Ypos + paddleSpeed, LENGTH-90)

    if p2Up:
        p2Ypos = max(p2Ypos - paddleSpeed , 0)
    elif p2Down:
        p2Ypos = min(p2Ypos + paddleSpeed, LENGTH-90)


def applyBallMovement():
    global ballXPos, ballXVel, ballYPos, ballYVel, p1Score, p2Score

    if (ballXPos + ballXVel < p1Xpos + paddleWidth) and (p1Ypos < ballYPos + ballYVel + ballWidth <= p1Ypos + paddleHeight):
        ballXVel *= -1
        ballYVel = (p1Ypos + paddleHeight / 2 - ballYPos) / 15
        ballYVel *= 1
    
    elif ballXPos + ballXVel < 0:
        p2Score += 1
        ballXPos = WIDTH / 2
        ballXPos = LENGTH / 2
        ballXVel = 10
        ballYVel = 0 

    if (ballXPos + ballXVel > p2Xpos - paddleWidth) and (p2Ypos < ballYPos + ballYVel + ballWidth <= p2Ypos + paddleHeight ):
        ballXVel *= -1
        ballYVel = (p2Ypos + paddleHeight / 2 - ballYPos) / 15
        ballYVel *= 1
    
    elif ballXPos + ballXVel > LENGTH:
        p1Score += 1
        ballXPos = WIDTH / 2
        ballXPos = LENGTH / 2
        ballXVel = -10
        ballYVel = 0 

    if ballYPos + ballYVel > LENGTH or ballYPos + ballYVel < 0:
        ballYVel *= -1

    ballXPos += ballXVel
    ballYPos += ballYVel

pygame.display.set_caption("PongV2")
screen.fill(BLACK)
pygame.display.flip()

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            if event.key == pygame.K_w:
                p1Up = True
            if event.key == pygame.K_s:
                p1Down = True
            if event.key == pygame.K_UP:
                p2Up = True
            if event.key == pygame.K_DOWN:
                p2Down = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                p1Up = False
            if event.key == pygame.K_s:
                p1Down = False
            if event.key == pygame.K_UP:
                p2Up = False
            if event.key == pygame.K_DOWN:
                p2Down = False
    
    screen.fill(BLACK)
    applyPlayerMovement()
    applyBallMovement()
    draw_objects()
    pygame.display.flip()
    pygame.time.wait(delay)