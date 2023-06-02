import pygame
from datetime import datetime, timedelta


def simulation(start, end):
    actual_date = start
    while actual_date < end:
        print(actual_date)
        actual_date += timedelta(minutes=1)

#initialize pygame
pygame.init()

#Start and End datetime of the simulation
start_datetime = datetime(2013,11,25,6,11)
end_datetime = datetime(2013,11,25,16,45)
duration = end_datetime - start_datetime
duration = int(duration.total_seconds() / 60) # minutes

# Scale total time interval to 5 minutes
scale_factor = 5/duration
print(scale_factor)

# Screen Size
WINDOW_WIDTH = 600
WINDOW_HEIGTH = 400

# COLORS
RED = (255,0,0)
BLUE = (0,0,255)
GREEN = (0,255,0)
BLACK = (0,0,0)
WHITE = (255,255,255)

# Create a display surface
display_surface = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGTH))
pygame.display.set_caption("Concrete Truck Simulation")
clock = pygame.time.Clock()

#See all available system fonts
# fonts = pygame.font.get_fonts()
# for font in fonts:
#     print(font)

# Define fonts
system_font = pygame.font.SysFont(None, 48)
system_text = system_font.render(f"DATE: {start_datetime}", True, WHITE)
system_text_rect = system_text.get_rect()
system_text_rect.topleft=(0,0)


# Main Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    duration 
    display_surface.blit(system_text, system_text_rect)
    pygame.display.update()

pygame.quit()