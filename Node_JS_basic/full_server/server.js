const express = require('express');
const controllerRouting = require('./routes/index');

// Create simple express server
const app = express();
const port = 1245;

controllerRouting(app);

app.listen(port, () => {
  console.log(`App listening at http://localhost:${port}`);
})

module.exports = app;
