import pygame
import math

size = [800, 600]
screen = pygame.display.set_mode(size)



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

