#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pygame
import random

import math
from pygame import mixer

# Initialize the pygame
pygame.init()

#create the screen
screen = pygame.display.set_mode((800, 600))

#Background:
background = pygame.image.load(r"C:\Users\infor\Downloads\space_galaxy_shine_137572_800x600 (1).jpg")

#background sound:
pygame.mixer.music.load(r"C:\Users\infor\Downloads\background.wav")
pygame.mixer.music.play(-1)

# Title and icon
pygame.display.set_caption('Space Invaders')
icon=pygame.image.load(r"C:\Users\infor\Downloads\spaceship.png")
pygame.display.set_icon(icon)

# Player
playerimg = pygame.image.load(r"C:\Users\infor\Downloads\spaceship (1).png")
playerX=370
playerY=480
playerX_change=0
playerY_change=0

# Enemy
enemyimg = []
enemyX=[]
enemyY=[]
enemyX_change=[]
enemyY_change=[]
num_of_enemies=10

for i in range(num_of_enemies):
    enemyimg.append(pygame.image.load(r"C:\Users\infor\Downloads\bug.png"))
    enemyX.append(random.randint(0, 800))
    enemyY.append(random.randint(50, 150))
    enemyX_change.append(0.3)
    enemyY_change.append(10)

# Bullet
# ready -  you can't se the bullet on the screen
# fire - The bullet is currently moving

bulletimg = pygame.image.load(r"C:\Users\infor\Downloads\bullet.png")
bulletX=0
bulletY=480
bulletX_change=0.1
bulletY_change=0.6
bullet_state='ready'

#font

score_value=0
font=pygame.font.Font(r"C:\Users\infor\Downloads\pineapple_days\Pineapple Days.ttf", 32)

textX=10
textY=10

# game over:
over_font=pygame.font.Font(r"C:\Users\infor\Downloads\pineapple_days\Pineapple Days.ttf", 64)

def show_score(x,y):
    score=font.render(str(score_value), True, (255,255,255))
    screen.blit(score, (x, y))

    
def game_over_text():
    over_text=over_font.render(f'GAME OVER', True, (255, 255, 255))
    screen.blit(over_text, (200, 250))
    
def player(x, y):
    screen.blit(playerimg, (x, y))

    
    
def enemy(x, y, i):
    screen.blit(enemyimg[i], (x, y))

    
def fire_bullet(x,y):
    global bullet_state
    bullet_state = 'fire'
    screen.blit(bulletimg, (x+16,y+10))

def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance=math.sqrt((math.pow(enemyX-bulletX, 2)) + (math.pow(enemyY-bulletY, 2)))
    if distance<27:
        return True
    else:
        return False
    
def isCollision2(enemyX, enemyY, playerX, playerY):
    distance=math.sqrt((math.pow(enemyX-playerX, 2)) + (math.pow(enemyY-playerY, 2)))
    if distance<35:
        return True
    else:
        return False
    
# Game loop
running = True
while running:
    
    screen.fill((255,255,0)) # change color of screen, (R,G,B)
    # background image:
    screen.blit(background, (0,0))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running= False
    
        # if the keystroke is pressed check whether its right or left
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                playerX_change= -0.4
            if event.key==pygame.K_RIGHT:
                playerX_change = 0.4
            if event.key==pygame.K_UP:
                playerY_change = -0.4
            if event.key==pygame.K_DOWN:
                playerY_change = 0.4
            if event.key==pygame.K_SPACE:
                if bullet_state == 'ready':
                    bullet_sound=pygame.mixer.Sound(r"C:\Users\infor\Downloads\laser.wav")
                    bullet_sound.play()
                    bulletX=playerX
                    fire_bullet(bulletX, bulletY)
        if event.type==pygame.KEYUP:
            if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT or event.key==pygame.K_UP or event.key==pygame.K_DOWN:
                playerX_change = 0
                playerY_change = 0
                
    # checking for bounderies of spaceship       
    playerX += playerX_change
    playerY += playerY_change
    
    if playerX <= 0:
        playerX = 0
    if playerX >= 736:
        playerX=736
    if playerY <= 0:
        playerY = 0
    if playerY >= 480:
        playerY=480
     
    # checking for bounderies of enemy
    for i in range(num_of_enemies):
        
        #game over
        if enemyY[i]>610:
            for j in range(num_of_enemies):
                enemyY[j]=2000
            game_over_text()
            break
        
        enemyX[i]+= enemyX_change[i]
        if enemyX[i] <= 0:
            enemyX_change[i]=0.5
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 736:
            enemyX_change[i]=-0.5
            enemyY[i] += enemyY_change[i]
      
    
        #Collision Enemy vs bullet
        collision= isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            explore_sound=pygame.mixer.Sound(r"C:\Users\infor\Downloads\explosion.wav")
            explore_sound.play()
            bulletY=playerY
            bullet_state='ready'
            score_value+=1
            enemyX[i]=random.randint(0, 735)
            enemyY[i]=random.randint(50, 150)
            print(score_value)
            
    
        #collision Enemy vs player
        collision2= isCollision2(enemyX[i], enemyY[i], playerX, playerY)
        if collision2:
            explore_sound=pygame.mixer.Sound(r"C:\Users\infor\Downloads\explosion.wav")
            explore_sound.play()
            playerY=480
            score_value-=1
            print(score_value)
        
        enemy(enemyX[i], enemyY[i], i)
        
        
    # Bullet moving:
    if bulletY<=0:
        bulletY=playerY
        bullet_state='ready' 
        
    if bullet_state =='fire':
        fire_bullet(bulletX, bulletY)
        bulletY-=bulletY_change
    
    
        
    player(playerX, playerY)
    
    show_score(textX, textY)
    
           
    pygame.display.update() # update to take effection


# In[ ]:





# In[ ]:




