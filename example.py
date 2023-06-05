import pygame
from datetime import datetime, timedelta

from batch import Plant
from equipment import Telebelt
from truck import Truck

def calculate_travel_speed(batch_time, arrive_time):
    pass


def check_trip_start(trips, actual_datetime):
    trips_initiated = []
    for trip in trips:
        if trip['batch_time'] == actual_datetime:
            trip['status'] = 'started'
            trips_initiated.append(trip)
    return trips_initiated

def check_trip_ended(started_trips, actual_datetime):
    for trip in started_trips:
        if trip['finish_time'] == actual_datetime:
            print(f'trip con id: {trip["id"]} eliminado...')
            started_trips.remove(trip)
            

pygame.init()

WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

#DATE information
start_datetime = datetime(2013,11,14,6,27)
end_datetime = datetime(2013,11,14,6,45)
duration = end_datetime - start_datetime
duration = duration.total_seconds() // 60
actual_datetime = start_datetime

SCREEN_WIDTH = 600
SCREEN_HEIGTH = 600
display_screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGTH))
pygame.display.set_caption("Time Simulation")

system_font = pygame.font.SysFont("calibri", 34)

# Create Batch Plant
main_batch_plant = Plant(60,300,60,60)
# Create list with Telebelts
telebelts = [
    {'id': 1, 'equipment':Telebelt(520,100,60,60)},
    {'id':2, 'equipment': Telebelt(520,500,60,60)},
]
# Create list with concrete trucks
concrete_trucks = [
    {'id':1, 'truck': Truck(0,0,40,40)},
    {'id': 2, 'truck': Truck(0,0,40,40)}
]

# Trips to deliver concrete
trips = [
    {'id': 1,
     'truck': concrete_trucks[1],
     'equipment': telebelts[0],
     'batch_time': datetime(2013,11,14,6,32),
     'arrive_time': datetime(2013,11,14,6,35),
     'start_time': datetime(2013,11,14,6,38),
     'finish_time': datetime(2013,11,14,6,38),
     'status': 'not_started',
     },
    {'id': 2,
     'truck': concrete_trucks[0],
     'equipment': telebelts[1],
     'batch_time': datetime(2013,11,14,6,36),
     'arrive_time': datetime(2013,11,14,6,39),
     'start_time': datetime(2013,11,14,6,42),
     'finish_time': datetime(2013,11,14,6,43),
     'status':'not_started',
     },
    
]


running = True
clock = pygame.time.Clock()
t = 0
started_trips = []

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    # Other game code here
    
    # Update time in screen
    system_text = system_font.render(f"DATE: {actual_datetime}", True, WHITE)
    system_text_rect = system_text.get_rect()
    system_text_rect.topleft = (0,0)
    
    # Check if trip started
    started_trips += check_trip_start(trips, actual_datetime)
    check_trip_ended(started_trips, actual_datetime)
    print(started_trips)
    
    #Fill the display surface to cover old images
    display_screen.fill(BLACK)
    #Draw Main Batch Plant
    pygame.draw.rect(display_screen,WHITE,(main_batch_plant.pos_x,
                                           main_batch_plant.pos_y,
                                           main_batch_plant.width,
                                           main_batch_plant.height))
    # Draw Telebelts
    for telebelt in telebelts:
        pygame.draw.rect(display_screen, RED,
                         (telebelt['equipment'].pos_x,
                          telebelt['equipment'].pos_y,
                          telebelt['equipment'].width,
                          telebelt['equipment'].height))
        
    # Draw concrete trucks
    if len(started_trips) > 0:
        for trip in started_trips:
            display_screen.blit(trip['truck']['truck'].truck_image, trip['truck']['truck'].truck_rect)
            
    display_screen.blit(system_text, system_text_rect)
    pygame.display.update()
    clock.tick(1)
    print(t)
    t = t + 1
    actual_datetime += timedelta(minutes=1)
    if t > duration:
        break
    