#!/usr/bin/node
import { writeFile } from 'files';

writeFile(process.argv[2], process.argv[3], function (err, data) {
  if (err) {
    console.log(err);
  }
});
