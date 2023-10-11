const http = require('http');

const server = http.createServer((_req, res) => {
    res.writeHead(200, {'Content-Type': 'text/plain; charset=utf8'});
    res.write('Witaj świecie!');
    setTimeout(() => {
        res.end('To już koniec odpowiedzi!\n');
    }, 5000)
});

// netcad

server.listen(3000, () => {
    console.log('Serwer nasłuchuje na porcie 3000!');
});