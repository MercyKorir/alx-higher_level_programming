#!/usr/bin/node
const url = process.argv[2];
const request = require('request');
request(url, (err, res, body) => {
  if (err) {
    console.error(err);
  } else {
    console.log(`code: ${res.statusCode}`);
  }
});
