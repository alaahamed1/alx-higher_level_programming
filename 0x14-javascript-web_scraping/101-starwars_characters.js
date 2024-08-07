#!/usr/bin/node

const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];

request(url, function (err, body) {
  if (!err) {
    const obj = JSON.parse(body);
    const characters = obj.characters;

    for (const character of characters) {
      request(character, function (err, body) {
        if (!err) {
          console.log(JSON.parse(body).name);
        }
      });
    }
  }
});
