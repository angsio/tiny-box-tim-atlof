from Obstacle import Obstacle
from Terminators import Terminators

# Parameters in Obstacle in order:
# Bouncy, Hangable, Invisible, Climbable Surfaces, Spikes

# tutorial levels
tutorials = {
  
    'tutorial_1': [
        Terminators(50, 675, 1300, 675),
        
        Obstacle(0, 700, 1500, 25, False, False, False, None, None), # Floor
        Obstacle(750, 650, 50, 50, False, False, False, None, None), # Block
        Obstacle(-25, 0, 25, 700, False, False, False, None, None), # Left Wall
        Obstacle(1500, 0, 25, 700, False, False, False, None, None) # Right Wall
        
    ],
    
    'tutorial_2': [
        Terminators(25, 675, 1400, 675),
        
        Obstacle(0, 700, 1500, 25, False, False, False, None, None), # Floor
        Obstacle(300, 675, 50, 25, True, False, False, None, None), # Bounce
        Obstacle(900, 600, 50, 100, False, False, False, ['left', 'right'], None), # Climbable
        Obstacle(-25, 0, 25, 700, False, False, False, None, None), # Left Wall
        Obstacle(1500, 0, 25, 700, False, False, False, None, None) # Right Wall
    ],
    
    'tutorial_3': [
        Terminators(0, 675, 300, 375),
        
        Obstacle(0, 700, 100, 25, False, False, False, None, None), # Floor1
        Obstacle(100, 700, 1500, 25, False, False, False, None, ['top']), # Floor2
        Obstacle(50, 500, 50, 200, False, False, False, ['left', 'right'], None), # Pillar
        Obstacle(50, 400, 350, 50, False, True, False, None, ['left']), # Ceiling 1
        Obstacle(900, 400, 400, 50, False, True, False, ['right'], None), # Ceiling 2
        Obstacle(625, 675, 75, 25, True, False, False, None, None), # Bounce Pad
        Obstacle(1300, 500, 200, 200, False, False, False, None, ['left']), # End
        Obstacle(-25, 0, 25, 700, False, False, False, None, None), # Left Wall
        Obstacle(1500, 0, 25, 700, False, False, False, None, None) # Right Wall
    ],
    
    'tutorial_4': [
        Terminators(25, 400, 1450, 400),
        
        Obstacle(-25, 0, 25, 700, False, False, False, None, None), # Left Wall
        Obstacle(1500, 0, 25, 700, False, False, False, None, None), # Right Wall
        Obstacle(0, 700, 1500, 25, False, False, False, None, ['top']), # Floor
        
        Obstacle(0, 425, 300, 275, False, False, False, None, None), # Start Plat
        Obstacle(1200, 425, 300, 275, False, False, False, None, None), # End Plat
        Obstacle(300, 500, 900, 150, False, False, True, None, None) # Invis platform
    ]

}

# All normal levels
screens = {
    'level_1': [
        Terminators(25, 375, 1225, 275),
        
        Obstacle(0, 700, 1500, 25, False, False, False, None, ['top']), # Floor
        Obstacle(0, 400, 200, 300, False, False, False, None, None), # Start
        Obstacle(300, 450, 100, 250, False, False, False, None, None), # Plat 1
        Obstacle(500, 500, 100, 200, False, False, False, None, None), # Plat 2
        Obstacle(700, 550, 100, 200, False, False, False, None, None), # Plat 3
        Obstacle(900, 300, 100, 400, False, False, False, ['left'], None), # Plat 4
        Obstacle(1200, 300, 50, 400, False, False, False, None, None), # Final
        Obstacle(-25, 0, 25, 700, False, False, False, None, None), # Left Wall
        Obstacle(1500, 0, 25, 700, False, False, False, None, None) # Right Wall
    ],
    
    'level_2': [
        Terminators(25, 475, 0, 275),
        
        Obstacle(0, 700, 1500, 25, False, False, False, None, ['top']), # Floor
        Obstacle(0, 500, 200, 200, False, False, False, None, None), # Start
        Obstacle(500, 675, 50, 25, True, False, False, None, None), # First Bounce
        Obstacle(1000, 675, 50, 25, True, False, False, None, None), # Second Bounce
        Obstacle(1450, 300, 50, 200, False, False, False, ['left'], None), # Checkpoint
        Obstacle(0, 300, 50, 50, False, False, False, ['right'], None), # Final Plat
        Obstacle(-25, 0, 25, 700, False, False, False, None, None), # Left Wall
        Obstacle(1500, 0, 25, 700, False, False, False, None, None) # Right Wall
    ],
    
    
    
    'level_3': [
        Terminators(25, 525, 25, 125),
        
        Obstacle(-25, 0, 25, 700, False, False, False, None, None), # Left Wall
        Obstacle(1500, 0, 25, 700, False, False, False, None, None), # Right Wall
        Obstacle(0, 700, 1500, 25, False, False, False, None, ['top']), # Floor
        
        Obstacle(0, 550, 200, 150, False, False, False, None, ['right']), # Start
        Obstacle(250, 300, 200, 400, True, False, False, ['left'], ['right']), # Plat 1 Bouncy
        Obstacle(600, 500, 200, 200, True, False, False, None, ['left']), # Plat 2 TrickBounce
        Obstacle(600, 250, 250, 125, False, False, False, None, ['left', 'right', 'top', 'bottom']), # Spike Obstacle
        Obstacle(1000, 650, 100, 50, True, False, False, None, None), # Bouncy 3
        Obstacle(1400, 200, 100, 350, False, False, False, ['left'], None), # Climb 1
        Obstacle(0, 150, 100, 25, False, False, False, None, None)   
    ],
    
    'level_4': [
        Terminators(50, 475, 50, 125),
        Obstacle(0, 150, 100, 25, False, False, False, None, None), # Exit Plat
        
        Obstacle(-25, 0, 25, 700, False, False, False, None, None), # Left Wall
        Obstacle(1500, 0, 25, 700, False, False, False, None, None), # Right Wall
        Obstacle(0, 700, 1500, 25, False, False, False, None, ['top']), # Floor
        
        Obstacle(25, 500, 75, 200, False, False, False, None, None), # Start / Checkpoint 1
        Obstacle(150, 600, 100, 100, True, False, False, None, None), # Bounce 1
        
        Obstacle(175, 400, 50, 150, True, False, False, None, ['bottom']), # Spike 1
        Obstacle(250, 325, 50, 150, True, False, False, None, ['bottom']), # Spike 2
        Obstacle(350, 250, 50, 150, True, False, False, None, ['bottom']), # Spike 3
        Obstacle(300, 550, 75, 150, False, False, False, None, None), # Checkpoint 2
        Obstacle(550, 400, 100, 350, False, False, False, ['left'], None), # Coaster 1
        Obstacle(900, 650, 50, 50, True, False, False, None, None), # Bounce 2
        Obstacle(1150, 200, 100, 550, False, False, False, ['left'], None) # Coaster 2
        
        
    ],
    
    'level_5': [
        Terminators(50, 650, 50, 100),
        
        Obstacle(-25, 0, 25, 700, False, False, False, None, None), # Left Wall
        Obstacle(1500, 0, 25, 700, False, False, False, None, None), # Right Wall
        Obstacle(0, 700, 1500, 25, False, False, False, None, ['top']), # Floor
        Obstacle(0, -25, 1500, 25, False, False, False, None, None), # Ceiling
        Obstacle(300, 550, 150, 150, False, False, False, ['left'], ['right']), # Climb 1
        Obstacle(300, 450, 150, 100, False, False, False, None, ['left', 'right']), # Spike 1
        Obstacle(0, 350, 250, 250, False, False, False, ['right'], ['top']), # Climb 2
        Obstacle(300, 350, 150, 100, False, False, False, ['left'], ['right']), # Climb 3
        Obstacle(0, 675, 300, 25, False, False, False, None, None), # Actual Floor
        
        
        Obstacle(500, 675, 50, 25, True, False, False, None, None), # Bounce 1
        Obstacle(600, 350, 100, 350, False, False, False, None, ['top', 'right', 'left']), # TallSpike 1
        Obstacle(750, 675, 50, 25, True, False, False, None, None), # Bounce 2
        Obstacle(850, 350, 100, 350, False, False, False, None, ['top', 'right', 'left']), # TallSpike 2
        Obstacle(1000, 675, 50, 25, True, False, False, None, None), # Bounce 3
        Obstacle(1100, 350, 100, 350, False, False, False, None, ['top', 'right', 'left']), # TallSpike 3
        Obstacle(1250, 675, 50, 25, True, False, False, None, None), # Bounce 4
        Obstacle(1350, 25, 150, 676, False, False, False, ['left'], None), # Climb
        Obstacle(1350, 0, 150, 25, False, False, False, None, ['left']), # Climb End Spike
        Obstacle(1275, 75, 25, 25, False, False, False, ['right'], None), # Checkpoint
        
        # Hangables
        Obstacle(1100, 0, 200, 25, False, True, False, None, None), # Hang 1
        Obstacle(850, 0, 100, 25, False, True, False, None, None), # Hang 2
        Obstacle(600, 0, 100, 25, False, True, False, None, None), # Hang 3
        Obstacle(0, 0, 450, 25, False, True, False, None, None), # Hang 4
        
        Obstacle(1100, 75, 100, 150, False, False, False, None, ['top', 'bottom', 'left', 'right']), # Spike Block 1
        Obstacle(850, 75, 100, 150, False, False, False, None, ['top', 'bottom', 'left', 'right']), # Spike Block 2
        Obstacle(600, 75, 100, 150, False, False, False, None, ['top', 'bottom', 'left', 'right']) # Spike Block 3
        
        
    ],
    
    'final_level': [
        Terminators(675, 350, 825, 400),
        
        Obstacle(0, 700, 1500, 25, False, False, False, None, ['top']), # Floor
        Obstacle(-25, 0, 25, 700, False, False, False, None, ['right']), # Left Wall
        Obstacle(1500, 0, 25, 700, False, False, False, None, ['left']), # Right Wall
        
        Obstacle(650, 375, 75, 25, False, False, False, None, None), # spawn platform
        Obstacle(575, 225, 25, 200, False, False, False, None, ['left', 'right', 'bottom', 'top']), # left spawn spike
        Obstacle(775, 225, 25, 475, False, False, False, None, ['top', 'left', 'right']), # right spawn spike
        Obstacle(600, 175, 175, 75, False, False, False, None, ['top', 'bottom']), # top spawn spike
        
        Obstacle(550, 675, 225, 25, True, False, False, None, None), # Bounce Pad Spawn
        Obstacle(225, 275, 350, 25, True, True, False, None, ['left']), # Hang 1
        Obstacle(125, 275, 100, 25, False, False, False, None, ['top', 'bottom']), # hang spike
        Obstacle(125, 375, 100, 25, True, False, False, None, None), # Bounce Pad 1
        Obstacle(325, 0, 75, 175, False, False, False, None, ['left', 'bottom', 'right']), # Annoying Bounce Spike
        Obstacle(225, 350, 25, 125, False, False, False, None, ['top', 'right', 'bottom']), # Cheese prevention spike
        Obstacle(0, 100, 100, 225, False, False, False, ['right'], ['top']), # Climb Wall
        
        Obstacle(875, 0, 625, 200, False, False, False, None, ['left', 'bottom']), # BIG SPIKE BLOCK
        Obstacle(800, 250, 125, 25, True, False, False, None, ['right']), # FAKE BOUNCE
        Obstacle(900, 275, 25, 225, False, False, False, None, ['left', 'right', 'bottom']), # Spike 2
        Obstacle(1100, 375, 300, 250, False, False, False, None, ['top', 'right', 'left', 'bottom']), # BIG SPIKE BLOCK 2
        Obstacle(1450, 375, 50, 25, False, False, False, None, ['top', 'left', 'bottom']), # random anger fuelling spike block
        Obstacle(1400, 550, 25, 25, False, False, False, None, ['top', 'right', 'bottom']), # anger fuelling spike block 2
        Obstacle(1475, 550, 25, 25, False, False, False, None, ['top', 'left', 'bottom']), # anger fuelling spike block 3
        Obstacle(925, 375, 175, 25, True, False, False, None, ['bottom']), # Bounce 2
        Obstacle(1100, 200, 300, 50, False, True, False, None, None), # Hang 2
        
        
        Obstacle(1000, 450, 50, 250, False, False, False, ['right'], None), # climb 2
        Obstacle(1050, 675, 450, 25, True, False, False, None, None), # totally not deceptive bouncy floor
        Obstacle(925, 675, 75, 25, True, False, False, None, None), # bouncy 3
        Obstacle(800, 425, 50, 100, False, False, False, ['right'], None), # final climb
        Obstacle(800, 525, 50, 175, False, False, False, None, ['right'])
    ],
    
    'tutorial_4': [
        Terminators(25, 400, 1450, 400),
        
        Obstacle(-25, 0, 25, 700, False, False, False, None, None), # Left Wall
        Obstacle(1500, 0, 25, 700, False, False, False, None, None), # Right Wall
        Obstacle(0, 700, 1500, 25, False, False, False, None, ['top']), # Floor
        
        Obstacle(0, 425, 300, 275, False, False, False, None, None), # Start Plat
        Obstacle(1200, 425, 300, 275, False, False, False, None, None), # End Plat
        Obstacle(300, 500, 900, 150, False, False, True, None, None) # Invis platform
    ]
}