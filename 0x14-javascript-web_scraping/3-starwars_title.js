#!/usr/bin/node
// Prints the title of a Star Wars movie

const ID = process.argv[2];
const request = require('request');
const url = 'http://swapi.co/api/films/' + ID;

request(url, function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    console.log(JSON.parse(body).title);
  }
});
