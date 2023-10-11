const net = require('net');

const server = net.createServer((socket) => {
    socket.on('data', (data) => {
        let result = data.toString().replaceAll('\n','');
        socket.write(`Dostałem: ${result}\n`);
    });
});

// netcad
server.on('connection', (socket) => {
    socket.write('Witaj!\n');
});

server.listen(3000, () => {
    console.log('Serwer nasłuchuje na porcie 3000!');
});