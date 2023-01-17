#!/usr/bin/node
const ep = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${ep}`;
const request = require('request');
request(url, (err, res, body) => {
  if (err) {
    console.error(err);
  } else {
    const data = JSON.parse(body);
    console.log(`${data.title}`);
  }
});
