const express = require('express');

const app = express(); // Initialize Express application
const port = 1245;

app.get('/', (req, res) => {
  res.send('Hello Holberton School!');
});

// Start the server
app.listen(port, () => {
  console.log(`Express server running at http://localhost:${port}/`);
});

module.exports = app;
