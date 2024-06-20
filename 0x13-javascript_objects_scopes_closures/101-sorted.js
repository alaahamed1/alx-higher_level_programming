#!/usr/bin/node

const dict = require('./101-data.js').dict;

const newDict = {};

for (const UserId in dict) {
  const occurrences = dict[UserId];

  if (!(occurrences in newDict)) {
 newDict[occurrences] = [];
  }

 newDict[occurrences].push(UserId);
}
console.log (newDict);
