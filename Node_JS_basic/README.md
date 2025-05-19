# NodeJS Basics — 19/05/2025

## Project File Structure

* `0-console.js` → Simple function logging a string to stdout
* `1-stdin.js` → Reads input from stdin and logs a formatted message
* `2-read_file.js` → Synchronous CSV reader using `fs.readFileSync`
* `3-read_file_async.js` → Asynchronous version returning a `Promise`
* `4-http.js` → HTTP server using Node's built-in `http` module
* `5-http.js` → HTTP server with dynamic `/students` route
* `6-http_express.js` → Basic Express server with root route
* `7-http_express.js` → Express server with dynamic `/students` route
* `full_server/` → Modular Express app with controllers and routing

---

## `database.csv`

Expected format:

```csv
firstname,lastname,age,field
Johann,Kerbrou,30,CS
Arielle,Salou,20,CS
...
```

Make sure to clean up trailing empty lines before testing.

---

## `full_server/` Breakdown

* `controllers/`

  * `AppController.js` → GET `/` returns a static welcome message
  * `StudentsController.js`

    * `getAllStudents()` → returns student count by field
    * `getAllStudentsByMajor()` → filters by `CS` or `SWE`
* `routes/`

  * `index.js` → Connects routes to controllers
* `utils.js` → `readDatabase(filePath)` reads and organizes student data
* `server.js` → Main Express app using router, runs on port 1245

---

## Common curl Tests

```bash
curl localhost:1245
curl localhost:1245/students
curl localhost:1245/students/CS
curl localhost:1245/students/SWE
curl localhost:1245/students/Math # triggers error
```

---

## Useful Commands

```bash
npm install
npm run dev         # runs full_server/server.js with nodemon + babel
npm run check-lint  # run ESLint
npm run test        # (not used here but good to remember)
```

---

## Notes / Reminders

* `process.argv[2]` is used to get the CSV file path
* All async controllers are wrapped in `try/catch` to avoid Express errors
* `res.type('text/plain')` is needed for consistent curl output
