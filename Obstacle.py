import pygame
import random


class Obstacle:
    
    # ------------ BLOCK IMAGE TYPES ---------------
    blockImgs = [
        [ # --------------- DIRT ---------------
            pygame.image.load('ImageAssets/Obstacles/Ground/top.png'),
            pygame.image.load('ImageAssets/Obstacles/Ground/dirt.png'),
            pygame.image.load('ImageAssets/Obstacles/Ground/leftDirt.png'),
            pygame.image.load('ImageAssets/Obstacles/Ground/rightDirt.png'),
            pygame.image.load('ImageAssets/Obstacles/Ground/top_left.png'),
            pygame.image.load('ImageAssets/Obstacles/Ground/top_right.png'),
            
            pygame.image.load('ImageAssets/Obstacles/Ground/bot_left.png'),
            pygame.image.load('ImageAssets/Obstacles/Ground/bot_right.png'),
            pygame.image.load('ImageAssets/Obstacles/Ground/bottom.png')
        ],
        
        [ # ----------- INDUSTRIAL -------------
            pygame.image.load('ImageAssets/Obstacles/Industrial/top.png'),
            pygame.image.load('ImageAssets/Obstacles/Industrial/dirt.png'),
            pygame.image.load('ImageAssets/Obstacles/Industrial/leftDirt.png'),
            pygame.image.load('ImageAssets/Obstacles/Industrial/rightDirt.png'),
            pygame.image.load('ImageAssets/Obstacles/Industrial/top_left.png'),
            pygame.image.load('ImageAssets/Obstacles/Industrial/top_right.png'),
            
            pygame.image.load('ImageAssets/Obstacles/Industrial/bot_left.png'),
            pygame.image.load('ImageAssets/Obstacles/Industrial/bot_right.png'),
            pygame.image.load('ImageAssets/Obstacles/Industrial/bottom.png')
        ],
        
        [ # ------------- GIRDERS --------------
            pygame.image.load('ImageAssets/Obstacles/Extra/leftGirder.png'),
            pygame.image.load('ImageAssets/Obstacles/Extra/leftGirder2.png'),
            pygame.image.load('ImageAssets/Obstacles/Extra/rightGirder.png'),
            pygame.image.load('ImageAssets/Obstacles/Extra/rightGirder2.png'),
            pygame.image.load('ImageAssets/Obstacles/Extra/midGirder.png'),
            pygame.image.load('ImageAssets/Obstacles/Extra/midGirder2.png')
            
        ]
    ]
    
    img25 = pygame.image.load('ImageAssets/Obstacles/Extra/25x25.png')
    
    # Ladder and Spike images
    spikeImg = pygame.image.load('ImageAssets/Other/spike.png')
    laddImg = pygame.image.load('ImageAssets/Other/ladder.png')
    
    def __init__(self, sizeX, sizeY, width, height, bouncy, hangable, invis, climbableSurfs, spikes):
        self.bouncy = bouncy
        self.hangable = hangable
        self.invis = invis
        self.climbableSurfs = climbableSurfs
        self.color = (0, 100, 255)
        self.block = pygame.Rect(sizeX, sizeY, width, height)
        self.spikes = spikes
        
        # Unique drawing per obstacle
        self.obsSurf = pygame.Surface((self.block.width + 50, self.block.height + 50))
        
        if not self.invis:
            
            if self.block.height == 25 and self.block.width == 25:
                
                self.obsSurf.blit(Obstacle.img25, (25, 25))
            
            elif self.block.height == 25 and self.block.width != 25:
                
                for x in range(50, self.block.width, 25):
                    self.obsSurf.blit(Obstacle.blockImgs[2][random.randint(4, 5)], (x, 25))
                    
                self.obsSurf.blit(Obstacle.blockImgs[2][random.randint(0, 1)], (25, 25))
                self.obsSurf.blit(Obstacle.blockImgs[2][random.randint(2, 3)], (self.block.width, 25))
                
                
            
            else:
                # ---------- OBSTACLE BLOCK DRAWINGS ---------------
                
                v = random.randint(0, 1) # variant
                
                # ------------- DIRT VARIANT ------------------
                # top left and top right
                self.obsSurf.blit(Obstacle.blockImgs[v][4], (25, 25))
                self.obsSurf.blit(Obstacle.blockImgs[v][5], (self.block.width, 25))
                
                # bottom left and bottom right
                self.obsSurf.blit(Obstacle.blockImgs[v][6], (25, self.block.height))
                self.obsSurf.blit(Obstacle.blockImgs[v][7], (self.block.width, self.block.height))
                
                # left and right sides
                for y in range(50, self.block.height, 25):
                    self.obsSurf.blit(Obstacle.blockImgs[v][2], (25, y))
                    self.obsSurf.blit(Obstacle.blockImgs[v][3], (self.block.width, y))
                    
                # middle
                for x in range(50, self.block.width, 25):
                    self.obsSurf.blit(Obstacle.blockImgs[v][0], (x, 25)) # top
                    self.obsSurf.blit(Obstacle.blockImgs[v][8], (x, self.block.height)) # bottom
                    for y in range(50, self.block.height, 25):
                        self.obsSurf.blit(Obstacle.blockImgs[v][1], (x, y))
                        
                









            # --------- DRAW SPIKES -----------
            if self.spikes != None:
                for spike in self.spikes:
                    if spike == 'left':
                        for y in range(25, self.block.height + 25, 25):
                            self.obsSurf.blit(pygame.transform.rotate(Obstacle.spikeImg, 90), (0, y))
                    elif spike == 'right':
                        for y in range(25, self.block.height + 25, 25):
                            self.obsSurf.blit(pygame.transform.rotate(Obstacle.spikeImg, -90), (self.block.width + 25, y))
                    elif spike == 'top':
                        for x in range(25, self.block.width + 25, 25):
                            self.obsSurf.blit(Obstacle.spikeImg, (x, 0))
                    elif spike == 'bottom':
                        for x in range(25, self.block.width + 25, 25):
                            self.obsSurf.blit(pygame.transform.flip(Obstacle.spikeImg, False, True), (x, self.block.height + 25))
                            
            # -------- DRAW LADDERS ----------
            if climbableSurfs != None:
                for surf in climbableSurfs:
                    for y in range(25, self.block.height + 25, 25):
                        if surf == 'right':
                            self.obsSurf.blit(Obstacle.laddImg, (self.block.width + 25, y))
                        elif surf == 'left':
                            self.obsSurf.blit(pygame.transform.flip(Obstacle.laddImg, True, False), (0, y))
            
            # Draw green underside if hangable obstacle
            if self.hangable:
                pygame.draw.rect(self.obsSurf, (50, 200, 70), (25, self.block.height + 25, self.block.width, 5))
            
            # Draw blue surface if bouncy obstacle
            if self.bouncy:
                pygame.draw.rect(self.obsSurf, (5, 230, 255), (25, 20, self.block.width, 5))
                    
            # make black transparent
            self.obsSurf.set_colorkey((0, 0, 0))

        # add collidable spikes
        if spikes != None:
            
            self.spikeList = []
            
            for spike in self.spikes:
                
                if spike == 'top':
                    self.spikeList.append(pygame.Rect(self.block.left, self.block.top - 5, self.block.width, 5))
                    
                elif spike == 'bottom':
                    self.spikeList.append(pygame.Rect(self.block.left, self.block.bottom, self.block.width, 5))
                    
                elif spike == 'right':
                    self.spikeList.append(pygame.Rect(self.block.right, self.block.top, 5, self.block.height))
                
                elif spike == 'left':
                    self.spikeList.append(pygame.Rect(self.block.left - 5, self.block.top, 5, self.block.height))
                    
        
                    
    # --------- SPIKE COLLISION -------
    def spiky(self, player):
        
        if self.spikes != None:
            for spike in self.spikeList:
                if player.block.colliderect(spike):
                    return 'death'
        return 'game'
    
    # ---------- CLIMBING -------------
    def climb(self, player):
        
        if self.climbableSurfs != None:
            
            if 'left' in self.climbableSurfs and self.block.colliderect(pygame.Rect(player.block.right, player.block.top, 1, player.block.height)) and (pygame.key.get_pressed()[pygame.K_d] or pygame.key.get_pressed()[pygame.K_RIGHT]):
                player.speedX = 0.0
                player.speedY = 0.0
                player.block.centery -= 3
                
            elif 'right' in self.climbableSurfs and self.block.colliderect(pygame.Rect(player.block.left - 1, player.block.top, 1, player.block.height)) and (pygame.key.get_pressed()[pygame.K_a] or pygame.key.get_pressed()[pygame.K_LEFT]):
                player.block.left = self.block.right
                player.speedX = 0.0
                player.speedY = 0.0
                player.block.centery -= 3

    # ----------- HANGING ------------
    def hang(self, player):
        
        if self.block.colliderect(pygame.Rect(player.block.left, player.block.top - 7, 25, 1)) and pygame.key.get_pressed()[pygame.K_e] and self.hangable:
            player.block.top = self.block.bottom
            player.hanging = True
            player.speedY = 0.0