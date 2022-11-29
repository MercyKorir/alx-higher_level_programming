#!/usr/bin/node
const len = process.argv.length;
let x;
if (len === 2) {
  console.log('Missing size');
}
process.argv.forEach((val, index) => {
  if (index === 2) {
    if (isNaN(val)) {
      console.log('Missing size');
    } else {
      x = Math.floor(Number(val));
      for (let height = 0; height < x; height++) {
        let row = '';
        for (let width = 0; width < x; width++) {
          row += 'X';
        }
        console.log(row);
      }
    }
  }
});
