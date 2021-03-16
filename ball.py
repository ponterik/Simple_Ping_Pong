class Ball():
    x = 0
    y = 0
    dx = 10
    dy = 2
    r  = 5
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def update_position(self, x_max, y_max):
        self.x = self.x + self.dx
        self.y = self.y + self.dy
        

        self.y = self.y + self.dy
        if self.y + self.r > y_max or self.y - self.r < 0:
            self.dy = -self.dy
    