import pygame

class House:
    
    def __init__(self) -> None:
        self.x = 400
        self.y = 580
        self.height = 250
        self.width = 300
        self.line_thickness = 3
        

    def set_size(self, width, height):
        self.width = width
        self.height = height
    
    
    def set_position(self, x, y):
        self.x = x
        self.y = y
    
    
    def set_line_thickness(self, thickness):
        self.line_thickness = thickness
    
    
    def draw(self, screen):
        self.draw_foundation(screen)
        self.draw_floor(screen)
        self.draw_roof(screen)
    
    
    def draw_foundation(self, screen):
        foundation_height = self.height * 0.1
        pygame.draw.rect(screen, "black", [self.x, self.y, self.width, foundation_height], self.line_thickness)
    
    
    def draw_floor(self, screen):
        self.draw_walls(screen)
        self.draw_door(screen)
        self.draw_left_window(screen)
        self.draw_right_window(screen)
    
    
    def draw_roof(self, screen):
        roof_lp_x = self.x
        roof_lp_y = self.y - 0.6 * self.height + self.line_thickness
        roof_rp_x = self.x + self.width
        roof_rp_y = roof_lp_y
        roof_cp_x = self.x + self.width / 2
        roof_cp_y = self.y - self.height * 0.9
        pygame.draw.polygon(
        screen, 
        "black", 
        [[roof_cp_x, roof_cp_y], [roof_lp_x, roof_lp_y], [roof_rp_x, roof_rp_y]],
        self.line_thickness,
        )
    
    
    def draw_walls(self, screen):
        walls_width = self.width * 0.9
        walls_height = self.height * 0.6
        walls_x = self.x + (self.width - walls_width) / 2
        walls_y = self.y - walls_height + self.line_thickness
        pygame.draw.rect(screen, "black", [walls_x, walls_y, walls_width, walls_height], self.line_thickness)
    
    
    def draw_door(self, screen):
        door_height = self.height * 0.4
        door_width = self.width * 0.2
        door_x = self.x + (self.width / 2) - (door_width / 2)
        door_y = self.y - door_height + self.line_thickness
        pygame.draw.rect(screen, "black", [door_x, door_y, door_width, door_height], self.line_thickness)
    
    
    def draw_left_window(self, screen):
        window_width = self.width * 0.15
        window_height = self.height * 0.25
        window_y = self.y - window_height - (self.height * 0.15)
        window_left_x = self.x + self.width * 0.15
        pygame.draw.rect(screen, "black", [window_left_x, window_y, window_width, window_height], self.line_thickness)
    
    
    def draw_right_window(self, screen):
        window_width = self.width * 0.15
        window_height = self.height * 0.25
        window_y = self.y - window_height - (self.height * 0.15)
        window_right_x = self.x + (self.width - self.width * 0.15) - window_width
        pygame.draw.rect(screen, "black", [window_right_x, window_y, window_width, window_height], self.line_thickness)