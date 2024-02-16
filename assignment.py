#-----------------------------------------------------------------------------
# Name: Tiny Box Tim and the Leap of Faith
# Purpose:
# This will be a platforming game where the player must continue to rise higher up employing various mechanics available to their disposal.
# Such mechanics will include hanging from hangable ceilings, bouncing off bouncy obstacles, and climbing up scalable walls.
# The player will progress through a various levels to eventually reach the end of the game.
#
# Author:      Amir Nasirov
# Created:     6-April-2023
# Updated:     23-April-2023

# ASSET SOURCES:
# https://www.kenney.nl/assets/pixel-platformer
# https://www.kenney.nl/assets/pixel-platformer-industrial-expansion

#-----------------------------------------------------------------------------
#I think this project deserves a level 4+ because ...
#
#Features Added:
#   PLAYABLE TUTORIAL
#   Many fun and clever levels that are mechanically and logically fun!
#   Bug-free (i think, i didnt find any)
#   Comfortable Controls
#   Distinct Theme
#   Downloaded Sprite Assets
#   Downloaded Text Font
#   Runs smoothly
#   Moving Background
#-----------------------------------------------------------------------------

import pygame
import math
from Levels import screens
from Levels import tutorials
from Obstacle import Obstacle

class StartScreen:
    
    def __init__(self):
        self.startButton = pygame.Rect(50, 200, 200, 50)
        self.tutorialButton = pygame.Rect(50, 300, 200, 50)
        self.quitButton = pygame.Rect(50, 400, 200, 50)
        
        self.startButton.centerx = 750
        self.tutorialButton.centerx = 750
        self.quitButton.centerx = 750

    def buttonClick(self):
        
        mouse = pygame.Rect(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1], 1, 1)
        
        if mouse.colliderect(self.startButton):
            return 'next'       
        elif mouse.colliderect(self.tutorialButton):
            return 'tutorial'
        elif mouse.colliderect(self.quitButton):
            return 'quit'
        else:
            return 'start'
        
    

class Player:
    
    def __init__(self):
        self.color = (0, 0, 0)
        self.speedX = 0.0
        self.speedY = 0.0
        self.maxBounce = 0
        self.jumping = False
        self.hanging = False
        self.block = pygame.Rect(0, 675, 25, 25)
        self.clone = pygame.Rect(0, 0, 25, 25)

    def drawPlayer(self, surface, charImgs):
        if self.hanging:
            surface.blit(charImgs[2], (self.block.left, self.block.top))
        elif self.jumping:
            surface.blit(charImgs[1], (self.block.left, self.block.top))
        else:
            surface.blit(charImgs[0], (self.block.left, self.block.top))


# main program function
def main():
    #-----------------------------Setup------------------------------------------------------#
    """ Set up the game and run the main game loop """
    pygame.init()
    surfaceSizeX = 1500
    surfaceSizeY = 700
    tutorial = False
    state = 'start'
    attempts = 1
    fullDrawing = pygame.Surface((1500, 700))
    
    # ----------- FONTS -----------
    pixelFontSmall = pygame.font.Font('Fonts/pixel.ttf', 12)
    pixelFont = pygame.font.Font('Fonts/pixel.ttf', 18)
    pixelFontBig = pygame.font.Font('Fonts/pixel.ttf', 24)
    pixelFontHuge = pygame.font.Font('Fonts/pixel.ttf', 30)
    pixelFontBiggest = pygame.font.Font('Fonts/pixel.ttf', 60)
    
    # ----------- TITLE -----------
    titleTxt = pixelFontHuge.render('TINY BOX TIM', False, (0, 0, 1))
    andTheTxt = pixelFontSmall.render('and the', False, (0, 0, 1))
    leapTxt = pixelFontHuge.render('LEAP', False, (0, 0, 1))
    ofTxt = pixelFontSmall.render('of', False, (0, 0, 1))
    faithTxt = pixelFontHuge.render('FAITH', False, (0, 0, 1))
    title = pygame.Surface((500, 300))
    title.blit(titleTxt, (40, 10))
    title.blit(andTheTxt, (175, 40))
    title.blit(leapTxt, (75, 55))
    title.blit(ofTxt, (200, 70))
    title.blit(faithTxt, (240, 55))
    title.set_colorkey((0, 0, 0))
    
    # -------- BUTTON VISUALS ----------
    startTxt = pixelFontBig.render('START', False, (0, 0, 0))
    tutTxt = pixelFontBig.render('TUTORIAL', False, (0, 0, 0))
    quitTxt = pixelFontBig.render('QUIT', False, (0, 0, 0))
    
    # -------- PLAYER IMAGES ------------
    charImgs = [
        pygame.image.load('ImageAssets/Character/idle.png'),
        pygame.image.load('ImageAssets/Character/jumping.png'),
        pygame.image.load('ImageAssets/Character/tired.png'),
        pygame.image.load('ImageAssets/Character/death.png')
    ]
    
    # --------- BACKGROUND IMAGES -------
    blue = pygame.image.load('ImageAssets/Background/blue.png')
    grey = pygame.image.load('ImageAssets/Background/grey.png')
    white = pygame.image.load('ImageAssets/Background/white.png')
    blueCloud = pygame.image.load('ImageAssets/Background/blue_cloud.png')
    greyCloud = pygame.image.load('ImageAssets/Background/grey_cloud.png')
    
    # --------- NUMBER IMAGES ----------
    numImgs = [
        pygame.image.load('ImageAssets/Background/Nums/0.png'),
        pygame.image.load('ImageAssets/Background/Nums/1.png'),
        pygame.image.load('ImageAssets/Background/Nums/2.png'),
        pygame.image.load('ImageAssets/Background/Nums/3.png'),
        pygame.image.load('ImageAssets/Background/Nums/4.png'),
        pygame.image.load('ImageAssets/Background/Nums/5.png'),
        pygame.image.load('ImageAssets/Background/Nums/6.png'),
        pygame.image.load('ImageAssets/Background/Nums/7.png'),
        pygame.image.load('ImageAssets/Background/Nums/8.png'),
        pygame.image.load('ImageAssets/Background/Nums/9.png'),  
    ]
    
    # Creating background
    background = pygame.Surface((1500, 700))
    
    for x in range(0, 1500, 25):
        for y in range(0, 300, 25):
            background.blit(blue, (x, y))
        background.blit(blueCloud, (x, 300))
        for y in range(325, 425, 25):
            background.blit(white, (x, y))
        background.blit(greyCloud, (x, 425))
        for y in range(450, 700, 25):
            background.blit(grey, (x, y))
            
    background = pygame.transform.flip(background, False, True)
        
    bigGround = pygame.Surface((3000, 1400))
    
    bigGround.blit(background, (0, 0))
    bigGround.blit(background, (1500, 0))
    bigGround.blit(pygame.transform.flip(background, False, True), (0, 700)) # Bottom Left, Start Point
    bigGround.blit(pygame.transform.flip(background, False, True), (1500, 700)) # Bottom Right
    
    # finished creating bigGround (4 backgrounds meshed into one to allow it to move)
    
    # ------- TUTORIAL BACKGROUNDS -----
    # ------------- LEVEL 1 ------------
    tutBg1 = pygame.Surface((1500, 700))
    tutBg1.set_colorkey((0, 0, 0))
    tutBg1.blit(pixelFont.render('These are obstacles.', False, (0, 0, 1)), (625, 550))
    tutBg1.blit(pixelFont.render('You can collide with them.', False, (0, 0, 1)), (625, 575))
    tutBg1.blit(pixelFont.render('WASD or Arrow keys to move.', False, (0, 0, 1)), (25, 525))
    tutBg1.blit(pixelFont.render('This is your spawnpoint.', False, (0, 0, 1)), (25, 575))
    tutBg1.blit(pixelFont.render('This is your goal.', False, (0, 0, 1)), (1200, 575))
    
    # ------------- LEVEL 2 ------------
    tutBg2 = pygame.Surface((1500, 700))
    tutBg2.set_colorkey((0, 0, 0))
    
    # Bouncing
    tutBg2.blit(pixelFont.render('You can bounce on blue surfaces.', False, (0, 0, 1)), (200, 350))
    tutBg2.blit(pixelFont.render('The height of your bounce is', False, (0, 0, 1)), (200, 375))
    tutBg2.blit(pixelFont.render('equal to the height you bounced from.', False, (0, 0, 1)), (200, 400))
    tutBg2.blit(pixelFont.render('Holding \'LShift\' stops the bounce.', False, (0, 0, 1)), (200, 450))
    # Climbing
    tutBg2.blit(pixelFont.render('You can climb ladders', False, (0, 0, 1)), (900, 400))
    tutBg2.blit(pixelFont.render('by moving into them.', False, (0, 0, 1)), (900, 425))
    
    # ------------- LEVEL 3 -------------
    tutBg3 = pygame.Surface((1500, 700))
    tutBg3.set_colorkey((0, 0, 0))
    tutBg3.blit(pixelFont.render('Holding \'E\' permits', False, (0, 0, 1)), (200, 500))
    tutBg3.blit(pixelFont.render('hanging from green undersides', False, (0, 0, 1)), (200, 525))
    
    # ------------- LEVEL 4 -------------
    tutBg4 = pygame.Surface((1500, 700))
    tutBg4.set_colorkey((0, 0, 0))
    tutBg4.blit(pixelFont.render('Sometimes you may', False, (0, 0, 1)), (600, 100))
    tutBg4.blit(pixelFont.render('need to take a...', False, (0, 0, 1)), (600, 125))
    tutBg4.blit(pixelFontBiggest.render('LEAP OF FAITH', False, (50, 75, 150)), (400, 150))
    
    # ------------- ATTEMPTS ------------
    attemptSurf = pygame.Surface((200, 50))
    currAttemptTxt = pixelFontHuge.render(f'ATTEMPT {attempts}', False, (0, 0, 0))
    
    # tutorial backgrounds in list to load.
    tutBGS = [
        tutBg1,
        tutBg2,
        tutBg3,
        tutBg4
    ]
    
    # level iterator, clock, and display
    levIt = 0
    clock = pygame.time.Clock()
    mainSurface = pygame.display.set_mode((surfaceSizeX, surfaceSizeY))

    
    # ------------- OBJECTS ------------
    player = Player()
    startScreen = StartScreen()
    
    #---------------Main Program Loop---------------
    while True:
        
        ev = pygame.event.poll()
            
        # quit game
        if ev.type == pygame.QUIT:
            break
        
        if state == 'game':
            
            # --------- TERMINATION ------------
            state = terminators.terminate(player, tutorial)
            
            if state != 'game':
                continue
            
            mainSurface.blit(bigGround, (-player.block.left*0.4, -player.block.bottom*0.4))
            
            # ---------- POSITION UPDATE --------
            player.block.centerx += player.speedX
            player.block.centery += player.speedY    
                
            # -------- COLLISION MECHANIC ------
            player.jumping = True
            player.hanging = False

            gravity = 0.16/len(obstacles)

            for obstacle in obstacles:
                    
                # ---------- GRAVITY ----------------
                if player.jumping:
                    player.speedY += gravity
                
                # collision
                if obstacle.block.colliderect(player.block):
                    pushBack(player, obstacle)
                    
                # check if touching floor
                if obstacle.block.colliderect(player.block.left, player.block.bottom + 1, 25, 1):
                    player.jumping = False
                
                # hang from underside if possible
                obstacle.hang(player)
                
                # check if colliding with spike
                state = obstacle.spiky(player)
                if state != 'game':
                    frame = 0
                    attempts += 1
                    currAttemptTxt = pixelFontHuge.render(f'ATTEMPT {attempts}', False, (0, 0, 0))
                    break
                
                # climb if possible
                obstacle.climb(player)

            
            
            # ------------ JUMP --------------
            if ev.type == pygame.KEYDOWN:
                if (ev.key == pygame.K_w or ev.key == pygame.K_UP) and not player.jumping:
                    player.speedY = -5
                    player.jumping = True

            # ------------ MOVEMENT ------------
            if (pygame.key.get_pressed()[pygame.K_d] or pygame.key.get_pressed()[pygame.K_RIGHT]) and player.speedX <= 6:
                player.speedX += 0.2
            elif (pygame.key.get_pressed()[pygame.K_a] or pygame.key.get_pressed()[pygame.K_LEFT]) and player.speedX >= -6:
                player.speedX -= 0.2
            else:
                player.speedX = player.speedX * 0.92

            # ------------ DRAWING -------------
            mainSurface.blit(fullDrawing, (0, 0))
            mainSurface.blit(currAttemptTxt, (1150, 30))
            player.drawPlayer(mainSurface, charImgs)
            
        # ------------ OTHER STATES -----------
        elif state == 'start':
        
            # Draw all words
            mainSurface.fill((19, 168, 191))
            mainSurface.blit(bigGround, (0, 0))
            mainSurface.blit(startTxt, (698, 213))
            mainSurface.blit(tutTxt, (663, 313))
            mainSurface.blit(quitTxt, (705, 413))
            mainSurface.blit(title, (535, 50))
            
            # check for button clicks
            if ev.type == pygame.MOUSEBUTTONDOWN:
                state = startScreen.buttonClick()
            tutorial = False
            
            # reset level iterator
            levIt = 0
            
        # Next tutorial level
        elif state == 'tutorial' or state == 'next':
                
            # if completed tutorial, go to start screen.
            if tutorial and levIt == 4:
                state = 'start'
                attempts = 1
                currAttemptTxt = pixelFontHuge.render(f'ATTEMPT {attempts}', False, (0, 0, 0))
                continue
            
            if levIt == 7:
                state = 'win'
                winInit = False
                continue
    
            # get level information
            if state == 'tutorial':
                levelKeys = list(tutorials.keys())
                level = tutorials.get(levelKeys[levIt])
                tutorial = True # draw instructions
                
            else:
                levelKeys = list(screens.keys())
                level = screens.get(levelKeys[levIt])
                
            # set start and end points
            terminators = level[0]
    
            # Set current obstacles
            obstacles = level[1:]
            
            # Initialize obstacles and terminators drawing for whole level to blit on screen.
            pygame.draw.rect(fullDrawing, (0, 0, 0), (0, 0, 1500, 700))
            for obs in obstacles:
                if not obs.invis:
                    fullDrawing.blit(obs.obsSurf, (obs.block.left - 25, obs.block.top - 25))
                
            # start and end points
            terminators.drawTerms(fullDrawing)
            
            # level number
            fullDrawing.blit(pygame.transform.scale(numImgs[levIt + 1], (50, 50)), (10, 10))
            
            # Tutorial instructions
            if state == 'tutorial':
                fullDrawing.blit(tutBGS[levIt], (0, 0))
    
            fullDrawing.set_colorkey((0, 0, 0)) # make black transparent
            
            # teleport player to start and reset speed
            player.block.centerx, player.block.centery = terminators.startBlock.centerx, terminators.startBlock.centery
            player.speedX, player.speedY = 0, 0
            
            # go to game
            state = 'game'
                        
            levIt += 1
            
        # --------- RESPAWNING ----------
        elif state == 'death':
            
            # Draw level as usual
            mainSurface.blit(bigGround, (-player.block.left*0.4, -player.block.bottom*0.4))
            mainSurface.blit(fullDrawing, (0, 0))
            mainSurface.blit(currAttemptTxt, (1150, 30))
        
            # Flashing animation
            if frame >= 40:
                player.block.centerx, player.block.centery = terminators.startBlock.centerx, terminators.startBlock.centery
                if frame <= 60 or (80 <= frame <= 100) or (120 <= frame <= 140):
                    mainSurface.blit(charImgs[0], (player.block.left, player.block.top))
            else:
                mainSurface.blit(charImgs[3], (player.block.left, player.block.top))
                    
            # reset speed and jumping state
            if frame == 140:
                player.speedX, player.speedY = 0, 0
                player.jumping = False
                state = 'game'
                  
            frame += 1
            
            
        # Final win screen
        elif state == 'win':
            
            # Drawings
            if not winInit:
                winObs = Obstacle(0, 600, 800, 100, False, False, False, None, None)
                winObs2 = Obstacle(800, 575, 700, 125, False, False, False, None, None)
                congratTxt = pixelFontBiggest.render('Congratulations!', False, (0, 0, 0))
                totalAttemptsTxt = pixelFontHuge.render(f'TOTAL ATTEMPTS: {attempts}', False, (0, 0, 0))
                clickAnyTxt = pixelFontBig.render('click anywhere to return to the main screen.', False, (0, 0, 0))
                
            winInit = True
            
            # Draw drawings
            mainSurface.blit(bigGround, (-player.block.left*0.4, -player.block.bottom*0.4))
            player.block.left = 75
            player.block.top = 575
            player.drawPlayer(mainSurface, charImgs)
            mainSurface.blit(winObs.obsSurf, (winObs.block.left - 25, winObs.block.top - 25))
            mainSurface.blit(winObs2.obsSurf, (winObs2.block.left - 25, winObs2.block.top - 25))
            mainSurface.blit(congratTxt, (400, 200))
            mainSurface.blit(totalAttemptsTxt, (400, 300))
            mainSurface.blit(clickAnyTxt, (400, 350))
            
            # Click anywhere to continue
            if ev.type == pygame.MOUSEBUTTONDOWN:
                state = 'start'
                attempts = 1
                currAttemptTxt = pixelFontHuge.render(f'ATTEMPT {attempts}', False, (0, 0, 0))
                
        # quit game
        else:
            break
            
        
        pygame.display.flip()
        
        clock.tick(60)

    pygame.quit() # Once we leave the loop, close the window.


def pushBack(player, obs):

    # Top of the obstacle
    if (player.block.bottom - (abs(player.speedY) + 1)) <= obs.block.top:
        player.block.bottom = obs.block.top
        
        # Bounce
        if obs.bouncy and not pygame.key.get_pressed()[pygame.K_LSHIFT]:
            player.speedY = -(math.floor(player.speedY) + 0.05)
            
        # No bounce or Lshift is pressed
        else:
            player.jumping = False
            player.speedY = 0.0
        
    # Bottom of the obstacle
    elif (player.block.top + (abs(player.speedY) + 1)) >= obs.block.bottom:
        player.block.top = obs.block.bottom
        player.speedY = 0.0
        
    # right side of the obstacle
    elif player.speedX < 0:
        player.block.left = obs.block.right
        player.speedX = 0.0
        
    # left side of the obstacle
    elif player.speedX > 0:
        player.block.right = obs.block.left
        player.speedX = 0.0
    

main()