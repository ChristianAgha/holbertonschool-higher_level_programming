#!/usr/bin/node
// Prints the addition of 2 integers
function add (a, b) {
  let num1 = parseFloat(a);
  let num2 = parseFloat(b);
  console.log(num1 + num2);
}
add(process.argv[2], process.argv[3]);
