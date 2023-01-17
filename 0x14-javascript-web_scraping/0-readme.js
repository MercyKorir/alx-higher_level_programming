#!/usr/bin/node
const file = process.argv[2];
const fs = require('fs');
const path = require('path');
fs.readFile(path.resolve(file), 'utf8', (err, data) => {
  if (err) {
    console.error(err);
  } else {
    console.log(data);
  }
});
