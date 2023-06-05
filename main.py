import pygame
import time
from utils import calc_total_distance, calc_speed

class Truck:
    def __init__(self, cord_x, cord_y):
        self.cord_x = cord_x
        self.cord_y = cord_y
        DEFAULT_IMAGE_SIZE = (80, 80)
        self.truck = pygame.image.load('truck.png')
        self.truck = pygame.transform.scale(self.truck, DEFAULT_IMAGE_SIZE)
        self.truck.convert()
        self.truck_rect = self.truck.get_rect()
        self.truck_rect.center = cord_x, cord_y
        self.path = [(self.cord_x, self.cord_y),(600,self.cord_y),(600,100)]
        self.distance = calc_total_distance(self.path)
        self.speed = calc_speed(self.distance, 0,5)

    


    
    def move(self,speed_x,speed_y):
        return self.truck_rect.move(speed_x, speed_y)
    
class Plant:
    def __init__(self, cord_x, cord_y):
        self.cord_x = cord_x
        self.cord_y = cord_y
        DEFAULT_IMAGE_SIZE = (80, 80)
        self.batch = pygame.image.load('batch_plant.png')
        self.batch = pygame.transform.scale(self.batch, DEFAULT_IMAGE_SIZE)
        self.batch.convert()
        self.batch_rect = self.batch.get_rect()
        self.batch_rect.center = cord_x, cord_y


def main():
    # pygame setup
    pygame.init()

    # Define Colors
    BLACK = (0,0,0)
    WHITE = (255,255,255)
    GREEN = (0,255,255)
    RED = (255,0,0)
    BLUE = (0,0,255)

    # Set the size for the image
    DEFAULT_IMAGE_SIZE = (80, 80)

    #text = "DATE: "
    screen = pygame.display.set_mode((800,500))
    pygame.display.set_caption("Concrete Truck Simulation")
    sysfont = pygame.font.get_default_font()
    print('system font :', sysfont)

    clock = pygame.time.Clock()
    running = True

    coord_x = 400
    coord_y = 200

    # Speed in which rect will move
    speed_x = 3
    speed_y = 0

    #t0 = time.time()
    
    #print('time needed for Font creation: ',time.time()-t0)

    # truck = pygame.image.load('truck.png')
    # truck = pygame.transform.scale(truck, DEFAULT_IMAGE_SIZE)
    # truck.convert()
    # truck_rect = truck.get_rect()
    # truck_rect.center = coord_x, coord_y
    truck_1 = Truck(coord_x, coord_y)
    font = pygame.font.SysFont(None, 48)
    time = clock.get_time()
    img = font.render('Time taken: {} ms'.format(time), True, (0, 0, 0))
    

   

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        time = pygame.time.get_ticks()
        font = pygame.font.SysFont(None, 48)
        img = font.render('Time taken: {} s'.format(time/1000), True, (0, 0, 0))
        


        if (coord_x > 720 or coord_x < 0):
            speed_x *= -1

        coord_x += speed_x

        # fill the screen with a color to wipe away anything from the last frame
        screen.fill(WHITE)
        screen.blit(img, (20,20))

        #screen.blit(truck, truck_rect)

        # RENDER YOUR GAME HERE
        #pygame.draw.rect(screen, RED, (coord_x, coord_y, 80, 80))
        truck_1.truck_rect = truck_1.move(speed_x,speed_y)
        screen.blit(truck_1.truck, truck_1.truck_rect)
        pygame.display.update()

        # flip() the display to put your work on screen
        #pygame.display.flip()

        # limits FPS to 60
        clock.tick(60)

    pygame.quit()


if __name__ == '__main__':
    main()