#!/usr/bin/node
// Searches the second biggest integer in a list
if (process.argv.length <= 3) {
  console.log('0');
} else if (process.argv.length >= 4) {
  let arr = [];
  for (let i = 2; i < process.argv.length; i++) {
    arr = arr.concat(process.argv[i]);
  }
  arr = arr.sort(function (a, b) { return a - b; });
  console.log(arr[arr.length - 2]);
}
