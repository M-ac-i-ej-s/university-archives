const io = require("socket.io")(8900, {
    cors: {
      origin: "*",
    },
});

let PlayerOneLabirynth = [
    [9,9,9,9,9,9,9,9,9,9,9,9],
    [9,0,0,0,0,0,'O',0,0,0,0,9],
    [9,0,0,1,1,1,1,0,0,0,0,9],
    [9,0,0,1,0,0,0,0,0,0,0,9],
    [9,0,0,1,1,0,0,0,1,1,1,9],
    [9,0,0,0,1,0,0,0,1,0,1,9],
    [9,0,0,0,1,1,1,1,1,0,1,9],
    [9,0,0,0,0,0,0,0,0,0,1,9],
    [9,0,0,0,0,0,0,0,0,0,1,9],
    [9,0,0,1,1,1,1,1,1,1,1,9],
    [9,0,0,0,0,0,0,0,0,0,0,9],
    [9,9,9,9,9,9,9,9,9,9,9,9]
];

let PlayerTwoLabirynth = [
    [9,9,9,9,9,9,9,9,9,9,9,9],
    [9,0,0,0,0,0,1,0,0,0,0,9],
    [9,0,0,1,1,1,1,0,0,0,0,9],
    [9,0,0,1,0,0,0,0,0,0,0,9],
    [9,0,0,1,1,0,0,0,1,1,1,9],
    [9,0,0,0,1,0,0,0,1,0,1,9],
    [9,0,0,0,1,1,1,1,1,0,1,9],
    [9,0,0,0,0,0,0,0,0,0,1,9],
    [9,0,0,0,0,0,0,0,0,0,1,9],
    [9,0,0,'O',1,1,1,1,1,1,1,9],
    [9,0,0,0,0,0,0,0,0,0,0,9],
    [9,9,9,9,9,9,9,9,9,9,9,9]
];

const players = []

let startPoint1 = {
    x: 1,
    y: 6
};
let startPoint2 = {
    x: 9,
    y: 3
};
let endPoint1 = {
    x: 9,
    y: 3
};

let endPoint2 = {
    x: 1,
    y: 6
};

io.on("connection", (socket) => {
    socket.on("addUser", () => {
        players.push('player');
        console.log(players)
        if(players.length === 2) {
            io.emit("startGame", {startPoint2,startPoint1, PlayerTwoLabirynth});   
        } else {
            io.emit("waiting", {startPoint1,startPoint2, PlayerOneLabirynth});
        }
    });

    socket.on("PlayerOneMove", (PlayerOneMove) => {
        let mess = 'not ok'


        switch(PlayerOneMove) {
            case 'up':
                if(PlayerOneLabirynth[startPoint2.y - 1][startPoint2.x] === 1) {
                    startPoint2.y -= 1;
                    mess = 'ok';
                }
            case 'down':
                if(PlayerOneLabirynth[startPoint2.y + 1][startPoint2.x] === 1) {
                    startPoint2.y += 1;
                    mess = 'ok';
                }
            case 'left':
                if(PlayerOneLabirynth[startPoint2.y][startPoint2.x - 1] === 1) {
                    startPoint2.x -= 1;
                    mess = 'ok';
                }
            case 'right':
                if(PlayerOneLabirynth[startPoint2.y][startPoint2.x + 1] === 1) {
                    startPoint2.x += 1;
                    mess = 'ok';
                }            
        }

        if(startPoint2.x === endPoint1.x && startPoint2.y === endPoint1.y) {
            mess = 'win';
        }

        io.emit("PlayerOneMove", {mess, startPoint2});
    });

    socket.on("PlayerTwoMove", (PlayerOneMove) => {
        let mess = 'not ok'
        console.log('ss')
        switch(PlayerOneMove) {
            case 'up':
                if(PlayerOneLabirynth[startPoint2.y - 1][startPoint2.x] === 1) {
                    startPoint2.y -= 1;
                    mess = 'ok';
                }
            case 'down':
                if(PlayerOneLabirynth[startPoint2.y + 1][startPoint2.x] === 1) {
                    startPoint2.y += 1;
                    mess = 'ok';
                }
            case 'left':
                if(PlayerOneLabirynth[startPoint2.y][startPoint2.x - 1] === 1) {
                    startPoint2.x -= 1;
                    mess = 'ok';
                }
            case 'right':
                if(PlayerOneLabirynth[startPoint2.y][startPoint2.x + 1] === 1) {
                    startPoint2.x += 1;
                    mess = 'ok';
                }            
        }

        if(startPoint2.x === endPoint2.x && startPoint2.y === endPoint2.y) {
            mess = 'win';
        }

        io.emit("PlayerOneMove", {mess, startPoint2});
    });

    socket.on("disconnect", () => {
        players.pop();
        console.log("a user disconnected");
    });
});