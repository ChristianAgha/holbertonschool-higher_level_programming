#!/usr/bin/node
// Prints number if integer
if (Number.parseFloat(process.argv[2]) == process.argv[2]) {
  console.log('My number: ' + parseInt(process.argv[2]));
} else {
  console.log('Not a number');
}
