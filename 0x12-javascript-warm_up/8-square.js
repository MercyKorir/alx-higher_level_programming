#!/usr/bin/node
const { argv } = require('node:process');
const len = argv.length;
let x;
if (len === 2) {
  console.log('Missing size');
}
argv.forEach((val, index) => {
  if (index === 2) {
    if (isNaN(val)) {
      console.log('Missing size');
    } else {
      x = Math.floor(Number(val));
      for (let height = 0; height < x; height++) {
        let row = '';
        for (let width = 0; width < x; width++) {
          row += 'x';
        }
        console.log(row + ' ');
      }
    }
  }
});
