#!/usr/bin/node
const { argv } = require('node:process');
const len = argv.length;
let x;
if (len === 2) {
  console.log('Missing number of occurrences');
}
argv.forEach((val, index) => {
  if (index === 2) {
    if (isNaN(val)) {
      console.log('Not a number');
    } else {
      x = Math.floor(Number(val));
      for (let iter = 0; iter < x; iter++) {
        console.log('C is fun');
      }
    }
  }
});
