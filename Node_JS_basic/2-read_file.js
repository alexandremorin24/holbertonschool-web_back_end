const fs = require('fs');

function countStudents(path) {
  try {
    // Read file content synchronously
    const data = fs.readFileSync(path, 'utf8');

    // Split content by line and remove empty ones
    const lines = data.split('\n').filter((line) => line.trim() !== '');

    // Remove header
    const students = lines.slice(1);

    const fields = {};
    for (const student of students) {
      const [firstname, , , field] = student.split(',');
      if (!fields[field]) {
        fields[field] = [];
      }
      fields[field].push(firstname);
    }

    console.log(`Number of students: ${students.length}`);

    for (const [field, names] of Object.entries(fields)) {
      console.log(`Number of students in ${field}: ${names.length}. List: ${names.join(', ')}`);
    }
  } catch (err) {
    throw new Error('Cannot load the database');
  }
}

module.exports = countStudents;
