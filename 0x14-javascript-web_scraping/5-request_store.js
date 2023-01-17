#!/usr/bin/node
const url = process.argv[2];
const file = process.argv[3];
const fs = require('fs');
const request = require('request');
const path = require('path');
request(url, (err, res, body) => {
  if (err) {
    console.error(err);
  } else {
    fs.writeFile(path.resolve(file), body, 'utf8', (err) => {
      if (err) {
        console.error(err);
      }
    });
  }
});
