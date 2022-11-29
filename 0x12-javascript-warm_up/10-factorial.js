#!/usr/bin/node
function factorial (a) {
  const len = process.argv.length;
  if (len < 3 || Number(a) === 0) {
    return (1);
  } else {
    return (Number(a) * factorial(a - 1));
  }
}
console.log(factorial(process.argv[2]));
