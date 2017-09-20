#!/usr/bin/node
// Prints factorial of input
function factorial (num) {
  if (num < 0) {
    return -1;
  } else if (num === 0 || isNaN(num) || num === undefined) {
    return 1;
  } else {
    return (num * factorial(num - 1));
  }
}
let result = factorial(process.argv[2]);
console.log(result);
