const express = require('express');
var {NodeAdapter} = require("ef-keycloak-connect");
const app = express();
const config = require(`./config.json`);
const session = require('express-session');
const memoryStore = new session.MemoryStore();
const keycloak = new NodeAdapter(config)

app.use(session({
    secret: 'secret1',
    resave: false,
    saveUninitialized: true,
    store: memoryStore
}));

process.env.NODE_TLS_REJECT_UNAUTHORIZED = 0    // to disable https

app.use( keycloak.middleware({ logout: '/logout' }))

app.get('/', (req, res) => {
    console.log('Hello world');
    res.send('Hello world');
});

app.get('/home', keycloak.protect(), (req, res) => {
    res.send('Welcome to Home');
});

app.listen(3000, () => {
  console.log(`Example app listening on port 3000`)
})