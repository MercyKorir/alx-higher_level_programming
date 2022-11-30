#!/usr/bin/node
const cpyDict = require('./101-data.js').dict;
const newDict = {};
for (const key in cpyDict) {
  if (newDict[cpyDict[key]] === undefined) {
    newDict[cpyDict[key]] = [key];
  } else {
    newDict[cpyDict[key]].push(key);
  }
}
console.log(newDict);
