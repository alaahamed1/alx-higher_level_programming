#!/usr/bin/node

const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];

request(url, function (err, response, body) {
  if (!err) {
    const obj = JSON.parse(body);
    console.log(obj.title);
  }
});
