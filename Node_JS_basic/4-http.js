// Bring http library
const http = require('http');

// Setup for host and port
const hostname = 'localhost';
const port = 1245;

// Create Server
const app = http.createServer((req, res) => {
  // Set the response HTTP header with HTTP status and Content type
  res.statusCode = 200;
  res.setHeader('Content-Type', 'text/plain');
  // Response message
  res.end('Hello Holberton School!');
});

app.listen(port, hostname);
