#!/usr/bin/node
function add (a, b) {
  const len = process.argv.length;
  if (len <= 3) {
    return ('NaN');
  } else {
    return (Number(a) + Number(b));
  }
}
console.log(add(process.argv[2], process.argv[3]));
