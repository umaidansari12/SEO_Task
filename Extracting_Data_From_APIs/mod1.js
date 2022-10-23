// Create an index.js file inside a folder & paste the code below

// Import axios module
const axios = require('axios');

// Custom function to extract data from PageSpeed API
const getApiData = async (url) => {
  const endpoint = 'https://www.googleapis.com/pagespeedonline/v5/runPagespeed';
  const key = 'YOUR-GOOGLE-API-KEY' // Edit with your own key;
  const apiResponse = await axios(`${endpoint}?url=${url}&key=${key}`); // Create HTTP call
  console.log(apiResponse.data); // Log data
  return apiResponse.data;
};

// Call your custom function
getApiData('https://www.searchenginejournal.com/');
