#!/usr/bin/node
// Prints the # of movies where "Wedge Antilles" is present

const apiUrl = process.argv[2];
const request = require('request');

request(apiUrl, function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    let count = 0;
    const jBody = JSON.parse(body);
    for (let i = 0; i < jBody.results.length; i++) {
      for (let j = 0; j < jBody.results[i].characters.length; j++) {
        let character = jBody.results[i].characters[j];
        if (character.match('18')) {
          count++;
        }
      }
    }
    console.log(count);
  }
});
