const fs = require('fs');

function readDatabase(filePath) {
  // Return a Promise
  return new Promise((resolve, reject) => {
    try {
      const data = fs.readFileSync(filePath, 'utf8'); // Read file
      // Split file into lines
      const lines = data.split('\n').filter((line) => line.trim() !== '');
      // Set up messages
      let message;

      // If only headers, exit
      if (lines.length <= 1) {
        message = 'DB Accessed. Number of students: 0';
        console.log(message);
        resolve({});
        return;
      }
      // Get csv headers, get student lines, create data containers
      const headers = lines[0].split(',');
      const studentLines = lines.slice(1);
      // Could use error handling of inexistant Keys
      const fieldIndex = headers.indexOf('field');
      const fnIndex = headers.indexOf('firstname');
      const fields = {};

      studentLines.forEach((row) => {
        // Split values in each row
        const values = row.split(',');
        // Add field if not exist and group student
        if (!fields[values[fieldIndex]]) {
          fields[values[fieldIndex]] = [];
        }
        fields[values[fieldIndex]].push(values[fnIndex].trim());
      });

      for (const field in fields) {
        if (field in fields) {
          message = `DB accessed for ${field}: ${fields[field].length}. List: ${fields[field].join(', ')}`;
          console.log(message);
        }
      }
      resolve(fields); // Resolve Promise as complete
    } catch (error) {
      reject(new Error('Cannot load the database'));
    }
  });
}

module.exports = readDatabase;
