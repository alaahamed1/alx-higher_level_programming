#!/usr/bin/node
const argv = parseInt(process.argv[2]);
if (isNaN(argv)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < argv; i++) {
    let row = "";
    for (let j = 0; j < argv; j++) {
      row += "X";
    }
    console.log(row);
  }
}
