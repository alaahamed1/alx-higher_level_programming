#!/usr/bin/node

const argv = process.argv[2];

if (argv) {
  console.log(argv);
} else if (argv === undefined) {
  console.log('No argument');
}
