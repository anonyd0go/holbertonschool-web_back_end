const express = require('express')
const countStudents = require('./3-read_file_async');

const args = process.argv.slice(2);
const app = express();
const port = 1245;

app.get('/', (req, res) => {
  res.send('Hello Holberton School!');
});

app.get('/students', async (req, res) => {
  const response = ['This is the list of our students']
  try {
    response.push(...(await countStudents(args[0])));
    res.send(`${response.join('\n')}`);
  } catch (err) {
    res.send(err.message);
  }
});

// Start the server
app.listen(port, () => {
  console.log(`Express server running at http://localhost:${port}/`);
});

module.exports = app;
