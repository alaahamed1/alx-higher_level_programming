#!/usr/bin/node

const file1 = process.argv[2];
const file2 = process.argv[3];
const fileDestination = process.argv[4];

const fs = require('fs');

fs.readFile(file1, 'utf8', (err, data) => {
  if (err) {
    console.error(err);
  }
  fs.writeFile(fileDestination, data, err => {
    if (err) {
      console.error(err);
    }
  });
});

fs.readFile(file2, 'utf8', (err, data) => {
  if (err) {
    console.error(err);
  }
  fs.appendFile(fileDestination, data, err => {
    if (err) {
      console.error(err);
    }
  });
});
