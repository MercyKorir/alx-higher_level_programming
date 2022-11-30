#!/usr/bin/node
const newList = require('./100-data.js').list;
console.log(newList);
console.log(newList.map((val, index) => val * index));
