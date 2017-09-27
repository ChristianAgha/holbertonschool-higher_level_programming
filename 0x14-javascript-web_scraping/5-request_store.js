#!/usr/bin/node
// Gets the contents of a webpage and stores it in a file

const fs = require('fs');
const request = require('request');
const apiUrl = process.argv[2];
const fileName = process.argv[3];

request(apiUrl, function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    fs.writeFileSync(fileName, body, 'utf-8', function (err) {
      if (err) {
        console.log(err);
      }
    });
  }
});
