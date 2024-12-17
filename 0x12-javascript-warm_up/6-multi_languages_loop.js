#!/usr/bin/node
// prints 3 lines

const lines = ['C is fun', 'Python is cool', 'JavaScript is amazing'];

let i = 0;

while (process.argv.length > 2 && i < lines.length) {
  console.log(lines[i]);
  i++;
}
