#!/usr/bin/node
const Square1 = require('./5-square');
module.exports = class Square extends Square1 {
  charPrint (c) {
    let char = c;
    if (c === undefined) {
      char = 'X';
    }
    let row = '';
    for (let i = 0; i < this.width; i++) {
      row += char;
    }
    for (let j = 0; j < this.height; j++) {
      console.log(row);
    }
  }
};
