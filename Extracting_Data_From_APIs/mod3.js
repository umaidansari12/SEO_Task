// Import Modules
const csv = require('csvtojson');
const { parse } = require('json2csv');
const { writeFileSync } = require('fs');

// Custom function to read URLs and convert it to JSON
const readCsvExportJson = async () => {
  const json = await csv().fromFile('yourfile.csv');
  console.log(json); // Log conversion JSON

  const converted = parse(json);
  console.log(converted); // Log conversion to CSV
  writeFileSync('new-csv.csv', converted);
};

readCsvExportJson();