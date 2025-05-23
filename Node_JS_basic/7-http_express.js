const express = require('express')
const countStudents = require('./3-read_file_async');

// Set up server
const args = process.argv.slice(2);
const app = express();
const port = 1245;

// Home route
app.get('/', (req, res) => {
  res.send('Hello Holberton School!');
});

// Get students from database
app.get('/students', async (req, res) => {
  const msg = 'This is the list of our students\n';
  try {
    const response = await countStudents(args[0]);
    res.send(`${msg}${response.join('\n')}`);
  } catch (err) {
    res.send(`${msg}${err.message}`);
  }
});

// Start the server
app.listen(port, () => {
  console.log(`Express server running at http://localhost:${port}/`);
});

module.exports = app;
