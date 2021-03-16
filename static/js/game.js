var socket=io('http://127.0.0.1:5000');
let client_id;

let type = "WebGL"
    if(!PIXI.utils.isWebGLSupported()){
      type = "canvas"
    }

socket.on('connect',function(){
    socket.emit('client_connected',{data:""});
    start_game()
});

socket.on('update',function(data){
    parsed = JSON.parse(data['data'])
    player1.x = parsed['players']['1']['x']
    player1.y = parsed['players']['1']['y']

    player2.x = parsed['players']['2']['x']
    player2.y = parsed['players']['2']['y']

    ball.x = parsed['ball']['x']
    ball.y = parsed['ball']['y']
});

socket.on('assign_id', function(data){
    client_id = data
    console.log(client_id)
});

function start_game() {
    initialize_inputs()
    app.ticker.add(delta => gameLoop(delta));
}

function gameLoop(delta){
    //To render updates
  }



let app = new PIXI.Application({ 
    width: 800,         // default: 800
    height: 600,        // default: 600
    antialias: true,    // default: false
    transparent: false, // default: false
    resolution: 1       // default: 1
  }
);
document.body.appendChild(app.view);

//Negative values to start them offscreen
let player1 = create_player(-100, -300)

let player2 = create_player(-700, -300)
let ball = create_ball(-400, -300)

create_middle_line(800, 600, 10)


function create_player(x, y) {
    let player = new PIXI.Graphics();
    player.beginFill(0xFFFFFF);
    player.drawRect(0, 0, 10, 100);
    player.endFill();
    player.x = x;
    player.y = y;
    app.stage.addChild(player);
    return player
}

function create_ball(x, y) {
    let ball = new PIXI.Graphics();
    ball.beginFill(0xFFFFFF);
    ball.drawCircle(0, 0, 10)
    ball.endFill();
    ball.x = x;
    ball.y = y;
    app.stage.addChild(ball);
    return ball
}
function create_middle_line(width, height, n) {
    for(i= 0; i < n+1; i++) {
        var circle = new PIXI.Graphics();
        circle.beginFill(0xFFFFFF);
        circle.drawCircle(0, 0, 5)
        circle.endFill();
        circle.x = width/2;
        circle.y = height*i/n;
        app.stage.addChild(circle);
    } 
}


function initialize_inputs(){
    let keypressed = null
    document.addEventListener('keydown', function(event) {

        if(event.keyCode == 38) {
            keypressed = "up"
        }
        else if(event.keyCode == 40) {
            keypressed = "down"
        } 
    });
    setInterval(function(){ send_input(); }, 10);
    function send_input() {
        if (keypressed) {
            let message = {
                'keypressed': keypressed,
                'player_id': client_id
            }
            socket.emit('input',{data: message});
            keypressed = null
        }
    }
}
