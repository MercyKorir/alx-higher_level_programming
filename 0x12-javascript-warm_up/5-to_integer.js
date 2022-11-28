#!/usr/bin/node
const { argv } = require('node:process');
const len = argv.length;
let intArg;
if (len == 2) {
  console.log('Not a number');
}
argv.forEach((val, index) => {
  if (index === 2) {
    if (isNaN(val)) {
      console.log('Not a number');
    } else {
      intArg = Math.floor(Number(val));
      console.log(`My number: ${intArg}`);
    }
  }
});
