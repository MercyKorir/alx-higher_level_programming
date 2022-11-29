#!/usr/bin/node
const len = process.argv.length;
let largest;
let first = -1;
let second = -1;
if (len === 2 || len === 3) {
  largest = 0;
  console.log(`${largest}`);
} else {
  process.argv.forEach((val) => {
    if (Number(val) > first) {
      second = first;
      first = val;
    } else if (val > second && val !== first) {
      second = val;
    }
  });
  console.log(`${second}`);
}
