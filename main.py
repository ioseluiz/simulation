import pygame

# pygame setup
pygame.init()

# Define colors
BLACK = (0,0,0)
WHITE = (255,255,255)
GREEN = (0,255,0)
RED = (255,0,0)
BLUE = (0,0,255)

screen = pygame.display.set_mode((800,500))
clock = pygame.time.Clock() # Control FPS
running = True

cord_x = 400
cord_y = 200

# Speed in which rect will move
speed_x = 3
speed_y = 3




while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close the window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    if (cord_x > 720 or cord_x < 0):   
        speed_x *= -1
    if (cord_y > 320 or cord_y < 0):
        speed_y *= -1
        
    cord_x += speed_x
    cord_y += speed_y
            
    # fill the screen with a color to wipe away anything from last frame
    screen.fill('purple')
    
    # RENDER YOUR GAME HERE
    pygame.draw.rect(screen, RED, (cord_x,cord_y,80,80))
    
    
    
    # flip() the display to put your work on screen
    pygame.display.flip()
    
    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-independent physics.
    clock.tick(60)
    
pygame.quit()