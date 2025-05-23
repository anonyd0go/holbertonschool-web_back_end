const http = require('http');
const countStudents = require('./3-read_file_async');
const args = process.argv.slice(2);

const hostname = '127.0.0.1';
const port = 1245;

const app = http.createServer(async (req, res) => {
  // Seet response and content type
  res.statusCode = 200;
  res.setHeader('Content-Type', 'text/plain');

  // Set up url endpoints and responses
  if (req.url === '/') {
    res.end('Hello Holberton School!');
  } else if (req.url === '/students') {
    res.write('This is the list of our students\n');
    try {
      const response = await countStudents('database.csv');
      res.end(`${response.join('\n')}`);
    } catch (err) {
      res.end(err.message);
    }
  } else {
    res,statusCode = 404;
    res.end();
  }
});

// Set app to listen
app.listen(port, hostname, () => {
  console.log(`Server running at ${hostname}:${port}`);
})

module.exports = app;
