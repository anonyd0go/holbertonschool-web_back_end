const readDatabase = require('../utils');

class StudentsController {
  // Gets all students organized by Majors
  static getAllStudents(req, res, db) {
    readDatabase(db).then((fields) => {
      const response = [];
      let msg;

      response.push('This is the list of our students');

      // Iterate ofer dictionary to create output
      for (const field of Object.keys(fields)) {
        msg = `Number of students in ${field}: ${fields[field].length}.
          List: ${fields[field].join(', ')}`;

        response.push(msg);
      }

      res.send(200, `${response.join('\n')}`);
    }).catch(() => {
      // Send error response if unable to load DB
      res.send(500, 'Cannot load the database');
    });
  }

  // Gets students by specified major
  static getAllStudentsByMajor(req, res, db) {
    // Verify major of request
    const { major } = req.params;
    if (major === 'CS' || major === 'SWE') {
      // Gets the list of students in the specified major
      readDatabase(db).then((fields) => {
        const stdntByMajor = fields[major];

        res.send(200, `List: ${stdntByMajor.join(', ')}`);
      }).catch(() => {
        res.send(500, 'Cannot load the database');
      });
    } else {
      res.send(500, 'Major parameter must be CS or SWE');
    }
  }
}

module.exports = StudentsController;
