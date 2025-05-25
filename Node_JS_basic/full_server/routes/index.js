const express = require('express');
const AppController = require('../controllers/AppController');
const StudentsController = require('../controllers/StudentsController');

// Controller for routing endpoints
function controllerRouting(app) {
  // Get database
  const db = process.argv[2];
  // Set up router
  const router = express.Router();
  app.use('/', router);

  // Home page return
  router.get('/', (req, res) => {
    AppController.getHomepage(req, res);
  });

  // Students endpoint for a response with all students by field
  router.get('/students', (req, res) => {
    StudentsController.getAllStudents(req, res, db);
  });

  // Students by major endpoint.  List of students in specified major
  router.get('/students/:major', (req, res) => {
    StudentsController.getAllStudentsByMajor(req, res, db);
  });
}

module.exports = controllerRouting;
