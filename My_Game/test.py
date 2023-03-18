import sun_class
import sky_class
import pygame

# Trying to understand this git
pygame.init()

size = [1000, 700]
screen = pygame.display.set_mode(size)

pygame.display.set_caption('House building')

done = False
clock = pygame.time.Clock()

sun = sun_class.Sun()
sun.set_start_position(200)
sun.set_display(size)

sky = sky_class.Sky()

while not done:
    
    clock.tick(60)   
    
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            done = True 
        
    # place code here
    screen.fill(sky.get_color_day(sun.get_degree()))
           
    sun.move(screen) 
    
    pygame.display.flip()
pygame.quit()