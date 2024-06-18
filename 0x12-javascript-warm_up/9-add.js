#!/usr/bin/node
const firstArgv = parseInt(process.argv[2])
const secondArgv = parseInt(process.argv[3])
function add(a, b) {
  a = firstArgv;
  b = secondArgv;
  const res = a + b;
  return res;
}
console.log(add(num1, num2));
