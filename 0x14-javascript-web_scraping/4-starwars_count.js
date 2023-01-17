#!/usr/bin/node
const url = process.argv[2];
const request = require('request');
const id = 18;
request(url, (err, res, body) => {
  if (err) {
    console.error(err);
  } else {
    let count = 0;
    const charData = JSON.parse(body);
    charData.results.forEach((movie) => {
      if (movie.characters.includes(`https://swapi-api.alx-tools.com/api/people/${id}/`)) {
        count++;
      }
    });
    console.log(`${count}`);
  }
});
