from player import Player
from ball import Ball
import json

class Game():
    players = {}
    player_limit = 2
    x_max = 800
    y_max = 600
    ball = Ball(x_max/2, y_max/2)
    is_running = False
    def __init__(self):
        pass

    def add_player(self, player_id):
        self.players[player_id] = Player(player_id, self.x_max, self.y_max)

    def initialize_game(self):
        self.is_running = True

    def game_step(self):
        for _, player in self.players.items():
            player.update_position(self.x_max, self.y_max)
            self.check_colission(player)
        self.ball.update_position(self.x_max, self.y_max)
    
    def game_state(self):
        state = {}
        state['players'] = {}
        state['ball'] = {'x': self.ball.x, 'y': self.ball.y}
        for player_id, player in self.players.items():
            state['players'][player_id] = player.as_dict()
        return json.dumps(state)
    
    def check_colission(self, player):
        if not player.is_left_side:
            if self.ball.x + self.ball.r > self.x_max - player.width:
                if player.y + player.height > self.ball.y > player.y:
                    self.ball.dx = -self.ball.dx
                else:
                    self.ball.x = self.x_max/2
                    self.ball.y = self.y_max/2
        
        if player.is_left_side:
            if self.ball.x - self.ball.r < 0 + player.width:
                if player.y + player.height > self.ball.y > player.y:
                    self.ball.dx = -self.ball.dx
                else:
                    self.ball.x = self.x_max/2
                    self.ball.y = self.y_max/2

    def update_input(self, player_id, key):
        self.players[player_id].set_latest_input(key)
