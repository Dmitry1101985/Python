import pygame
import math
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

def draw_basis(x: float, y: float, width: int, height: int) -> None:
    """Drawing basis for house
    in function draw_house()

    Args:
        x (float): main point x coordinate. 
        y (float): main point y coordinate.
        width (int): total house width.
        height (int): total house height.
    """
    basics_height = height * 0.1 #calculate basis height from total house height.
    
    #drawing basis - rectangle
    pygame.draw.rect(screen, "black", [x, y, width, basics_height], 3)
    

def draw_walls(x: float, y: float, width: int, height: int) -> None:
    """Drawing walls for house in
    function draw_house()

    Args:
        x (float): main point x coordinate.
        y (float): main point y coordinate.
        width (int): total house width.
        height (int): total house height.
    """
    walls_width = width * 0.9 #calculate wall width
    walls_height = height * 0.6 #calculate wall height
    walls_y = y - walls_height #calculate y position to paste walls
    walls_x = x + (width - walls_width) / 2 #calculate x position to paste walls
    #drawing walls - rectangle
    pygame.draw.rect(screen, "black", [walls_x, walls_y, walls_width, walls_height], 3)
    

def draw_roof(x: float, y: float, width: int, height: int) -> None:
    """Drawing roof for house in
    function draw_house()

    Args:
        x (float): main point x coordinate.
        y (float): main point y coordinate.
        width (int): total house width.
        height (int): total house height.
    """
    left_point_x = x #calculate x position of lower left point of poligon
    left_point_y = y - 0.6 * height #calculate y position of lower left point of poligon
    right_point_x = x + width #calculate x position of lower right point of poligon
    right_point_y = y - 0.6 * height #calculate y position of lower right point of poligon
    central_poin_x = x + width / 2 #calculate x position of upper central point of poligon
    central_poin_y = y - height * 0.9 #calculate y position of upper central point of poligon
    #drawing roof - poligon by three points
    pygame.draw.polygon(
        screen, 
        "black", 
        [[central_poin_x, central_poin_y], [left_point_x, left_point_y], [right_point_x, right_point_y]],
        3,
        )
    

def draw_window(x: float, y: float, width: int, height: int) -> None:
    """Drawing two simmetric windows for house in
    function draw_house()

    Args:
        x (float): main point x coordinate.
        y (float): main point y coordinate.
        width (int): total house width.
        height (int): total house height.
    """
    windows_width = width * 0.15 #calculate width for both windows
    windows_height = height * 0.25 #calculate height for both windows
    window_1_x = x + width * 0.15 #calculate x position for paste point for first window
    window_2_x = x + (width - width * 0.15) - windows_width #calculate x position for paste point for second window
    windows_y = y - windows_height - (height * 0.15) #calculate y position for paste point for both windows
    #drawing first window  - rectangle
    pygame.draw.rect(screen, "black", [window_1_x, windows_y, windows_width, windows_height], 3)
    #drawing second window  - rectangle
    pygame.draw.rect(screen, "black", [window_2_x, windows_y, windows_width, windows_height], 3)
    pass


def draw_door(x: float, y: float, width: int, height: int) -> None:
    """Drawing door for house in
    function draw_house()

    Args:
        x (float): main point x coordinate.
        y (float):  main point y coordinate.
        width (int): total house width.
        height (int): total house height.
    """
    door_height = height * 0.4 #calculate door height
    door_width = width * 0.2 #calculate door width
    door_x = x + (width / 2) - (door_width / 2) #calculate x position to paste door
    door_y = y - door_height #calculate y position to paste door
    #drawing door - rectangle
    pygame.draw.rect(screen, "black", [door_x, door_y, door_width, door_height], 3)
    

def draw_house(x=250, y=300, height=200, width=300) -> None:
    """Function drawing house with main point with coordinates (x,y)

    Args:
        x (int, optional): main point x coordinate. Defaults to 250.
        y (int, optional): main point y coordinate. Defaults to 300.
        height (int, optional): total house height. Defaults to 200.
        width (int, optional): total house width. Defaults to 300.
    """
    y = y - height * 0.1 #slide y to center
    x = x - width / 2 #slide x to center
    
    draw_basis(x, y, width, height) 
    draw_walls(x, y, width, height)
    draw_roof(x, y, width, height)
    draw_window(x, y, width, height)
    draw_door(x, y, width, height)


def spin_house(x=250, y=300, height=200, changes=350, start_pos_changes=350, flag=True) -> tuple:
    """Spinning house. Uses draw_house function 
    and global variables changes and start_pos_changes.
    House spinning by opyical illusion (changing house width)

    Args:
        x (int, optional): x coordinate to paste house. Defaults to 250.
        y (int, optional): y coordinate to paste house. Defaults to 300.
        height (int, optional): house height. Defaults to 200.
        changes (int, optional): current value of house width. Defaults to 350.
        start_pos_changes (int, optional): start value of house width. Defaults to 350.
        flag (bool, optional): need to reduce house width or to increase. Defaults to True.

    Returns:
        tuple: changes and flag
    """
    
    if flag :  # if need to reduse width 
        if changes > 10: # and if its not last value
            changes -= 10 #reducing house width
    else: # else if need to increase
        if changes < start_pos_changes: # and widht value isnt over
            changes += 10 #increasing house width
    
    #changing flag
    if changes == start_pos_changes and not flag:
        flag = not flag
    elif changes == 10 and flag:
         flag = not flag
    
    draw_house(x, y, height, changes)
      
    return changes, flag


def draw_sun(x=60, y=100, radius=40) -> None:
    """Drawing yellow sun

    Args:
        x (int, optional): central x coordinate of circle (sun). Defaults to 60.
        y (int, optional): central y coordinate of circle (sun). Defaults to 100.
        radius (int, optional): radius of circle (sun). Defaults to 40.
    """
    pygame.draw.circle(screen, "yellow", [x, y], radius)       


def moving_sun(start_fi=235, fi =235, fi_step=0.2, start_blue_in_sky=155, blue_in_sky=155) -> tuple:
    """Moving sun by arc, using function draw_sun() and changing sky colore to paint the sky 

    Args:
        start_fi (int, optional): start sun position degree. Defaults to 235.
        fi (int, optional): current sun position degree. Need to change position. Defaults to 235.
        fi_step (float, optional): step degree. Defaults to 0.2.
        start_blue_in_sky (int, optional): starting blue value of sky in RGB. Defaults to 155.
        blue_in_sky (int, optional): current blue value of sky in RGB. changeble.  Defaults to 155.

    Returns:
        tuple: current sun position fi and current blue value of sky in RGB
    """
    x_0 = 400 #center
    y_0 = 600 #last line
    R = 500 #Radius of circle of sun traectory
    end_fi = (270 - start_fi) + 270 #calculate last sun position. Need for simmetric
    steps_to_center = (270 - start_fi) / fi_step #calculate how many steps from start to middle
    blue_step = (255 - start_blue_in_sky) / steps_to_center #calculate changing value of blue in RGB by one step
    #if not end - increse fi
    if fi < end_fi:
        fi += fi_step
    #if sun in first half make sky more blue    
    if fi < 270 and blue_in_sky < 255:
        blue_in_sky += blue_step
    elif fi > 270 and fi < end_fi: #if sun goes down make sky less blue
        blue_in_sky -= blue_step
    
    x_current = x_0 + R * math.cos(math.radians(fi)) #calculate current x-coordinate of sun position
    y_current = y_0 + R * math.sin(math.radians(fi)) #calculate current y-coordinate of sun position
    
    draw_sun(x_current, y_current) #drawing sun by current coordinates
    
    return fi, blue_in_sky



while not done:
    
    clock.tick(60)   
    
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
 
            done = True 
            
    # place code here
    screen.fill((228, 172, blue_in_sky))
    changes, flag = spin_house(400, 550, 300, changes, start_pos_changes, flag)
    fi, blue_in_sky = moving_sun(start_fi, fi, 0.2, start_blue_in_sky, blue_in_sky)
      
    pygame.display.flip()
pygame.quit()            
            