#!/usr/bin/node
const request = require('request')
const movieId = process.argv[2]
if (!movieId) {
	console.error("Please provide a movie ID")
	process.exit(1);
}
const url = `https://swapi.dev/api/films/${movieID}/`;
request(url, (error, response, body) => {
	if (error) {
		console.error(error);
		return;

	}

	if (response.statusCode === 200) {
		const filmData = JSON.parse(body);
		const characters = filmData.characters;
		characters.forEach((characterUrl) => {
			request(characterUrl, (error, response, body) => {
				if (!error && response.statusCode === 200) {
					const characterData = JSON.parse(body);
					console.log(characterData.name);
				}
			});
		});
	} else {
		console.error(`Failed to retreive movie Data for ${movieId}`);
	}
});
