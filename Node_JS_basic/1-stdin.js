process.stdout.write('Welcome to Holberton School, what is your name?\n');

process.stdin.setEncoding('utf8');

process.stdin.on('readable', () => {
  const chunk = process.stdin.read();
  if (chunk !== null) {
    displayMessage(`Your name is : ${chunk}`);
  }
});

process.on('close', () => {
  process.stdout.write('This important software is now closing\n');
});
