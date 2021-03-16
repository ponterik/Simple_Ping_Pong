from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit, send
from game import Game
from threading import Timer
import json
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)
game = Game()
connected_players = 0
@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('input')
def handle_input(data):
    global game
    input_data = data['data']
    game.update_input(input_data['player_id'], input_data['keypressed'])

@socketio.on('client_connected')
def handle_client_connect_event(data):
    print("connected")
    #Timer(1, game_loop, args = [1]).start()
    global connected_players
    global game

    connected_players = connected_players + 1

    player_id = connected_players
    emit('assign_id', player_id)
    game.add_player(player_id)

    print(connected_players)
    if connected_players == game.player_limit:
        game.initialize_game()
        Timer(1, game_loop).start()


@socketio.on('disconnect')
def disconnected():
    print('disconnected')

def game_loop():
    global game
    game.game_step()
    state = game.game_state()
    socketio.emit('update', {'data': state}, broadcast=True)
    Timer(0.05, game_loop).start()
    

if __name__ == '__main__':
    socketio.run(app)
