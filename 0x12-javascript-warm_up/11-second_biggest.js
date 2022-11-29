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
      first = Number(val);
    } else if (Number(val) > second && Number(val) !== first) {
      second = Number(val);
    }
  });
  console.log(`${second}`);
}
