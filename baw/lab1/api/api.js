const express = require('express');
const basicAuth = require('express-basic-auth')
const app = express();

app.use(basicAuth({
    users: { 'admin': 'supersecret' },
    challenge: true
}))

app.get('/hello', (req, res) => {
  res.send('Hello, World!');
});

app.listen(3001, () => {
  console.log('Server started on port 3001');
});