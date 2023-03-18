import pygame
import house
import sun

# Trying to understand this git
pygame.init()

size = [800, 600]
screen = pygame.display.set_mode(size)

pygame.display.set_caption('House building')

done = False
clock = pygame.time.Clock()
start_pos_changes = 350
changes = start_pos_changes
flag = True
fi = 208
start_fi = fi
blue_in_sky = 100
start_blue_in_sky = blue_in_sky


while not done:
    
    clock.tick(60)   
    
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
 
            done = True 
            
    # place code here
    screen.fill((228, 172, blue_in_sky))
    changes, flag = house.spin_house(400, 550, 300, changes, start_pos_changes, flag)
    fi, blue_in_sky = sun.moving_sun(start_fi, fi, 0.2, start_blue_in_sky, blue_in_sky)
      
    pygame.display.flip()
pygame.quit()            
            