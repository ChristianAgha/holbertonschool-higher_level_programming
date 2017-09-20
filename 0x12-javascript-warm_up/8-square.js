#!/usr/bin/node
// Prints a square
let x = '';
if (parseFloat(process.argv[2])) {
  for (let n = 0; n < parseInt(process.argv[2]); n++) {
    x += 'X';
  }
  for (let n = 0; n < parseInt(process.argv[2]); n++) {
    console.log(x);
  }
} else {
  console.log('Missing size');
}
