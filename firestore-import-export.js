const { initializeFirebaseApp } = require('firestore-export-import')
const fs = require('fs')
const serviceAccount = require('./service-account.json')

// Initiate Firebase App
initializeFirebaseApp(serviceAccount)

// Export options
const options = {
    //docsFromEachCollection: 10, // limit number of documents when exporting
    refs: ['refKey', 'deep.level.key'], // reference Path
  }




var json = require('./degree_data_processed.json')
const { url } = require('inspector')

fs.writeFile('degree_data_p.json', JSON.stringify(formatData(json)), (err) => {
  if (err) {
    throw err;
  }
})

function formatData(details) {
  var formattedDetails = [];
  for (var id in details) {
    formattedDetails.push({
      university: details[id].university,
      location: details[id].location,
      name: details[id].name,
      url: details[id].url
    });
  }
  return formattedDetails;
}


