#!/usr/bin/node
// Defines Square class

const Square = require('./5-square').Square;

Square.prototype.charPrint = function (char) {
  if (char === undefined) {
    char = 'X';
  }
  for (let i = 0; i < this.height; i++) {
    console.log(char.repeat(this.width));
  }
};

module.exports.Square = Square;
