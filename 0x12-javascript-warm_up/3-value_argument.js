#!/usr/bin/node
const { argv } = require('node:process');
let count = 0;
argv.forEach((val, index) => {
  count++;
});
if (count === 2) {
  console.log('No argument');
} else {
  argv.forEach((val, index) => {
    if (index === 2) {
      console.log(`${val}`);
    }
  });
}
