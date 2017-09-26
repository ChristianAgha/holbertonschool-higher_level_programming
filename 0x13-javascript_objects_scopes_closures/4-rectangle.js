#!/usr/bin/node
// Defines a rectangle class
exports.Rectangle = function Rectangle (w, h) {
  if (w > 0 && h > 0) {
    this.width = w;
    this.height = h;
  }

  this.print = function () {
    for (let i = 0; i < this.height; i++) {
      console.log('X'.repeat(this.width));
    }
  };

  this.rotate = function () {
    const temp = this.width;
    this.width = this.height;
    this.height = temp;
  };

  this.double = function () {
    this.width = this.width * 2;
    this.height = this.height * 2;
  };
};
