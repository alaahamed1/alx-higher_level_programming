#!/usr/bin/node
function add(a, b) {
  const firstArgv = parseInt(process.argv[2])
  const secondArgv = parseInt(process.argv[3])
  a = firstArgv;
  b = secondArgv;
  res = a + b;
  console.log(res)
}
add()
