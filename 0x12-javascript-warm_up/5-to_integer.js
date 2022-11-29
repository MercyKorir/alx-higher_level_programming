#!/usr/bin/node
const len = process.argv.length;
let intArg;
if (len === 2) {
  console.log('Not a number');
}
process.argv.forEach((val, index) => {
  if (index === 2) {
    if (isNaN(val)) {
      console.log('Not a number');
    } else {
      intArg = Math.floor(Number(val));
      console.log(`My number: ${intArg}`);
    }
  }
});
