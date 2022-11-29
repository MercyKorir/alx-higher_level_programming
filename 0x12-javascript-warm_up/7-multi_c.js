#!/usr/bin/node
const len = process.argv.length;
let x;
if (len === 2) {
  console.log('Missing number of occurrences');
}
process.argv.forEach((val, index) => {
  if (index === 2) {
    x = Math.floor(Number(val));
    for (let iter = 0; iter < x; iter++) {
      console.log('C is fun');
    }
  }
});
