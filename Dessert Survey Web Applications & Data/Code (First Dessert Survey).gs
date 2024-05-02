// Function to handle GET requests and serve the HTML page from file.
function doGet(e) {
  return HtmlService.createHtmlOutputFromFile('WebApp');
}

// Function to add a new record to the Google Sheet based on dessert attributes provided.
function AddRecord(dessertName, dessertType, dessertDensity, dessertSweetness, dessertTartness, timeEaten, dessertRanking1_10, chocolate, whiteChocolate, mAndMs, pretzels, caramel, diffFruit, banana, strawberry, blueberry, cherry, orange, lemon) {
  // URL of the Google Sheet where data is stored
  var url = 'https://docs.google.com/spreadsheets/d/1qMG-DlyWZsGrb4tlCmQajL17u-LYSRcSPbNF2bzn8f4/edit?pli=1#gid=0';
  // Open the spreadsheet by URL
  var ss= SpreadsheetApp.openByUrl(url);
  // Access the specific sheet by name
  var webAppSheet = ss.getSheetByName("Sheet1");
  // Append the new row with data from the function arguments and the current date
  webAppSheet.appendRow([dessertName, dessertType, dessertDensity, dessertSweetness, dessertTartness, timeEaten, dessertRanking1_10, chocolate, whiteChocolate, mAndMs, pretzels, caramel, diffFruit, banana, strawberry, blueberry, cherry, orange, lemon, new Date()]);
  
}
