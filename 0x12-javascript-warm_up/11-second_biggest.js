#!/usr/bin/node

const argv = process.argv.slice(2);

if (argv.length < 2) {
  console.log(0);
} else {
  let biggestNum = Number(argv[0]);
  let secBigNum = Number(argv[1]);
  if (biggestNum < secBigNum) {
    secBigNum = Number(argv[0]);
    biggestNum = Number(argv[1]);
  }
  for (const i of argv) {
    const num = Number(i);
    if (num > biggestNum) {
      secBigNum = biggestNum;
      biggestNum = num;
    }
    if (num > secBigNum && num < biggestNum) {
      secBigNum = num;
    }
  }
  console.log(secBigNum);
}
