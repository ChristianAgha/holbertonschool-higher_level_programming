#!/usr/bin/node
// Prints the # of movies where "Wedge Antilles" is present

const apiUrl = process.argv[2];
const request = require('request');
let count = 0;

request(apiUrl, function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    const jBody = JSON.parse(body);
    for (let i = 0; i < jBody.results.length; i++) {
      for (let j = 0; j < jBody.results[i].characters.length; j++) {
        let character = jBody.results[i].characters[j];
        let wedgeAntilles = 'https://swapi.co/api/people/18/';
        if (character === wedgeAntilles) {
          count++;
        }
      }
    }
  }
  console.log(count);
});
