process.stdout.write('Welcome to Holberton School, what is your name?\n');

process.stdin.setEncoding('utf8');

process.stdin.on('data', (input) => {
  const name = input.trim();
  process.stdout.write(`Your name is: ${name}\n`);
  process.stdin.end();
});

process.on('exit', () => {
  console.log('This important software is now closing');
});
