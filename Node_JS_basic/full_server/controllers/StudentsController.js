const readDatabase = require('../utils');

class StudentsController {
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
      res.send(500, 'Cannot load the database');
    });
  }

  static getAllStudentsByMajor(req, res, db) {
    const { major } = req.params;
    if (major === 'CS' || major === 'SWE'){
      readDatabase(db).then((fields) => {
        const stdntByMajor = fields[major];

        res.send(200, `List: ${stdntByMajor.join(', ')}`);
      }).catch(() => {
        res.send(500, `Cannot load the database`)
      })
    } else {
      res.send(500, 'Major parameter must be CS or SWE');
    }
  }
}

module.exports = StudentsController;
