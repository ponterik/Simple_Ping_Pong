class Player:
    x = 0
    y = 0
    latest_input = None
    movement_speed = 10
    width = 10
    height = 100
    is_left_side = None
    def __init__(self, id):
        self.id = id

    def update_position(self, x_max, y_max):
        if self.latest_input:
            if self.latest_input == "up":
                self.y = self.y - self.movement_speed
                if  self.y < 0:
                    self.y = 0
            if self.latest_input == "down":
                self.y = self.y + self.movement_speed
                if (self.y + self.height) > y_max:
                    self.y = y_max - self.height
            self.latest_input = None

    def set_latest_input(self, key):
        self.latest_input = key
        
    def as_dict(self):
        return {'x': self.x, 'y': self.y}
    
    def set_position(self, x, y, is_left_side):
        self.x = x
        self.y = y
        self.is_left_side = is_left_side