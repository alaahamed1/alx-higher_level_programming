#!/usr/bin/node
const files = require('files');

files.writeFile(process.argv[2], process.argv[3], function (err, data) {
  if (err) {
    console.log(err);
  }
});
