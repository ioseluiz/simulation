import pygame

class Truck:
    def __init__(self,pos_x, pos_y,width,height):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.width = width
        self.height = height
        self.image_path = 'truck.png'
        self.create_truck_image()
        
    def create_truck_image(self):
        truck_image = pygame.image.load(self.image_path)
        DEFAULT_IMAGE_SIZE = (50, 50)
        # Scale the image to your needed size
        self.truck_image = pygame.transform.scale(truck_image, DEFAULT_IMAGE_SIZE)
        self.truck_rect = self.truck_image.get_rect()
        self.truck_rect.center = (150, 330)
        
       
        
        