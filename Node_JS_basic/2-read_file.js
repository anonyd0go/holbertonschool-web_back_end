const fs = require('fs');

function countStudents(filePath) {
  try {
    const data = fs.readFileSync(filePath, 'utf8'); // Read file
    // Split file into lines
    const lines = data.split('\n').filter((line) => line.trim() !== '');

    // If only headers, exit
    if (lines.length <= 1) {
      console.log('Number of students: 0');
      return;
    }
    // Get csv headers, get student lines, create data containers
    const headers = lines[0].split(',');
    const studentLines = lines.slice(1);
    const fieldIndex = headers.indexOf('field');
    const fnIndex = headers.indexOf('firstname');
    const students = [];
    const fields = {};

    studentLines.forEach((row) => {
      // Split values in each row
      const values = row.split(',');
      // Add student to student list
      students.push(values[fnIndex].trim());

      // Add field if not exist and group student
      if (!fields[values[fieldIndex]]) {
        fields[values[fieldIndex]] = [];
      }
      fields[values[fieldIndex]].push(values[fnIndex].trim());
    });

    // List number of students
    console.log(`Number of students: ${students.length}`);

    for (const field in fields) {
      if (field in fields) {
        console.log(
          `Number of students in ${field}: ${fields[field].length}. List: ${fields[field].join(', ')}`,
        );
      }
    }
  } catch (error) {
    throw new Error('Cannot load the database');
  }
}

module.exports = countStudents;
