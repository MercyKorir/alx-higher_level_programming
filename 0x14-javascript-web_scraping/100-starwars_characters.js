#!/usr/bin/node
const id = process.argv[2];
const request = require('request');
const url = `https://swapi.dev/api/films/${id}/`;
request(url, (err, res, body) => {
  if (err) {
    console.error(err);
  } else {
    const data = JSON.parse(body);
    const characters = data.characters;
    characters.forEach(character => {
      request(character, (err, res, body) => {
        if (err) {
          console.error(err);
        } else {
          const characterData = JSON.parse(body);
          console.log(characterData.name);
        }
      });
    });
  }
});
