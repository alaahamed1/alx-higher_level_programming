#!/usr/bin/node
const args = process.argv.slice(2);
if (args.length < 2) {
  console.log(0);
} else {
  const intArgs = args.map(arg => parseInt(arg)).sort((a, b) => b - a);
  console.log(intArgs[1]);
}
