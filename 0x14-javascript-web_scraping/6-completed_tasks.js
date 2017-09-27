#!/usr/bin/node
// Computes the number of tasks completed by user id

const request = require('request');
const apiUrl = process.argv[2];
let done = {};

request(apiUrl, function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    const jBody = JSON.parse(body);
    for (let i = 0; i < jBody.length; i++) {
      done[jBody[i].userId] = 0;
    }
    for (let j = 0; j < jBody.length; j++) {
      if (jBody[j].completed === true) {
        done[jBody[j].userId] += 1;
      }
    }
  }
  console.log(done);
});
