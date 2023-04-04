import pygame
import math

class Sun:
    
    def __init__(self) -> None:
        self.x = 60
        self.y = 100
        self.radius = 40
        self.fi = 235
        self.fi_start = self.fi
        self.fi_step = 0.2
        self.fi_stop = 305
        self.x_center_tarectory = 400
        self.y_center_tarectory = 600
        self.radius_traectory = 500
        self.steps_total = 350
    
        
    def set_display(self, size: list):
        self.x_center_tarectory = size[0] / 2
        self.y_center_tarectory = size[1]
        self.radius_traectory = size[1] - 100
    
        
    def set_start_position(self, start):
        self.fi_start = start
        self.fi_stop = (270 - self.fi_start) + 270
        self.steps_total = ((self.fi_stop - self.fi_start) / self.fi_step)
        
    
    def set_position(self, x, y):
        self.x = x
        self.y = y
    
    
    def get_degree(self):
        return self.fi
    
    
    def draw(self, screen):
        pygame.draw.circle(screen, "yellow", [self.x, self.y], self.radius)
    
        
    def move(self, screen):
        if self.fi < self.fi_stop:
            self.fi += self.fi_step
        
        self.x = self.x_center_tarectory + self.radius_traectory * (math.cos(math.radians(self.fi)))
        self.y = self.y_center_tarectory + self.radius_traectory * (math.sin(math.radians(self.fi)))
        
        self.draw(screen)
    
    
    
    
# sun = Sun()
# print(f'fi_start = {sun.fi_start} and fi_stop = {sun.fi_stop}')

# sun.set_start_position(210)

# print(f'fi_start = {sun.fi_start} and fi_stop = {sun.fi_stop}')