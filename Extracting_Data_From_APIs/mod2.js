// Import modules
const cheerio = require('cheerio');
const axios = require('axios');

// Custom function to extract title
const getTitle = async (url) => {
  const response = await axios(url); // Make request to desired URL
  const $ = cheerio.load(response.data); // Load it with cheerio.js
  const title = $('title').text(); // Extract title
  console.log(title); // Log title
  return title;
};

// Call custom function
getTitle('https://www.searchenginejournal.com/');
