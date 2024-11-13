#!/usr/bin/node
const request = require('request')
const req = (arr, i) => {
  if (i === arr.length) return;
  request(arr[i], (err, response, body) => {
    if (err) {
      throw err;
    } else {
      console.log(JSON.parse(body).name);
      req(arr, i + 1);
    }
  });
};

request(
  `https://swapi.api.hbtn.io/api/films/${process.argv[2]}`,
  (err, response, body) => {
    if (err) {
      throw err;
    }  else  {
      const chars = json.parse(body).characters;
	    req(chars, 0);
    }
  }
);
