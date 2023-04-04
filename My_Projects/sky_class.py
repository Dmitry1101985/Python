class Sky:
    
    
    def __init__(self) -> None:
        self.day_color_R = 254
        self.day_color_G = 254
        self.day_color_B = 217
        
        
    def get_color_day(self, degree) -> tuple:
        if degree < 270:
            self.day_color_R = 74 + (degree - 180) / 0.5
            self.day_color_G = 74 + (degree - 180) / 0.5
        else:
            self.day_color_R = 254 - (degree - 270) / 0.5
            self.day_color_G = 254 - (degree - 270) / 0.5
        
        return self.day_color_R, self.day_color_G, self.day_color_B
    
    
    