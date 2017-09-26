#!/usr/bin/node
// Defines Square class

const Rectangle = require('./4-rectangle').Rectangle;

function Square (size) {
  Rectangle.call(this, size, size);
}

module.exports.Square = Square;
