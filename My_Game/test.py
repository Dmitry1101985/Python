import sun_class
import sky_class
import house_class
import pygame

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

house = house_class.House()
house_2 = house_class.House()
house_2.set_size(150, 100)
house_2.set_position(200, 200)
# house.set_size(300, 200)
# house.set_position(350,680)

while not done:
    
    clock.tick(60)   
    
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            done = True 
        
    # place code here
    screen.fill(sky.get_color_day(sun.get_degree()))
           
    sun.move(screen) 
    
    house.draw(screen)
    house_2.draw(screen)
    
    pygame.display.flip()
pygame.quit()