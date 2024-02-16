import pygame

class Terminators:
    
    exitImg = pygame.image.load('ImageAssets/Other/exit.png')
    
    def __init__(self, x1, y1, x2, y2):
        self.startBlock = pygame.Rect(x1, y1, 25, 25)
        self.endBlock = pygame.Rect(x2, y2, 25, 25)
        
    def drawTerms(self, surface):
        surface.blit(Terminators.exitImg, (self.startBlock.left, self.startBlock.top)) # Starting block
        surface.blit(Terminators.exitImg, (self.endBlock.left, self.endBlock.top))
        
    def terminate(self, player, tutorial):
        if player.block.colliderect(self.endBlock):
            if tutorial:
                return 'tutorial'
            else:
                return 'next'
        else:
            return 'game'