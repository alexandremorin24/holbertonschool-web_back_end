import readDatabase from '../utils';

class StudentsController {
  static async getAllStudents(req, res) {
    const path = process.argv[2];
    try {
      const data = await readDatabase(path);
      let response = 'This is the list of our students';

      const fields = Object.keys(data).sort();
      for (const field of fields) {
        const names = data[field];
        response += `\nNumber of students in ${field}: ${names.length}. List: ${names.join(', ')}`;
      }

      res.status(200).send(response);
    } catch (err) {
      res.status(500).send('Cannot load the database');
    }
  }

  static async getAllStudentsByMajor(req, res) {
    const { major } = req.params;
    if (major !== 'CS' && major !== 'SWE') {
      res.status(500).send('Major parameter must be CS or SWE');
      return;
    }

    const path = process.argv[2];
    try {
      const data = await readDatabase(path);
      const names = data[major];
      res.status(200).send(`List: ${names.join(', ')}`);
    } catch (err) {
      res.status(500).send('Cannot load the database');
    }
  }
}

export default StudentsController;
