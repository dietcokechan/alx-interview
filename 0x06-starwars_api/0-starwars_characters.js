#!/usr/bin/node

const request = require('request');
const filmID = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${filmID}`;

request(url, async (err, res, body) => {
  if (err) {
    console.log(err);
  }
  for (const charID of JSON.parse(body).characters) {
    await new Promise((resolve, reject) => {
      request(charID, (err, res, body) => {
        if (err) {
          reject(err);
        }
        console.log(JSON.parse(body).name);
        resolve();
      });
    });
  }
});
