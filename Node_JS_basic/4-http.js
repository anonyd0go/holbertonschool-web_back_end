// Bring http library
const http = require('http');

// Setup for host and port
const hostname = '127.0.0.1';
const port = 1245;

// Create Server
const app = http.createServer((req, res) => {
  // Set the response HTTP header with HTTP status and Content type
  res.statusCode = 200;
  res.setHeader('Content-Type', 'text/plain');
  // Response message
  res.end('Hello Holberton School!');
});

// Open port to listen to
app.listen(port, hostname);

module.exports = app;
